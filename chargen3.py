#!/usr/bin/python3

"""
chargen v3 is a character creation tool for tabletop roleplaying games
v3 is geared towards using an api to determine character information
"""
import math
import random
import argparse
import json
import requests

###############################################################################
# argument parsing

parser = argparse.ArgumentParser(prog='chargen', description=\
    'Generate characters for games')
subparsers = parser.add_subparsers(title='subcommands', description=\
    'valid subcommands', help='type of character to generate', dest='game_arg')
parser_fivee = subparsers.add_parser('five_e', help=\
    'Dungeons and Dragons 5th Edition')
parser_fivee.add_argument("-2", "--two-array", action="store_true", \
   dest="two_array", default=False,\
   help="use a 2d6+6 method")
parser_fivee.add_argument("-3", "--three-array", action="store_true",\
   dest="three_array", default=False,\
   help="use a 3d6 straight value method")
parser_fivee.add_argument("-4", "--four-array", action="store_true", \
   dest="four_array", default=True,\
   help="use a 4d6 drop the lowest method (default)")
parser.add_argument("-a", "--api", dest="api_url", default=\
    "https://api.open5e.com/", help="base URL for API")
parser_fivee.add_argument("-r", "--random", action="store_true", dest="random",\
    default=False, help="randomly generate the character (not default)")
parser_fivee.add_argument("-v", "--background", action="store_true", \
    dest="background", default=False, \
    help="create background (not default)")
args = parser.parse_args()

###############################################################################
# object classes
class FiveECharacter():
    """ Dungeons and Dragons 5th edition Character """
    def __init__(self, data_dict):
        '''create character'''
        self.first_name = prompt_from_options("names", \
            get_name_selection("firstnames.txt"))
        self.last_name = prompt_from_options("names", \
            get_name_selection("surnames.txt"))
        self.race_name = prompt_from_options("races", data_dict["races"])
        for count, value in enumerate(data_dict["races"]):
            if self.race_name == value["name"]:
                race_number = count
        self.class_name = prompt_from_options("classes", data_dict["classes"])
        if args.background:
            self.background = prompt_from_options("backgrounds", \
                data_dict["backgrounds"])
        self.stats = fivee_get_stats(data_dict["races"][race_number]["asi"])
        self.hit_points = fivee_get_hp(data_dict, self.class_name, \
            self.stats["constitution"])

###############################################################################
# functions
def roll_dx(num):
    '''returns a number between one and num'''
    rollresult = random.randint(1,num)
    return rollresult

def roll_to_x(num):
    '''returns a number between 0 and num'''
    rollresult = random.randint(0,num)
    return rollresult

def file_len(file_name):
    '''open the file, count the lines, return'''
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_name(file_name):
    '''function to get content from a line in file'''
    num_of_lines = file_len(file_name)
    random_num = random.randint(0, num_of_lines)
    file = open(file_name)
    all_lines = file.readlines()
    return str(all_lines[random_num].strip())

def get_name_selection(file_name):
    """similar to get_name, used to get 10 random names"""
    name_list = []
    for i in range(0,9):
        num_of_lines = file_len(file_name)
        random_num = random.randint(0, num_of_lines)
        file = open(file_name)
        all_lines = file.readlines()
        name_list.append({"name": str(all_lines[random_num].strip())})
    return name_list

def fivee_get_stats(asi_list):
    """returns the dict of ability scores"""
    scores = {}
    scores_names = ["strength", "dexterity", "constitution", "intelligence", \
        "wisdom", "charisma"]
    available_scores = ["strength", "dexterity", "constitution", "intelligence", \
        "wisdom", "charisma"]
    increase_scores = []
    for increase in asi_list:
        stat_name = increase["attributes"][0].lower()
        value = increase["value"]
        if stat_name == "other" and stat_name not in available_scores:
            stat_name = available_scores[random.randint(0, len(available_scores) -1)]
        increase_scores.append({"name": stat_name, "amount": value})
        available_scores.remove(stat_name)
    scores = {}
    for score in scores_names:
        scores[score] = fivee_roll_stat(score, increase_scores)
    return scores

def fivee_roll_stat(score_name, increase_scores):
    '''creates a text output of a score for a stat'''
    stat_score_list = []
    if args.two_array is True:
        for i in range(2):
            stat_score_list.append(roll_dx(6))
        stat_score = stat_score_list[0] + stat_score_list[1] + 6
    elif args.three_array is True:
        for i in range(3):
            stat_score_list.append(roll_dx(6))
        stat_score = stat_score_list[0] + stat_score_list[1] + stat_score_list[2]
    elif args.four_array is True:
        for i in range(4):
            stat_score_list.append(roll_dx(6))
            stat_score_list.sort(reverse=True)
        stat_score_list.pop(-1)
        stat_score = stat_score_list[0] + stat_score_list[1] + stat_score_list[2]
    for count, value in enumerate(increase_scores):
        if score_name in value["name"]:
            #print(f'adding {increase_scores[count]["amount"]} to {stat_score} ({value["name"]})')
            stat_score = stat_score + increase_scores[count]["amount"]
    modifier = math.floor(( stat_score - 10) / 2)
    return {"score": stat_score, "modifier": modifier}

def fivee_get_hp(data_dict, class_name, constitution):
    """uses the class name to find starting hp from data dict"""
    for count, value in enumerate(data_dict["classes"]):
        if value["name"] == class_name:
            class_int = count
    hp_string = data_dict["classes"][class_int]["hp_at_1st_level"]
    value = int(hp_string.split(" ")[0])
    value = value + constitution["modifier"]
    return value

def prompt_from_options(option_name, json_struct):
    '''asks the user what to pick out of available options'''
    if not args.random:
        print(f"Please pick one of the following options from character {option_name}: ")
        for count, value in enumerate(json_struct):
            print(f"{count}: {value['name']}")
        selection = input(f"Pick by number, or 'r' for random: ")
        if selection == "r":
            selection = random.randint(0, len(json_struct))
        if type(selection) is not int:
            selection = int(selection)
    else:
        selection = random.randint(0, len(json_struct) -1)
    return json_struct[selection]["name"]

def main():
    '''main loop'''
    r = requests.get(args.api_url, timeout=30)
    #print(r.json())
    data_dict = {}
    for endpoint in r.json().items():
        endpoint_name = endpoint[0]
        local_request = requests.get(endpoint[1], timeout=30)
        data_dict[endpoint_name] = local_request.json()["results"]
    player = FiveECharacter(data_dict)
    print(json.dumps(player.__dict__))

###############################################################################
# main
if __name__ == '__main__':
    if args.game_arg is not None:
        main()
    else:
        parser.print_help()

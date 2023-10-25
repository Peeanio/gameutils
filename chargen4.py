import argparse
import json
import chargen

parser = argparse.ArgumentParser(prog='chargen.py', description=\
    'Generate characters for games')
subparsers = parser.add_subparsers(title='subcommands', \
    description='valid subcommands', help='type of character to gen',\
    dest="game_arg")
parser_cyberpunk = subparsers.add_parser('cyberpunk',\
 help='Cyberpunk 2020')
parser_ose = subparsers.add_parser('ose',\
 help='Old School Essentials Advanced')
parser_ose.add_argument("-b", "--basic", action="store_true", \
   dest="oseBasic", default=True,\
   help="Old School Essentials Basic")
parser_ose.add_argument("-a", "--advanced", action="store_true", \
   dest="oseAdvanced", default=False,\
   help="Old School Essentials Advanced")
parser_fivee = subparsers.add_parser('five_e', \
    help='Dungeons and Dragons 5th Edition')
parser_fivee.add_argument("-2", "--two-array", action="store_true", \
   dest="twoArray", default=False,\
   help="use a 2d6+6 method")
parser_fivee.add_argument("-3", "--three-array", action="store_true",\
   dest="threeArray", default=False,\
   help="use a 3d6 straight value method")
parser_fivee.add_argument("-4", "--four-array", action="store_true", \
   dest="fourArray", default=True,\
   help="use a 4d6 drop the lowest method (default)")
args = parser.parse_args()


five_e_stat_name_list = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
five_e_race_list = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling",\
    "Half-Orc", "Human", "Tiefling"]

class Character_Five_E:
  '''character object for D&D 5th ed'''
  def __init__(self, arg_dict):
    self.name = Character_Name()
    self.race = fiveERollRace()
    self.stats = {}
    for stat in five_e_stat_name_list:
        self.stats[stat] = Character_Five_E_Stat(stat, self.race, arg_dict)


class Character_Name:
  '''name object consists of a dict of first and last name'''
  def __init__(self):
    characterFirstName = chargen.getname("firstnames.txt")
    nameChance = chargen.rollDx(10)
    if nameChance == 1:
      characterLastName = "of " + chargen.getname("surnames.txt")
    elif nameChance == 2:
      characterLastName = chargen.getname("surnames.txt") + "-" + chargen.getname("surnames.txt")
    else:
      characterLastName = chargen.getname("surnames.txt")

    self.firstName = characterFirstName
    self.lastName  = characterLastName

class Character_Five_E_Stat:
    '''object for a stat in 5e of score, modifier, and name'''
    def __init__(self, name, race, args):
        statScoreList = []
        if args['twoArray'] == True:
            for i in range(2):
                    statScoreList.append(chargen.rollDx(6))
            statScore = statScoreList[0] + statScoreList[1] + 6
        elif args['threeArray'] == True:
            for i in range(3):
                statScoreList.append(chargen.rollDx(6))
            statScore = statScoreList[0] + statScoreList[1] + statScoreList[2]
        elif args['fourArray'] == True:
            for i in range(4):
                statScoreList.append(chargen.rollDx(6))
                statScoreList.sort(reverse=True)
            statScoreList.pop(-1)
            statScore = statScoreList[0] + statScoreList[1] + statScoreList[2]
        modifier = chargen.dndReturnModifier(statScore)
        self.score = statScore
        self.modifier = modifier

def fiveERollRace():
#picks a random race from list
    numOfRace = chargen.rollToX(len(five_e_race_list) - 1)
    characterRace = five_e_race_list[numOfRace]
    return characterRace


if __name__ == '__main__':
    if args.game_arg == "cyberpunk":
        genCharacter()
    elif args.game_arg == "five_e":
        character = Character_Five_E(vars(args))
    elif args.game_arg == "ose":
        genOseCharacter()
    else:
        parser.print_help()
        exit()

    print(json.dumps(character, default=lambda o: o.__dict__))


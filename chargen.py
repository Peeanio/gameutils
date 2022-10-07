#!/usr/bin/python3
#python version of chargens script
#Author: Max Russell

import random
#libary for random number generation
import sys
#file opening
import argparse 
#for argument parsing
import json
#output formatting

########################################################################
# option parsing setup

parser = argparse.ArgumentParser(prog='chargen.py', description=\
    'Generate characters for games')
subparsers = parser.add_subparsers(title='subcommands', \
    description='valid subcommands', help='type of character to gen',\
    dest="game_arg")
parser_cyberpunk = subparsers.add_parser('cyberpunk', help='Cyberpunk 2020')
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
#parser.add_argument("-c", "--2020", action="store_true", dest="cyberpunk",\
#	help="generate Cyberpunk 2020V2 character")
#parser.add_argument("-f", "--5e", action="store_true", dest="fifthE",\
#    help="generate a 5th ed SRD character")
args = parser.parse_args()

########################################################################
#functions
def rollDx(x):
#returns a number between one and x
	rollresult = random.randint(1,x)
	return rollresult

def rollToX(x):
#returns a number between 0 and x
	rollresult = random.randint(0,x)
	return rollresult

def rollStat(stat):
#creates a text output of a score for a stat
	statScore = (rollDx(10))
	while statScore == 1:
			statScore = (rollDx(10))
	print(stat + " is: " + str(statScore))

def rollBackstory():
#generates the player class and some fluff to make more interesting
	global playerClass #this makes it available outside the functions
	playerClass = arrayClasses[rollToX(9)]
	playerClothes = arrayClothes[rollToX(9)]
	playerEthnicity = arrayEthnicity[rollToX(9)]
	playerParents = arrayParents[rollToX(9)]
	print("Class is: " + str(playerClass))
	print("Clothes are: " + str(playerClothes))
	print("Ethnicity is: " + str(playerEthnicity))
	print("Parents are/were: " + str(playerParents))

def rollCyberWare():
#rolls for cybernetics for character
	global characterCyberWare
	if str(playerClass) == str("Solo"):
	#solo has more rolls
		rollCyberwareSub(6)
	else:
		rollCyberwareSub(3)

def rollCyberwareSub(y):
#subfunction to generate cyberware, does the actual rolls. So I only have to change
#one place
	rolledCyberware = [0 for x in range(y)]
	characterCyberWare = [0 for x in range(y)]
	for x in range(y):
		rolledCyberware[x] = rollDx(10)
		characterCyberWare[x] = arrayCyberWare[rolledCyberware[x]]
	for x in rolledCyberware:
		if x == 1:
			cyberOptics = str(arrayCyberoptics[rollToX(5)])
			print("Cyberoptics are: " + cyberOptics)
		elif x == 2:
			cyberArm = str(arrayCyberarm[rollToX(5)])
			print("Cyberarm is: " + cyberArm)
		elif x == 3:
			cyberAudio = str(arrayCyberaudio[rollToX(5)])
			print("Cyberaudio is: " + cyberAudio)
		else:
			print("Cyberware is: " + str(arrayCyberWare[x]))

def rollWeapons():
#generates a weapon and armour based on class
	global characterArmor
	global characterWeapon
	wepArm = rollToX(9)
	if str(playerClass) == str("Nomad") or str(playerClass) == str("Cop"):
		wepArm += 2
	elif str(playerClass) == str("Solo"):
		wepArm += 3
	while wepArm >= 10:
		wepArm = 9
	print("Armor is: " + arrayArmor[wepArm])
	print("Weapon is: " + arrayWeapons[wepArm])

def genCharacter():
	print ("Name is: " +getname("firstnames.txt") + " " + getname("surnames.txt"))
	for x in range(0,len(statsValues)):
		statsValues[x] = rollStat(statsLongNames[x])
	rollBackstory()
	rollCyberWare()
	rollWeapons()


def file_len(fname):
#open file, count the lines, return
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def getname(filename):
#function to make repeatable
        #get the number of lines, then get a random number between 0 and it
        numoflines = file_len(filename)
        randomnum = random.randint(0,numoflines)

        #open the file, read it, print only the generated line number
        file = open(filename)
        all_lines = file.readlines()
        return str(all_lines[randomnum].strip())

def gen5eCharacter():
#generates a 5th ed SRD character
    characterFirstName = getname("firstnames.txt") 
    nameChance = rollDx(10)
    if nameChance == 1:
      characterLastName = "of " + getname("surnames.txt")
    elif nameChance == 2:
      characterLastName = getname("surnames.txt") + "-" + getname("surnames.txt")
    else:
      characterLastName = getname("surnames.txt")
    for x,y in statDict.items():
        characterStatDict[x] = dndRollStat(x)

    characterRace = dndRollRace()
    characterClass, characterHitPoints = dndRollClass()
    print(json.dumps({'name': {'firstName': characterFirstName, 'lastName':\
        characterLastName}, 'race': characterRace, 'class': characterClass, \
        'hitPoints': characterHitPoints, 'stats': characterStatDict}))

def dndRollStat(stat):
#creates a text output of a score for a stat
   statScoreList = []
   if args.twoArray == True:
       for i in range(2):
            statScoreList.append(rollDx(6))
       statScore = statScoreList[0] + statScoreList[1] + 6
   elif args.threeArray == True:
      for i in range(3):
         statScoreList.append(rollDx(6))
      statScore = statScoreList[0] + statScoreList[1] + statScoreList[2]
   elif args.fourArray == True:
      for i in range(4):
         statScoreList.append(rollDx(6))
         statScoreList.sort(reverse=True)
      statScoreList.pop(-1)
      statScore = statScoreList[0] + statScoreList[1] + statScoreList[2]
   return statScore

def dndRollRace():
#picks a random race and increments stats
    numOfRace = rollToX(len(dndRaceList) - 1)
    characterRace = dndRaceList[numOfRace]
    if characterRace == "Dragonborn":
        characterStatDict.update({'STR': characterStatDict['STR']+ 2})
        characterStatDict.update({'CHA': characterStatDict['CHA']+ 1})
    if characterRace == "Dwarf":
        characterStatDict.update({'CON': characterStatDict['CON']+ 2})
        characterStatDict.update({'WIS': characterStatDict['WIS']+ 1})
    if characterRace == "Elf":
        characterStatDict.update({'DEX': characterStatDict['DEX']+ 2})
        characterStatDict.update({'INT': characterStatDict['INT']+ 1})
    if characterRace == "Gnome":
        characterStatDict.update({'INT': characterStatDict['INT']+ 2})
        characterStatDict.update({'CON': characterStatDict['CON']+ 1})
    if characterRace == "Half-Elf":
        characterStatDict.update({'CHA': characterStatDict['CHA']+ 2})
        randStatNum = rollToX(5)
        randStat = statList[randStatNum]
        characterStatDict.update({randStat: characterStatDict[randStat]+ 1})
    if characterRace == "Halfing":
        characterStatDict.update({'DEX': characterStatDict['DEX']+ 2})
        characterStatDict.update({'CHA': characterStatDict['CHA']+ 1})
    if characterRace == "Half-Orc":
        characterStatDict.update({'STR': characterStatDict['STR']+ 2})
        characterStatDict.update({'CON': characterStatDict['CON']+ 1})
    if characterRace == "Human":
        characterStatDict.update({'STR': characterStatDict['STR']+ 1})
        characterStatDict.update({'DEX': characterStatDict['DEX']+ 1})
        characterStatDict.update({'CON': characterStatDict['DEX']+ 1})
        characterStatDict.update({'INT': characterStatDict['DEX']+ 1})
        characterStatDict.update({'WIS': characterStatDict['DEX']+ 1})
        characterStatDict.update({'CHA': characterStatDict['DEX']+ 1})
    if characterRace == "Tiefling":
        characterStatDict.update({'CHA': characterStatDict['CHA']+ 2})
        characterStatDict.update({'INT': characterStatDict['INT']+ 1})
    return characterRace

def dndRollClass():
#picks a random class, prepares hitpoints, kicks off additional generation
    numOfClass = rollToX(len(dndClassList) - 1)
    characterClass = dndClassList[numOfClass]
    if characterClass == "Barbarian":
       pass 
    if characterClass == "Bard":
        pass
    if characterClass == "Cleric":
        pass
    if characterClass == "Druid":
        pass
    if characterClass == "Fighter":
        pass
    if characterClass == "Monk":
        pass
    if characterClass == "Paladin":
        pass
    if characterClass == "Ranger":
        pass
    if characterClass == "Rogue":
        pass
    if characterClass == "Sorcerer":
        pass
    if characterClass == "Warlock":
        pass
    if characterClass == "Wizard":
        pass
    characterHitPoints = dndClassHitDieDict[characterClass]
    return characterClass, characterHitPoints

def dndGenBarbarian():
    pass
def dndGenBard():
    pass
def dndGenCleric():
    pass
def dndGenDruid():
    pass
def dndGenFighter():
    pass
def dndGenMonk():
    pass
def dndGenPaladin():
    pass
def dndGenRanger():
    pass
def dndGenRogue():
    pass
def dndGenSorcerer():
    pass
def dndGenWarlock():
    pass
def dndGenWizard():
    pass
########################################################################
#cyberpunk declare arrays
arrayClasses=["Solo", "Rocker", "Netrunner", "Media", "Nomad", "Fixer",\
 "Cop", "Corporate", "Techie", "Medtechie"]
arrayClothes=["Biker Leathers", "Blue Jeans", "Corporate Suits", \
"Jumpsuits", "Miniskirts", "High Fashion", "Cammos", "Normal Clothes", \
"Nude", "Bag Lady Chich"]
arrayEthnicity=["Anglo-American", "African", "Japanese/Korean", \
"Central European/Soviet", "Pacific Islander", \
"Chinese/Southeast Asian", "Black American", "Hispanic American", \
"Central/South American", "European"]
arrayParents=["Corporate Executive", "Corporate Manager", \
"Corporate Technician", "Nomad Pack", "Pirate Fleet", "Gang Family", \
"Crime Lord", "Combat Zone Poor", "Urban Homeless", "Arcology Family"]
statsLongNames=["Intelligence", "Reflex", "Technology", "Cool", "Luck",\
 "Attractiveness", "Movement Allowance", "Empathy", "Body"]
statsShortNames=["int", "ref", "tech", "cool", "luck", "att", "ma", \
"emp", "body"]
statsValues=[0 for x in range(9)]
arrayCyberWare=["Blank", "Cyberoptics", "Cyberarm with gun", "Cyberaudio",\
 "Big Nucks", "Rippers", "Vampires", "Slice n' Dice",\
 "Reflex Boost (Kerenzikov)", "Reflex Boost (Sandevistan)", "Nothing"]
arrayCyberoptics=["Infrared", "Lowlight", "Camera", "Dartgun",\
 "Antidazzle", "Targeting Scope"]
arrayCyberarm=["Med. Pistol", "Light Pistol", "Med. Pistol",\
 "Light Submachinegun", "Very Heavy Pistol", "Heavy Pistol"]
arrayCyberaudio=["Wearman", "Radio Splice", "Phone link",\
 "Amplified Hearing", "Sound Editing", "Digital Recording Link"]
arrayArmor=["Heavy Leather", "Armor Vest", "Light Armor Jacket",\
 "Light Armor Jacket", "Med Armor Jacket", "Med Armor Jacket",\
 "Med Armour Jacket", "Heavy Armor Jacket", "Heavy Armor Jacket",\
 "Metalgear"]
arrayWeapons=["Knife", "Light pistol", "Med pistol", "Heavy Pistol",\
 "Heavy Pistol", "Light SMG", "Lt. Assault Rifle", "Med Assault Rifle",\
  "Hvy. Assault rifle", "Hvy. Assault Rifle"]

########################################################################
#5e declare values
statDict = { "STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
statList = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
characterStatDict = dict()
dndRaceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling",\
    "Half-Orc", "Human", "Tiefling"]
dndClassList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", \
    "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
dndClassHitDieDict = {"Barbarian": 12, "Bard": 8, "Cleric": 8, "Druid": 8, \
    "Fighter": 10, "Monk": 8, "Paladin": 10, "Ranger": 10, "Rogue": 8, \
    "Sorcerer": 6, "Warlock": 8, "Wizard": 6 }
#######################################################################
#main
if args.game_arg == "cyberpunk":
	genCharacter()
elif args.game_arg == "five_e":
    gen5eCharacter()
else:
    parser.print_help()

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
    characterClass, characterHitPoints, dndProficiencies, equipment, features = dndRollClass()
    print(json.dumps({'name': {'firstName': characterFirstName, 'lastName':\
        characterLastName}, 'race': characterRace, 'class': characterClass, \
        'hitPoints': characterHitPoints, 'stats': characterStatDict, \
        'proficiencies': dndProficiencies, "equipment": equipment, "features": features}))

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
   modifier = dndReturnModifier(statScore)
   return {"score": statScore, "modifier": modifier}

def dndReturnModifier(statScore):
   #determine modifier
   if statScore == 1:
       modifier = -5
   elif statScore == 2 or statScore == 3:
       modifier = -4
   elif statScore == 4 or statScore == 5:
       modifier = -3
   elif statScore == 6 or statScore == 7:
       modifier = -2
   elif statScore == 8 or statScore == 9:
       modifier = -1
   elif statScore == 10 or statScore == 11:
       modifier = 0
   elif statScore == 12 or statScore == 13:
       modifier = 1
   elif statScore == 14 or statScore == 15:
       modifier = 2
   elif statScore == 16 or statScore == 17:
       modifier = 3
   elif statScore == 18 or statScore == 19:
       modifier = 4
   elif statScore == 20 or statScore == 21:
       modifier = 5
   return modifier

def dndRollRace():
#picks a random race and increments stats
    numOfRace = rollToX(len(dndRaceList) - 1)
    characterRace = dndRaceList[numOfRace]
    if characterRace == "Dragonborn":
        characterStatDict.update({'STR': {"score": characterStatDict['STR']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['STR']["score"]+ 2)}})
        characterStatDict.update({'CHA': {"score": characterStatDict['CHA']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['CHA']["score"]+ 1)}})
    if characterRace == "Dwarf":
        characterStatDict.update({'CON': {"score": characterStatDict['CON']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['CON']["score"]+ 2)}})
        characterStatDict.update({'WIS': {"score": characterStatDict['WIS']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['WIS']["score"]+ 1)}})
    if characterRace == "Elf":
        characterStatDict.update({'DEX': {"score": characterStatDict['DEX']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['DEX']["score"]+ 2)}})
        characterStatDict.update({'INT': {"score": characterStatDict['INT']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['INT']["score"]+ 1)}})
    if characterRace == "Gnome":
        characterStatDict.update({'INT': {"score": characterStatDict['INT']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['INT']["score"]+ 2)}})
        characterStatDict.update({'CON': {"score": characterStatDict['CON']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['CON']["score"]+ 1)}})
    if characterRace == "Half-Elf":
        characterStatDict.update({'CHA': {"score": characterStatDict['CHA']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['CHA']["score"]+ 2)}})
        randStatNum = rollToX(5)
        randStat = statList[randStatNum]
        characterStatDict.update({randStat: {"score": characterStatDict[randStat]["score"]+ 1, "modifier": dndReturnModifier(characterStatDict[randStat]["score"]+ 1)}})
    if characterRace == "Halfing":
        characterStatDict.update({'DEX': {"score": characterStatDict['DEX']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['DEX']["score"]+ 2)}})
        characterStatDict.update({'CHA': {"score": characterStatDict['CHA']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['CHA']["score"]+ 1)}})
    if characterRace == "Half-Orc":
        characterStatDict.update({'STR': {"score": characterStatDict['STR']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['STR']["score"]+ 2)}})
        characterStatDict.update({'CON': {"score": characterStatDict['CON']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['CON']["score"]+ 1)}})
    if characterRace == "Human":
        characterStatDict.update({'STR': {"score": characterStatDict['STR']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['STR']["score"]+ 1)}})
        characterStatDict.update({'DEX': {"score": characterStatDict['DEX']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['DEX']["score"]+ 1)}})
        characterStatDict.update({'CON': {"score": characterStatDict['CON']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['CON']["score"]+ 1)}})
        characterStatDict.update({'INT': {"score": characterStatDict['INT']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['INT']["score"]+ 1)}})
        characterStatDict.update({'WIS': {"score": characterStatDict['WIS']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['WIS']["score"]+ 1)}})
        characterStatDict.update({'CHA': {"score": characterStatDict['CHA']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['CHA']["score"]+ 1)}})
    if characterRace == "Tiefling":
        characterStatDict.update({'CHA': {"score": characterStatDict['CHA']["score"]+ 2, "modifier": dndReturnModifier(characterStatDict['CHA']["score"]+ 2)}})
        characterStatDict.update({'INT': {"score": characterStatDict['INT']["score"]+ 1, "modifier": dndReturnModifier(characterStatDict['INT']["score"]+ 1)}})
    return characterRace

def dndRollClass():
#picks a random class, prepares hitpoints, kicks off additional generation
    numOfClass = rollToX(len(dndClassList) - 1)
    characterClass = dndClassList[numOfClass]
    if characterClass == "Barbarian":
        dndProficiencies, equipment, features = fiveEGenBarbarian()
    if characterClass == "Bard":
        dndProficiencies, equipment, features = fiveEGenBard()
    if characterClass == "Cleric":
        dndProficiencies, equipment, features = fiveEGenCleric()
    if characterClass == "Druid":
        dndProficiencies, equipment, features = fiveEGenDruid()
    if characterClass == "Fighter":
        dndProficiencies, equipment, features = fiveEGenFighter()
    if characterClass == "Monk":
        dndProficiencies, equipment, features = fiveEGenMonk()
    if characterClass == "Paladin":
        dndProficiencies, equipment, features = fiveEGenPaladin()
    if characterClass == "Ranger":
        dndProficiencies, equipment, features = fiveEGenRanger()
    if characterClass == "Rogue":
        dndProficiencies, equipment, features = fiveEGenRogue()
    if characterClass == "Sorcerer":
        dndProficiencies, equipment, features = fiveEGenSorcerer()
    if characterClass == "Warlock":
        dndProficiencies, equipment, features = fiveEGenWarlock()
    if characterClass == "Wizard":
        dndProficiencies, equipment, features = fiveEGenWizard()
    characterHitPoints = dndClassHitDieDict[characterClass] + characterStatDict["CON"]["modifier"]
    return characterClass, characterHitPoints, dndProficiencies, equipment, features

def fiveEGenBarbarian():
    dndSavingThrows = ["STR", "CON"]
    dndWeaponsProficiencies = ["simple weapons", "martial weapons"]
    dndArmourProficiencies = ["light armour", "medium armour", "shields"]
    skills = chooseFromList(2, ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList[1, ["greataxe", ""]], chooseFromList[1, ["handaxe x2", ""]], "explorer's pack", "javelin x4"]
    features = ["Rage", "Unarmoured Defence"]
    return profDict, equipment, features

def fiveEGenBard():
    dndSavingThrows = ["DEX", "CHA"]
    dndWeaponsProficiencies = ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"]
    dndArmourProficiencies = ["light armour"]
    skills = chooseFromList(3, ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["rapier", "longsword", ""]), chooseFromList(1, ["diplomat's pack", "entertainer's pack"]), chooseFromList(1, ["lute", ""]), "leather armour", "dagger"]
    features = ["Spellcasting", "Ritual casting", "Bardic Inspiration"]
    return profDict, equipment, features

def fiveEGenCleric():
    dndSavingThrows = ["WIS", "CHA"]
    dndWeaponsProficiencies = ["simple weapons"]
    dndArmourProficiencies = ["light armour", "medium armour", "shields"]
    skills = chooseFromList(2, ["History", "Insight", "Medicine", "Persuasion", "Religion"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["mace", "warhammer"]), chooseFromList(1, ["scale armour", "leather armour", "chain mail"]), chooseFromList(1, ["light crossbow, twenty bolts", ""]), chooseFromList(1, ["priest's pack", "explorer's pack"]), "shield", "holy symbol"]
    features = ["Spellcasting", "Ritual Casting", chooseFromList(1, ["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain"])]
    return profDict, equipment, features

def fiveEGenDruid():
    dndSavingThrows = ["INT", "WIS"]
    dndWeaponsProficiencies = ["clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitarts", "sickles", "slings", "spears"]
    dndArmourProficiencies = ["light armour", "medium armour", "shields", "no metal armour"]
    skills = chooseFromList(2, ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["wooden shield", ""]), chooseFromList(1, ["scimitar", ""]), "leather armour", "explorer's pack", "druidic focus"]
    features = ["Spellcasting", "Ritual casting", "Druidic"]
    return profDict, equipment, features

def fiveEGenFighter():
    dndSavingThrows = ["STR", "CON"]
    dndWeaponsProficiencies = ["simple weapons", "martial weapons"]
    dndArmourProficiencies = ["all armour", "shields"]
    skills = chooseFromList(2, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["Chain mail", "leather armour, longbow, 20 arrows"]), chooseFromList(1, [" and a shield", "two "]), chooseFromList(1, ["light crossbow, 20 bolts", "handaxe x2"]), chooseFromList(1, ["dungeoneer's pack", "explorer's pack"])]
    features = [chooseFromList(1, ["Archery", "Defence", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]), "Second Wind"]
    return profDict, equipment, features

def fiveEGenMonk():
    dndSavingThrows = ["STR", "DEX"]
    dndWeaponsProficiencies = ["simple weapons", "shortswords"]
    dndArmourProficiencies = []
    skills = chooseFromList(2, ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["shortsword", ""]), chooseFromList(1, ["dungeoneer's pack", "explorer's pack"]), "darts x10"]
    features = ["Martial Arts", "Unarmoured Defence"]
    return profDict, equipment, features

def fiveEGenPaladin():
    dndSavingThrows = ["WIS", "CHA"]
    dndWeaponsProficiencies = ["simple weapons", "martial weapons"]
    dndArmourProficiencies = ["all armour", "shields"]
    skills = chooseFromList(2, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, [" and a shield", " x2"]), chooseFromList(1, ["javelins x5", ""]), chooseFromList(1, ["priests's pack", "explorer's pack"]), "chain mail", "holy symbol"]
    features = ["Divine Sense", "Lay on Hands"]
    return profDict, equipment, features

def fiveEGenRanger():
    dndSavingThrows = ["STR", "DEX"]
    dndWeaponsProficiencies = ["simple weapons", "martial weapons"]
    dndArmourProficiencies = ["light armour", "medium armour", "shields"]
    skills = chooseFromList(3, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["scale mail", "leather armour"]), chooseFromList(1, ["shortsword x2", " x2"]), chooseFromList(1, ["dungeoneer's pack", "explorer's pack"]), "longbow", "arrows x20"]
    features = ["Favour enemy: " + chooseFromList(1, ["aberrations", "beasts", "celestials", "constructs", "dragons", "elementals", "fey", "fiends", "giants", "monstrosities", "oozes", "plants", "undead", "humanoids"]), "Natural Explorer: " + chooseFromList(1, ["arctic", "coast", "desert", "forest", "grassland", "mountain", "swamp", "Underdark"])]
    return profDict, equipment, features

def fiveEGenRogue():
    dndSavingThrows = ["DEX", "INT"]
    dndWeaponsProficiencies = ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"]
    dndArmourProficiencies = ["light armour"]
    skills = chooseFromList(4, ["Acrobatics", "Athletics", "Deception", "Insight", "Investigation", "Perception", "Performance", "Persuasion", "Slight of Hand", "Stealth"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["rapier", "shortsword"]), chooseFromList(1, ["shortbox, arrows x20", "shortsword"]), chooseFromList(1, ["burglar's pack", "dungeoneer's pack", "explorer's pack"]), "leather armour" , "daggers x2", "thieves' tools"]
    features = ["Expertise", "Sneak Attack", "Theives' Cant"]
    return profDict, equipment, features

def fiveEGenSorcerer():
    dndSavingThrows = ["CON", "CHA"]
    dndWeaponsProficiencies = ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
    dndArmourProficiencies = []
    skills = chooseFromList(2, ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["light crossbow, bolts x20", ""]), chooseFromList(1, ["component pouch", "arcane focus"]), chooseFromList(1, ["dungeoneer's pack", "explorer's pack"]), "dagger x2"]
    features = ["Spellcasting", "Sorcerous Origin: " + chooseFromList(1, ["Draconic Bloodline", "Wild Magic"])]
    return profDict, equipment, features

def fiveEGenWarlock():
    dndSavingThrows = ["WIS", "CHA"]
    dndWeaponsProficiencies = ["simple weapons"]
    dndArmourProficiencies = ["light armour"]
    skills = chooseFromList(2, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["light crossbow, bolts x20", ""]), chooseFromList(1, ["component pouch", "arcane focus"]), chooseFromList(1, ["dungeoneer's pack", "scholar's pack"]), "leather armour", chooseFromList(1, [""]), "dagger x2"]
    features = ["Pact Magic", "Otherwordly Patron: " + chooseFromList(1, ["the Archfey", "the Fiend", "the Great Old One"])]
    return profDict, equipment, features

def fiveEGenWizard():
    dndSavingThrows = ["INT", "WIS"]
    dndWeaponsProficiencies = ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
    dndArmourProficiencies = []
    skills = chooseFromList(2, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"])
    profDict = {"savingThrows": dndSavingThrows, "weaponProficiencies": dndWeaponsProficiencies, "armourProficiencies": dndArmourProficiencies, "skills": skills}
    equipment = [chooseFromList(1, ["quarterstaff", "dagger"]), chooseFromList(1, ["component pouch", "arcane focus"]), chooseFromList(1, ["scholar's pack", "explorer's pack"]), "spellbook"]
    features = ["Spellcasting", "Ritual casting", "Arcane Recovery"]
    return profDict, equipment, features
    
def chooseFromList(amount, listOfOptions):
    #provide an amount to choose from a list options, returns list of selections
    selections = []
    for pick in range(0, amount):
        number = rollToX(len(listOfOptions))
        selections.append(listOfOptions.pop(number - 1))
    if amount == 1:
        return selections[0]
    else:
        return selections

def genOseCharacter():
   characterFirstName = getname("firstnames.txt") 
   nameChance = rollDx(10)
   if nameChance == 1:
      characterLastName = "of " + getname("surnames.txt")
   elif nameChance == 2:
      characterLastName = getname("surnames.txt") + "-" + getname("surnames.txt")
   else:
      characterLastName = getname("surnames.txt")
   print(json.dumps({'name': {'firstName': characterFirstName, 'lastName':\
        characterLastName}}))
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
dndSavingThrows = []
dndToolsProficiencies = []
dndWeaponsProficiencies = []
dndArmourProficiencies = []
dndSkills = []
dndEquipment = []
dndClass = []
#######################################################################
#main
if __name__ == '__main__':
   if args.game_arg == "cyberpunk":
      genCharacter()
   elif args.game_arg == "five_e":
       gen5eCharacter()
   elif args.game_arg == "ose":
       genOseCharacter()
   else:
       parser.print_help()

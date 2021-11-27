#!/usr/bin/python3
#python utility to generate warbands for the Frostgrave game
#Author: Max Russell

#imports
import random
import sys
from optparse import OptionParser

#parsing
parser = OptionParser()
parser.add_option("-f", "--frostgrave", action="store_true", \
	dest="frostgrave", help="generate Frostgrave warband")
parser.add_option("-a", "--apprentice", action="store_true", \
	dest="apprentice", default=False, \
	help="have an apprentice in warband")
(options, args) = parser.parse_args()

#functions
def rollDx(x):
#returns a number between one and x
	rollresult = random.randint(1,x)
	return rollresult

def rollToX(x):
#returns a number between 0 and x
	rollresult = random.randint(0,x)
	return rollresult

def ReturnSpell(x, spellschool):
#returns a spell from a school given a number
	spell = spellschool[rollToX(x)]
	return spell

def GetSpells(array, num):
#gets spells from an array given the name and length
	availableSpells = array.copy()
	for i in range(0, num):
		newSpell = ReturnSpell((len(availableSpells)-1), \
		availableSpells)
		if newSpell in spellList:
			availableSpells.remove(newSpell)
			newSpell = ReturnSpell((len(availableSpells)-1), \
			availableSpells)
		else:
			availableSpells.remove(newSpell)
		spellList.append(newSpell)
	return spellList

def GetAllSpells(spells, relations):
#get all of the spells, using other functions
	GetSpells(spells, 3)
	GetSpells(relations[0], 1)
	GetSpells(relations[1], 1)
	GetSpells(relations[2], 1)
	availableRelations = relations.copy()
	enemyRelation = availableRelations.pop(-1)
	del availableRelations[0:2]
	firstRelation = availableRelations[random.randint(0,4)]
	availableRelations.remove(firstRelation)
	secondRelation = availableRelations[random.randint(0,3)]
	GetSpells(firstRelation, 1)
	GetSpells(secondRelation, 1)
	
	return spellList

def GetSoldiers():
#returns a list with the soldiers and an int for gold
	global soldierList
	soldierList = []
	global currentGold
	currentGold = startingGold
	availableSoldiers = arraySoldierType.copy()
	if options.apprentice == True:
		availableSoldiers.remove("Apprentice")
		soldierList.append("Apprentice")
		currentGold = currentGold - dictSoldierCost["Apprentice"]
		count = 1
	else:
		count = 0
	#roll for solider, removing all soliders that are too expensive
	#money. get money based on dictionary prices
	while currentGold > 19:

		newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
	
		#the following works, but more verbose than I think needed.
		#maybe something with for loops over the dictionary amount
		#based on remaining currentGold?
		if currentGold < 20:
			continue
		if currentGold <= 50 and newSoldier == "Infantryman":
			availableSoldiers.remove("Infantryman")
			availableSoldiers.remove("Crossbowman")
			availableSoldiers.remove("Archer")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 50 and newSoldier == "Crossbowman":
			availableSoldiers.remove("Crossbowman")
			availableSoldiers.remove("Infantryman")
			availableSoldiers.remove("Archer")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 50 and newSoldier == "Archer":
			availableSoldiers.remove("Archer")
			availableSoldiers.remove("Crossbowman")
			availableSoldiers.remove("Infantryman")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 80 and newSoldier == "Treasure Hunter":
			availableSoldiers.remove("Treasure Hunter")
			availableSoldiers.remove("Man-at-Arms")
			availableSoldiers.remove("Tracker")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 80 and newSoldier == "Man-at-Arms":
			availableSoldiers.remove("Man-at-Arms")
			availableSoldiers.remove("Treasure Hunter")
			availableSoldiers.remove("Tracker")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 80 and newSoldier == "Tracker":
			availableSoldiers.remove("Tracker")
			availableSoldiers.remove("Treasure Hunter")
			availableSoldiers.remove("Man-at-Arms")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 100 and newSoldier == "Marksman":
			availableSoldiers.remove("Marksman")
			availableSoldiers.remove("Apothecary")
			availableSoldiers.remove("Barbarian")
			availableSoldiers.remove("Ranger")
			availableSoldiers.remove("Templar")
			availableSoldiers.remove("Knight")
		elif currentGold <= 100 and newSoldier == "Apothecary":
			availableSoldiers.remove("Marksman")
			availableSoldiers.remove("Apothecary")
			availableSoldiers.remove("Barbarian")
			availableSoldiers.remove("Ranger")
			availableSoldiers.remove("Templar")
			availableSoldiers.remove("Knight")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 100 and newSoldier == "Barbarian":
			availableSoldiers.remove("Marksman")
			availableSoldiers.remove("Apothecary")
			availableSoldiers.remove("Barbarian")
			availableSoldiers.remove("Ranger")
			availableSoldiers.remove("Templar")
			availableSoldiers.remove("Knight")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 100 and newSoldier == "Ranger":
			availableSoldiers.remove("Marksman")
			availableSoldiers.remove("Apothecary")
			availableSoldiers.remove("Barbarian")
			availableSoldiers.remove("Ranger")
			availableSoldiers.remove("Templar")
			availableSoldiers.remove("Knight")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 100 and newSoldier == "Templar":
			availableSoldiers.remove("Marksman")
			availableSoldiers.remove("Apothecary")
			availableSoldiers.remove("Barbarian")
			availableSoldiers.remove("Ranger")
			availableSoldiers.remove("Templar")
			availableSoldiers.remove("Knight")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 100 and newSoldier == "Knight":
			availableSoldiers.remove("Marksman")
			availableSoldiers.remove("Apothecary")
			availableSoldiers.remove("Barbarian")
			availableSoldiers.remove("Ranger")
			availableSoldiers.remove("Templar")
			availableSoldiers.remove("Knight")
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		elif currentGold <= 200 and newSoldier == "Apprentice":
			availableSoldiers.remove('Apprentice')
			newSoldier = availableSoldiers[rollToX(len\
		(availableSoldiers) -1)]
		else:
			soldierList.append(newSoldier)
		if count >= len(soldierList):
			continue
		else:
			currentGold = currentGold - dictSoldierCost[soldierList\
			[count]]
		count = count + 1
	#refund if too poor
	if currentGold < 0:
		currentGold = currentGold + dictSoldierCost[soldierList[-1]]
		del soldierList[-1]		
	return soldierList
	return currentGold

def GetSoldiers2():
#second run, NOT used
	global soldierList
	soldierList = []
	global currentGold
	currentGold = startingGold
	availableSoldiers = arraySoldierType.copy()
	availableCosts = dictSoldierCost.copy()
	#roll for solider, removing all soliders that are too expensive
	#money. get money based on dictionary prices
	while currentGold > 19:

		newSoldier = soldierList.append(availableSoldiers[rollToX(len\
		(availableSoldiers) -1)])
		currentGold = currentGold - dictSoldierCost[soldierList[0]]
	
		#the following works, but more verbose than I think needed.
		#maybe something with for loops over the dictionary amount
		#based on remaining currentGold?
		if currentGold < 20:
			continue
		
		for value in availableCosts:
			if value > currentGold:
				del availableCosts[key]
		
		soldierList.append(availableSoldiers[rollToX(len\
		(availableSoldiers)-1)])
	return soldierList
	return currentGold
	
def FileLen(fname):
#open file, count the lines, return
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
	
def GetName(filename):
#function to make repeatable for first/last
        numoflines = FileLen(filename)
        randomnum = random.randint(0,numoflines)

        #open the file, read it, print only the generated line number
        file = open(filename)
        all_lines = file.readlines()
        return str(all_lines[randomnum].strip())

def GenWarband():
#generates the warband; main script here
	global startingGold
	startingGold = 500
	global spellList
	spellList = [ ]
	
	playerClass = arrayWizardType[rollToX(9)]
	
	if playerClass == "Chronomancer":
		spellArray = arrayChronomancerSpells
		relationsArray = arrayChronomancerRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Elementalist":
		spellArray = arrayElementalistSpells
		relationsArray = arrayElementalistRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Enchanter":
		spellArray = arrayEnchanterSpells
		relationsArray = arrayEnchanterRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Illusionist":
		spellArray = arrayIllusionistSpells
		relationsArray = arrayIllusionistRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Necromancer":
		spellArray = arrayNecromancerSpells
		relationsArray = arrayNecromancerRelations
		GetAllSpells(spellArray, relationsArray)	
	elif playerClass == "Sigilist":
		spellArray = arraySigilistSpells
		relationsArray = arraySigilistRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Soothsayer":
		spellArray = arraySoothsayerSpells
		relationsArray = arraySoothsayerRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Summoner":
		spellArray = arraySummonerSpells
		relationsArray = arraySummonerRelations
		GetAllSpells(spellArray, relationsArray)
	elif playerClass == "Thaumaturge":
		spellArray = arrayThaumaturgeSpells
		relationsArray = arrayThaumaturgeRelations
		GetAllSpells(spellArray, relationsArray)	
	elif playerClass == "Witch":
		spellArray = arrayWitchSpells
		relationsArray = arrayWitchRelations
		GetAllSpells(spellArray, relationsArray)
	else:
		print("wtf class do you have?")
	
	
	playerName = GetName("firstnames.txt") + " " + \
	GetName("surnames.txt")
	print("Name is: " + playerName)
	
	availableSpells = spellArray
	print("Class: " + playerClass)
	print("Spells are: " + str(spellList))
	GetSoldiers()
	print("Soldiers are: " + str(soldierList))
	print("Remaining Gold is: " + str(currentGold))

#declare data structs
arrayWizardType = ["Chronomancer", "Elementalist", "Enchanter", \
"Illusionist", "Necromancer", "Sigilist", "Soothsayer", "Summoner",\
"Thaumaturge","Witch"]
arraySoldierType = ["War Hound", "Thug", "Archer","Crossbowman",\
"Infantryman", "Tracker", "Man-at-Arms", "Treasure Hunter", "Knight",\
"Templar", "Ranger", "Barbarian", "Apothecary", "Marksman",\
"Apprentice"]
dictSoldierCost = {"War Hound": 20, "Thug": 20, "Archer": 50,\
"Crossbowman": 50, "Infantryman": 50, "Tracker": 80, "Man-at-Arms": 80,\
"Treasure Hunter": 80, "Knight": 100, "Templar": 100, "Ranger": 100,\
"Barbarian": 100, "Apothecary": 100, "Marksman": 100, "Apprentice": 200}
arrayChronomancerSpells = ["Crumble", "Decay", "Fast Act", \
"Fleet Feet", "Petrify", "Slow", "Timestore", "Time Walk"]
arrayElementalistSpells = ["Call Storm", "Destructive Sphere",\
"Elemental Ball", "Elemental Bolt", "Elemental Hammer",\
"Elemental Shield", "Scatter Shot", "Wall"]
arrayEnchanterSpells = ["Animate Construct", "Control Construct",\
"Embed Enchantment", "Enchant Armour", "Enchant Weapon", "Grenade",\
"Strength", "Telekinesis"]
arrayIllusionistSpells = ["Beauty", "Fool's Gold", "Glow", \
"Illusionary Solider", "Invisibility", "Monstrous Form", "Teleport",\
"Transpose"]
arrayNecromancerSpells = ["Bone Dart", "Bones of the Earth",\
"Control Undead", "Raise Zombie", "Reveal Death", "Spell Eater",\
"Steal Health", "Strike Dead"]
arraySigilistSpells = ["Absorb Knowledge", "Create Grimoire",\
"Draining Word", "Explosive Rune", "Furious Quill", "Power Word",\
"Push", "Write Scroll"]
arraySoothsayerSpells = ["Awareness", "Combat Awareness",\
"Forget Spell", "Mind Control", "Reveal Invisible", "Reveal Secret",\
"Will Power", "Wizard Eye"]
arraySummonerSpells = ["Bind Demon", "Imp", "Leap",\
"Plague of Insects", "Planar Tear", "Planar Walk","Possess",\
"Summon Demon"]
arrayThaumaturgeSpells = ["Banish", "Blinding Light",\
"Circle of Protection", "Dispel", "Heal", "Miraculus Cure",\
"Restore Life", "Shield"]
arrayWitchSpells = ["Animal Companion", "Brew Potion",\
"Control Animal", "Curse", "Familiar", "Fog", "Mud", "Posion Dart"]
arrayChronomancerRelations = [arrayNecromancerSpells, \
arraySoothsayerSpells, arrayElementalistSpells, arrayThaumaturgeSpells,\
arraySummonerSpells, arrayIllusionistSpells, arrayWitchSpells,\
arraySigilistSpells, arrayEnchanterSpells]
arrayElementalistRelations = [arraySummonerSpells,\
arrayEnchanterSpells, arrayChronomancerSpells, arrayThaumaturgeSpells,\
arraySoothsayerSpells, arraySigilistSpells, arrayWitchSpells, \
arrayNecromancerSpells, arrayIllusionistSpells]
arrayEnchanterRelations = [arrayWitchSpells, arraySigilistSpells,\
arrayElementalistSpells, arrayNecromancerSpells,\
arrayIllusionistSpells, arraySummonerSpells, arraySoothsayerSpells,\
arrayThaumaturgeSpells, arrayChronomancerSpells]
arrayIllusionistRelations = [arraySoothsayerSpells,\
arraySigilistSpells, arrayThaumaturgeSpells, arrayNecromancerSpells,\
arrayWitchSpells, arrayChronomancerSpells, arraySummonerSpells,\
arrayEnchanterSpells, arrayElementalistSpells]
arrayNecromancerRelations = [arrayWitchSpells, arrayChronomancerSpells,\
arraySummonerSpells, arrayElementalistSpells, arraySigilistSpells,\
arrayIllusionistSpells, arrayEnchanterSpells, arraySoothsayerSpells,\
arrayThaumaturgeSpells]
arraySigilistRelations = [arrayThaumaturgeSpells,\
arrayIllusionistSpells, arrayEnchanterSpells, arrayNecromancerSpells,\
arrayElementalistSpells, arrayWitchSpells, arrayChronomancerSpells,\
arraySoothsayerSpells, arraySummonerSpells]
arraySoothsayerRelations = [arrayThaumaturgeSpells,\
arrayChronomancerSpells, arrayIllusionistSpells, arrayEnchanterSpells,\
arraySummonerSpells, arrayNecromancerSpells, arrayElementalistSpells,\
arraySigilistSpells, arrayWitchSpells]
arraySummonerRelations = [arrayNecromancerSpells, arrayWitchSpells,\
arrayElementalistSpells, arraySoothsayerSpells,arrayEnchanterSpells,\
arrayIllusionistSpells, arrayChronomancerSpells,\
arrayThaumaturgeSpells, arraySigilistSpells]
arrayThaumaturgeRelations = [arraySoothsayerSpells,\
arraySigilistSpells, arrayIllusionistSpells, arrayElementalistSpells,\
arrayWitchSpells, arrayChronomancerSpells, arraySummonerSpells,\
arrayEnchanterSpells, arrayNecromancerSpells]
arrayWitchRelations = [arrayEnchanterSpells, arrayNecromancerSpells,\
arraySummonerSpells, arrayThaumaturgeSpells, arrayIllusionistSpells,\
arrayElementalistSpells, arraySigilistSpells, arrayChronomancerSpells,\
arraySoothsayerSpells]


#script proper starts

if options.frostgrave == True:
	GenWarband()
else:
	parser.print_help()

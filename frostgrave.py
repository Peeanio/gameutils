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

#declare data structs
class WizardType():
	def __init__(self, spell1, spell2, spell3, spell4, spell5, spell6,\
	spell7, spell8, allied1, allied2, allied3, neutral1, neutral2,\
	neutral3, neutral4, neutral5, opposed):
		self.spell1 = spell1
		self.spell2 = spell2
		self.spell3 = spell3
		self.spell4 = spell4
		self.spell5 = spell5
		self.spell6 = spell6
		self.spell7 = spell7
		self.spell8 = spell8
		self.allied1 = allied1
		self.allied2 = allied2
		self.allied3 = allied3
		self.neutral1 = neutral1
		self.neutral2 = neutral2
		self.neutral3 = neutral3
		self.neutral4 = neutral4
		self.neutral5 = neutral5
		self.opposed = opposed
		
class PlayerWizard():
	def __init__(self):
		self.school = arrayWizardType[rollToX(9)]
		self.spell1 = self.school
		self.spell2 = spell2
		self.spell3 = spell3
		self.spell4 = spell4
		self.spell5 = spell5
		self.spell6 = spell6
		self.spell7 = spell7
		self.spell8 = spell8

arrayWizardType = ["Chronomancer", "Elementalist", "Enchanter", \
"Illusionist", "Necromancer", "Sigilist", "Soothsayer", "Summoner",\
"Thaumaturge","Witch"]
arraySoldierType = ["War Hound", "Thug", "Archer","Crossbowman",\
"Infantryman", "Tracker", "Man-at-Arms", "Treasure Hunter", "Knight",\
"Templar", "Ranger", "Barbarian", "Apothecary", "Marksman",\
"Apprentice"]
dictSoliderCost = {"War Hound": 20, "Thug": 20, "Archer": 50,\
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
arrayChronomancerRelations = [arrayNecromancerSpells, arraySoothsayerSpells,\
arrayElementalistSpells, arrayThaumaturgeSpells,	arraySummonerSpells, arrayIllusionistSpells, arrayWitchSpells,\
arraySigilistSpells, arrayEnchanterSpells]
arrayElementalistRelations = [arraySummonerSpells,	arrayEnchanterSpells,\
arrayChronomancerSpells, arrayThaumaturgeSpells, arraySoothsayerSpells, arraySigilistSpells, arrayWitchSpells, \
arrayNecromancerSpells, arrayIllusionistSpells]
arrayEnchanterRelations = [arrayWitchSpells, arraySigilistSpells, arrayElementalistSpells,\
arrayNecromancerSpells, arrayIllusionistSpells, arraySummonerSpells, arraySoothsayerSpells, arrayThaumaturgeSpells, \
arrayChronomancerSpells]
arrayIllusionistRelations = [arraySoothsayerSpells, arraySigilistSpells, arrayThaumaturgeSpells,\
arrayNecromancerSpells, arrayWitchSpells, arrayChronomancerSpells, arraySummonerSpells, arrayEnchanterSpells,\
arrayElementalistSpells]
arrayNecromancerRelations = [arrayWitchSpells, arrayChronomancerSpells, arraySummonerSpells,\
arrayElementalistSpells, arraySigilistSpells, arrayIllusionistSpells, arrayEnchanterSpells, arraySoothsayerSpells,\
arrayThaumaturgeSpells]
arraySigilistRelations = [arrayThaumaturgeSpells, arrayIllusionistSpells, arrayEnchanterSpells,\
arrayNecromancerSpells, arrayElementalistSpells, arrayWitchSpells, arrayChronomancerSpells,arraySoothsayerSpells,\
arraySummonerSpells]
arraySoothsayerRelations = [arrayThaumaturgeSpells, arrayChronomancerSpells,\
arrayIllusionistSpells, arrayEnchanterSpells, arraySummonerSpells, arrayNecromancerSpells, arrayElementalistSpells,\
arraySigilistSpells, arrayWitchSpells]
arraySummonerRelations = [arrayNecromancerSpells, arrayWitchSpells, arrayElementalistSpells,\
arraySoothsayerSpells,arrayEnchanterSpells, arrayIllusionistSpells, arrayChronomancerSpells, arrayThaumaturgeSpells,\
arraySigilistSpells]
arrayThaumaturgeRelations = [arraySoothsayerSpells, arraySigilistSpells, arrayIllusionistSpells,\
arrayElementalistSpells, arrayWitchSpells, arrayChronomancerSpells, arraySummonerSpells, arrayEnchanterSpells,\
arrayNecromancerSpells]
arrayWitchRelations = [arrayEnchanterSpells, arrayNecromancerSpells, arraySummonerSpells,\
arrayThaumaturgeSpells, arrayIllusionistSpells, arrayElementalistSpells, arraySigilistSpells,\
arrayChronomancerSpells, arraySoothsayerSpells]

startingGold = 500
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

	
ReturnSpell(7, arrayWitchSpells)

availableSpells = spellArray

print(spellList)

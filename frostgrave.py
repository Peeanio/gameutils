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
arrayChronomancerRelations = ["Necromancer", "Soothsayer",\
"Elementalist", "Thaumaturge",	"Summoner", "Illusionist", "Witch",\
"Sigilist", "Enchanter"]
arrayElementalistSpells = ["Call Storm", "Destructive Sphere",\
"Elemental Ball", "Elemental Bolt", "Elemental Hammer",\
"Elemental Shield", "Scatter Shot", "Wall"]
arrayElementalistRelations = ["Summoner",	"Enchanter",\
"Chronomancer", "Thaumaturge", "Soothsayer", "Sigilist", "Witch", \
"Necromancer", "Illusionist"]
arrayEnchanterSpells = ["Animate Construct", "Control Construct",\
"Embed Enchantment", "Enchant Armour", "Enchant Weapon", "Grenade",\
"Strength", "Telekinesis"]
arrayEnchanterRelations = ["Witch", "Sigilist", "Elementalist",\
"Necromancer", "Illusionist", "Summoner", "Soothsayer", "Thaumaturge", \
"Chronomancer"]
arrayIllusionistSpells = ["Beauty", "Fool's Gold", "Glow", \
"Illusionary Solider", "Invisibility", "Monstrous Form", "Teleport",\
"Transpose"]
arrayIllusionistRelations = ["Soothsayer", "Sigilist", "Thaumaturge",\
"Necromancer", "Witch", "Chronomancer", "Summoner", "Enchanter",\
"Elementalist"]
arrayNecromancerSpells = ["Bone Dart", "Bones of the Earth",\
"Control Undead", "Raise Zombie", "Reveal Death", "Spell Eater",\
"Steal Health", "Strike Dead"]
arrayNecromancerRelations = ["Witch", "Chronomancer", "Summoner",\
"Elementalist", "Sigilist", "Illusionist", "Enchanter", "Soothsayer",\
"Thaumaturge"]
arraySigilistSpells = ["Absorb Knowledge", "Create Grimoire",\
"Draining Word", "Explosive Rune", "Furious Quill", "Power Word",\
"Push", "Write Scroll"]
arraySigilistRelations = ["Thaumaturge", "Illusionist", "Enchanter",\
"Necromancer", "Elementalist", "Witch", "Chronomancer","Soothsayer",\
"Summoner"]
arraySoothsayerSpells = ["Awareness", "Combat Awareness",\
"Forget Spell", "Mind Control", "Reveal Invisible", "Reveal Secret",\
"Will Power", "Wizard Eye"]
arraySoothsayerRelations = ["Thaumaturge", "Chronomancer",\
"Illusionist", "Enchanter", "Summoner", "Necromancer", "Elementalist",\
"Sigilist", "Witch"]
arraySummonerSpells = ["Bind Demon", "Imp", "Leap",\
"Plague of Insects", "Planar Tear", "Planar Walk","Possess",\
"Summon Demon"]
arraySummonerRelations = ["Necromancer", "Witch", "Elementalist",\
"Soothsayer","Enchanter", "Illusionist", "Chronomancer", "Thaumaturge",\
"Sigilist"]
arrayThaumaturgeSpells = ["Banish", "Blinding Light",\
"Circle of Protection", "Dispel", "Heal", "Miraculus Cure",\
"Restore Life", "Shield"]
arrayThaumaturgeRelations = ["Soothsayer", "Sigilist", "Illusionist",\
"Elementalist", "Witch", "Chronomancer", "Summoner", "Enchanter",\
"Necromancer"]
arrayWitchSpells = ["Animal Companion", "Brew Potion",\
"Control Animal", "Curse", "Familiar", "Fog", "Mud", "Posion Dart"]
arrayWitchRelations = ["Enchanter", "Necromancer", "Summoner",\
"Thaumaturge", "Illusionist", "Elementalist", "Sigilist",\
"Chronomancer", "Soothsayer"]
startingGold = 500
spellList = [ ]
	
playerClass = arrayWizardType[rollToX(9)]
	
if playerClass == "Chronomancer":
	spellArray = "arrayChronomancerSpells"
	relationsArray = "arrayChronomancerRelations"
	GetSpells(arrayChronomancerSpells, 3)
	GetSpells(arrayNecromancerSpells, 1)
	GetSpells(arraySoothsayerSpells, 1)
	GetSpells(arrayElementalistSpells, 1)
elif playerClass == "Elementalist":
	spellArray = "arrayElementalistSpells"
	relationsArray = "arrayElementalistRelations"
	GetSpells(arrayElementalistSpells, 3)
	GetSpells(arraySummonerSpells, 1)
	GetSpells(arrayEnchanterSpells, 1)
	GetSpells(arrayChronomancerSpells, 1)
elif playerClass == "Enchanter":
	spellArray = "arrayEnchanterSpells"
	relationsArray = "arrayEnchanterRelations"
	GetSpells(arrayEnchanterSpells, 3)
	GetSpells(arrayWitchSpells, 1)
	GetSpells(arraySigilistSpells, 1)
	GetSpells(arrayElementalistSpells, 1)
elif playerClass == "Illusionist":
	spellArray = "arrayIllusionistSpells"
	relationsArray = "arrayIllusionistRelations"
	GetSpells(arrayIllusionistSpells, 3)
	GetSpells(arraySoothsayerSpells, 1)
	GetSpells(arraySigilistSpells, 1)
	GetSpells(arrayThaumaturgeSpells, 1)	
elif playerClass == "Necromancer":
	spellArray = "arrayNecromancerSpells"
	relationsArray = "arrayNecromancerRelations"
	GetSpells(arrayNecromancerSpells, 3)
	GetSpells(arrayWitchSpells, 1)
	GetSpells(arrayChronomancerSpells, 1)
	GetSpells(arraySummonerSpells, 1)	
elif playerClass == "Sigilist":
	spellArray = "arraySigilistSpells"
	relationsArray = "arraySigilistRelations"
	GetSpells(arraySigilistSpells, 3)
	GetSpells(arrayThaumaturgeSpells, 1)
	GetSpells(arrayIllusionistSpells, 1)
	GetSpells(arrayEnchanterSpells, 1)	
elif playerClass == "Soothsayer":
	spellArray = "arraySoothsayerSpells"
	relationsArray = "arraySoothsayerRelations"
	GetSpells(arraySoothsayerSpells, 3)
	GetSpells(arrayThaumaturgeSpells, 1)
	GetSpells(arrayIllusionistSpells, 1)
	GetSpells(arrayEnchanterSpells, 1)	
elif playerClass == "Summoner":
	spellArray = "arraySummonerSpells"
	relationsArray = "arraySummonerRelations"
	GetSpells(arraySummonerSpells, 3)
	GetSpells(arrayNecromancerSpells, 1)
	GetSpells(arrayWitchSpells, 1)
	GetSpells(arrayElementalistSpells, 1)	
elif playerClass == "Thaumaturge":
	spellArray = "arrayThaumaturgeSpells"
	relationsArray = "arrayThaumaturgeRelations"
	GetSpells(arrayThaumaturgeSpells, 3)
	GetSpells(arraySoothsayerSpells, 1)
	GetSpells(arraySigilistSpells, 1)
	GetSpells(arrayIllusionistSpells, 1)	
elif playerClass == "Witch":
	spellArray = "arrayWitchSpells"
	relationsArray = "arrayWitchRelations"
	GetSpells(arrayWitchSpells, 3)
	GetSpells(arrayEnchanterSpells, 1)
	GetSpells(arrayNecromancerSpells, 1)
	GetSpells(arraySummonerSpells, 1)
else:
	print("wtf class do you have?")

	
ReturnSpell(7, arrayWitchSpells)

availableSpells = spellArray

print(spellList)

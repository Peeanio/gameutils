#!/usr/bin/python3
#python version of chargens script
#Author: Max Russell

import random
#libary for random number generation
import sys
#file opening
from optparse import OptionParser
#for option parsing

########################################################################
# option parsing setup

parser = OptionParser()
parser.add_option("-c", "--2020", action="store_true", dest="cyberpunk",\
	help="generate Cyberpunk 2020V2 character")
(options, args) = parser.parse_args()

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

########################################################################
#declare arrays
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
#main
if options.cyberpunk == True:
	genCharacter()

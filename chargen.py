#!/usr/bin/python3
#python version of chargens script

import random
#libary for random number generation

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
	for x in range(3):
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
	for x in range(0,len(statsValues)):
		statsValues[x] = rollStat(statsLongNames[x])
	rollBackstory()
	rollCyberWare()
	rollWeapons()

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
genCharacter()

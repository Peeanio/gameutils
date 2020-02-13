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
#	print (rollDx)

def rollStat(stat):
#creates a text output of a score for a stat
	statScore = (rollDx(10))
	while statScore == 1:
			statScore = (rollDx(10))
	print(stat + " is: " + str(statScore))
	
def rollBackstory():
#generates the player class and some fluff to make more interesting
	global playerClass #this makes it available outside the functions
	playerClass = arrayClasses[rollDx(9)]
	playerClothes = arrayClothes[rollDx(9)]
	playerEthnicity = arrayEthnicity[rollDx(9)]
	playerParents = arrayParents[rollDx(9)]		
	print("Class is: " + str(playerClass))
	print("Clothes are: " + str(playerClothes))
	print("Ethnicity is: " + str(playerEthnicity))
	print("Parents are/were: " + str(playerParents))
	
def rollCyberWare():
#rolls for cybernetics for character
	rolledCyberware = [0 for x in range(5)]
	if str(playerClass) == str("Solo"):
		#diceCyberWare = [ 0 for x in range(5) ]
		for x in range(5):
			rolledCyberware[x] = rollDx(10)
			Print("Cyberware is: " + str(rolledCyberware[x]))
		
	else:
		#diceCyberWare = [ 0 for x in range(2) ]
		for x in range(2):
			rolledCyberware[x] = rollDx(10)
			print("Cyberware is: " + str(rolledCyberware[x]))
	playerCyberWareRolls = rolledCyberware
	print(str(rolledCyberware))
	#need to break this part up into individual rolls, and append to character
def genCharacter():
	for x in range(0,len(statsValues)):
		statsValues[x] = rollStat(statsLongNames[x])
	rollBackstory()
	rollCyberWare()
	
	
	
	
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
arrayCyberWare=["Cyberoptics", "Cyberarm with gun", "Cyberaudio",\
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
 "Heavy Armor Jacket", "Heavy Armor Jacket", "Metalgear"]
arrayWeapons=["Knife", "Light pistol", "Med pistol", "Heavy Pistol"\
 "Heavy Pistol", "Light SMG", "Lt. Assault Rifle", "Med Assault Rifle",\
  "Hvy. Assault rifle", "Heavy Assault Rifle"]

########################################################################
#main
genCharacter()


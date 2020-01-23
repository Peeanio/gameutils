#!/usr/bin/python3
#python version of chargens script

import random
#libary for random number generation

def rollDx(x):
#returns a number between one and x
	rollresult = random.randint(1,x)
	return rollresult
#	print (rollDx)

def rollStat(stat):
#creates a text output of a score for a stat
	statscore = (rollDx(6) + rollDx(6))
	print(stat + " is: " + str((rollDx(6) + rollDx(6))))
	
def rollBackstory():
	playerClass = arrayClasses[rollDx(9)]
	playerClothes = arrayClothes[rollDx(9)]
	playerEthnicity = arrayEthnicity[rollDx(9)]
	playerParents = arrayParents[rollDx(9)]		
	print("Class is: " + str(playerClass))
	print("Clothes are: " + str(playerClothes))
	print("Ethnicity is: " + str(playerEthnicity))
	print("Parents are/were: " + str(playerParents))	

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

#main 
for x in range(0,len(statsValues)):
	statsValues[x] = rollStat(statsLongNames[x])
rollBackstory()

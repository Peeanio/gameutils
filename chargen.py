#!/usr/bin/python3
#python version of chargens script

import random
#libary for random number generation

def rollD6():
#returns a number between one and six
	rollresult = random.randint(1,6)
	return rollresult
#	print (rollD6)

def rollStat(stat):
#creates a text output of a score for a stat
	statscore = (rollD6() + rollD6())
	print(stat + " is: " + str((rollD6() + rollD6())))
	

rollStat("Int")

#!/usr/bin/python

# a dice rolling utility to speed up the process of rolling dice
# designed to be expandable and simple, while following
# standard unix philosophy

# Author: Max Russell
# max@theguards.net

import random

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", type="int", dest="numOfDice", help="number of dice to be rolled")
parser.add_option("-s", type="int", dest="sizeOfDice", help="number of sides dice have, default six")
(options, args) = parser.parse_args()

def rollDice(y):
    resultList = [];
    for x in range(y):
        resultList.append( random.randint(1,6) )
    for x in range(1, sizeOfDice):
        print("Number of " + str(x) + "s: " + str(resultList.count(x)) )

if options.sizeOfDice is None:
    sizeOfDice = 7
else:
    sizeOfDice = options.sizeOfDice + 1

if options.numOfDice is None:
    print ("Please enter the number of dice to roll:")
    rollDice(int(input()))

else: 
    rollDice(int(options.numOfDice))

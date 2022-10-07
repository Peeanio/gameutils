#!/usr/bin/python

# a dice rolling utility to speed up the process of rolling dice
# designed to be expandable and simple, while following
# standard unix philosophy

# Author: Max Russell
# max@theguards.net

import random
import json
import argparse

parser = argparse.ArgumentParser(prog='roll.py', description='multipurpose dice rolling utility')
subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='dice rolling helper style', dest='rollArg')
parser_traditional = subparsers.add_parser('traditional', help='traditional, generic')
parser_traditional.add_argument("-d", dest="numOfDice", help="number of dice to be rolled")
parser_traditional.add_argument("-s", dest="sizeOfDice", help="number of sides dice have, default six")
parser_traditional.add_argument("-a", dest="aboveInt", help="only return results above this value")
parser_fiveE = subparsers.add_parser('fivee', help='roll 5e d20 dice check')
parser_fiveE.add_argument("-a", "--advantage", action="store_true", dest="booleanAdvantage", default=False, help="roll with advantage (roll twice pick higher")
parser_fiveE.add_argument("-d", "--disadvantage", action="store_true", dest="booleanDisadvantage", default=False, help="roll with disadvantage (roll twice pick lower)")
parser_fiveE.add_argument("-m", "--modifer", dest="rollModifier", default=0, help="define a static numerical modifier for the roll)")
parser_fiveE.add_argument("-p", "--proficiency", action="store_true", dest="booleanProficiency", default=False, help="roll with Proficiency bonus (scales with level)")
parser_fiveE.add_argument("-e", "--expertise", action="store_true", dest="booleanExpertise", default=False, help="roll with expertise (scales with level)")
parser_fiveE.add_argument("-l", "--level", dest="rollLevel", default=1, help="scales the level (defaults to 1)")
parser_fiveE.add_argument("-v", "--verbose", action="store_true", dest="booleanVerbose", default=False, help="returns JSON formatted info on the rolling operation")
args = parser.parse_args()

def rollDice(y):
    resultList = [];
    for x in range(y):
        resultList.append( random.randint(1,sizeOfDice) )
    for x in range(1, sizeOfDice):
        if resultList.count(x) != 0:
            if args.aboveInt is not None:
                if x >= args.aboveInt:
                    print("Number of " + str(x) + "s: " + str(resultList.count(x)) )
            else:
                print("Number of " + str(x) + "s: " + str(resultList.count(x)) )
def rollDx(x):
#returns a number between one and x
    rollresult = random.randint(1,x)
    return rollresult

def rollToX(x):
#returns a number between 0 and x
    rollresult = random.randint(0,x)
    return rollresult

if args.rollArg == 'traditional':
    if args.sizeOfDice is None:
        sizeOfDice = 7
    else:
        sizeOfDice = args.sizeOfDice + 1

    if args.numOfDice is None:
        print ("Please enter the number of dice to roll:")
        rollDice(int(input()))

    else: 
        rollDice(int(args.numOfDice))

elif args.rollArg == 'fivee':
    if (args.booleanAdvantage) != (args.booleanDisadvantage):
        firstRolledResult = rollDx(20)
        secondRolledResult = rollDx(20)
        listRolledResult = [firstRolledResult, secondRolledResult]
        listRolledResultSorted = sorted(listRolledResult)
        if args.booleanAdvantage == True:
            listRolledResultSorted.pop(0)
            finalResult = listRolledResultSorted[0]
        if args.booleanDisadvantage == True:
            listRolledResultSorted.pop(-1)
            finalResult = listRolledResultSorted[0]
    else:
        firstRolledResult = rollDx(20)
        secondRolledResult = None
        finalResult = firstRolledResult
    #proficency/expertise logic
    args.rollLevel = int(args.rollLevel)
    if args.rollLevel >= 1 and args.rollLevel <= 4:
        currentProficiencyModifier = 2
    elif args.rollLevel >= 5 and args.rollLevel <= 8:
        currentProficiencyModifier = 3
    elif args.rollLevel >= 9 and args.rollLevel <= 12:
        currentProficiencyModifier = 4
    elif args.rollLevel >= 13 and args.rollLevel <= 16:
        currentProficiencyModifier = 5
    elif args.rollLevel >= 17 and args.rollLevel <= 20:
        currentProficiencyModifier = 6
    else:
        print("level is outside of band, aborting")
    totalModifier = int(args.rollModifier)
    if (args.booleanProficiency):
        totalModifier = totalModifier + currentProficiencyModifier
    if (args.booleanExpertise):
        totalModifier = totalModifier + currentProficiencyModifier 
    if args.booleanVerbose == False:
        print(str(finalResult + totalModifier))
    else:
        print(json.dumps({'finalRoll': finalResult + totalModifier, 'rolledDie': finalResult, 'staticModifier': int(args.rollModifier), 'level': args.rollLevel, 'proficiency': args.booleanProficiency, 'expertise': args.booleanExpertise, 'advantage': args.booleanAdvantage, 'disadvantage': args.booleanDisadvantage, 'firstRolledResult': firstRolledResult, 'secondRolledResult': secondRolledResult}))

else:
    parser.print_help()

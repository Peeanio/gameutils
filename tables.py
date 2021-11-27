#!/usr/bin/python3

#Author: Max Russell

'''
Utility to get values from tables for various games
Program takes name of file from input, and returns a random entry from that file

File are formatted as the text to return as a single line on the file
'''

#imports
import random
import sys
import argparse

#parsing
parser = argparse.ArgumentParser()
parser.add_argument('table', nargs=1, help="print help")
args = parser.parse_args()

#functions
def FileLen(fname):
#open file, count the lines, return
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def GetLine(filename):
#function to make repeatable for any word type
        numoflines = FileLen(filename)
        randomnum = random.randint(0,numoflines)

        #open the file, read it, print only the generated line number
        file = open(filename)
        all_lines = file.readlines()
        return str(all_lines[randomnum].strip())

def GetEntry():
#returns a random value of a table file
    name = GetLine(args.table[0])
    return name

#script begins
try:
	args.table
except:
	parser.print_help()
else:
	print(GetEntry())

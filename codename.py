#!/usr/bin/python3

#Author: Max Russell
#script indended to give codenames for various purposes, 
#ie people or operations. users are expected to supply their own
#noun and adjective lists, for more control vs the defaults
#no thought will be given initally to aptronyms or backronyms

#imports
import random
import sys
from optparse import OptionParser

#parsing
parser = OptionParser()
parser.add_option("-o", "--operation", action="store_true", \
	dest="operation", help="generate operation name")
parser.add_option("-c", "--codename", action="store_true", \
	dest="codename", help="generate identity name")
parser.add_option("-n", "--nouns", metavar="NOUNFILE", \
	dest="NOUNFILE", default="nouns.txt", \
	help="set the path to list of nouns")
parser.add_option("-a", "--adjectives", metavar="ADJECTIVEFILE", \
	dest="ADJECTIVEFILE", default="adjectives.txt", \
	help="set the path to list of adjectives")
parser.add_option("-q", "--quiet", action="store_true", \
	dest="quiet", default=False, help="displays only the code name")
parser.add_option("-u", "--upper", action="store_true",\
	dest="upper", default=False, \
	help="codename will be shown in upper case instead of camel")
parser.add_option("--nospaces", action="store_true", dest="nospaces",\
	default=False, help="no spaces in the codename")
(options, args) = parser.parse_args()

def FileLen(fname):
#open file, count the lines, return
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def GetWord(filename):
#function to make repeatable for any word type
        numoflines = FileLen(filename)
        randomnum = random.randint(0,numoflines)

        #open the file, read it, print only the generated line number
        file = open(filename)
        all_lines = file.readlines()
        return str(all_lines[randomnum].strip())
        
def Operation():
#returns the operation name generated from adj + noun
	name = GetWord(options.ADJECTIVEFILE).capitalize() + " " + \
		GetWord(options.NOUNFILE).capitalize()
	return name

def CodeName():
#returns the name generated from file passed in
	name = GetWord(options.NOUNFILE).capitalize()
	return name
	
#script begins
if options.operation == True:
	result = Operation()
elif options.codename == True:
	result = CodeName()
else:
	parser.print_help()

#optional settings
if options.upper == True:
	result = result.upper()
if options.nospaces == True:
	result = result.replace(" ", "")
if options.quiet == False and options.operation == True:
	print("Operation: " + result)
elif options.quiet == False and options.codename == True:
	print("Codename: " + result)
else:
	print(result)

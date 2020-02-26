#!/usr/bin/python

#takes a file of names and picks one randomly

import random
import sys

listFile = open("cyberchargen.c") #open(sys.argv)
lines=listFile.readlines()
with listFile as f:
	for i, l in enumerate(f):
		pass
count = i+1
random = random.randint(1,count)

print (lines[random])

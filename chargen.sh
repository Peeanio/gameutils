#!/bin/sh

#character generator for pen and paper rpgs
#work in progress


Roll () {
#rolls a single die up to number passed to function	
	echo $((RANDOM%$1+1))
}

RollStat () {
#take argument name of stat
	STAT=$(($(Roll 6)+$(Roll 6)))
#not ready for 11+ reroll yet, likely because of string instead of int
#	if [ $STAT >= 11 ]; then
#		STAT=$(($(Roll 6)+$(Roll 6)))
#	fi
	echo $1 is: $STAT
	
##$(Roll 10)+$(Roll 10)
}
RollClass () {
#rolls for one of the classes in game
	CLASS=$(Roll 10)
	if [ $CLASS == 1 ]; then
		CLASSNAME="Rockerboy"
	elif [ $CLASS == 2 ]; then
		CLASSNAME="Solo"
	elif [ $CLASS == 3 ]; then
		CLASSNAME="Netrunner"
	elif [ $CLASS == 4 ]; then
		CLASSNAME="Techie"
	elif [ $CLASS == 5 ]; then
		CLASSNAME="Medtech"
	elif [ $CLASS == 6 ]; then
		CLASSNAME="Media"
	elif [ $CLASS == 7 ]; then
		CLASSNAME="Cop"
	elif [ $CLASS == 8 ]; then
		CLASSNAME="Corporate"
	elif [ $CLASS == 9 ]; then
		CLASSNAME="Fixer"
	elif [ $CLASS == 10 ]; then
		CLASSNAME="Nomad"
	else
		CLASSNAME="WTF"
	fi
	echo "Class is "$CLASSNAME
}

RollSkills () {
#each role has 10 skills that points are divided between. generates
#points per skill
#likely not working because of string vs int
	TOTALPOINTS=40
	SKILLPOINTS=(Roll 10)
	POINTSLEFT=(40-$(SKILLPOINTS))
	echo $POINTSLEFT

}

RollStat INT 
RollStat REF
RollStat CL
RollStat TECH
RollStat LK
RollStat ATT
RollStat MA
RollStat EMP
RollClass
RollSkills

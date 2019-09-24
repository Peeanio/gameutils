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



RollOneToTen () {
#allows for one function to do multiple generations
	$(( $1=$(Roll 10) ))
	if [ $1 == 1 ]; then
		RESULT=$2
	elif [ $1 == 2 ]; then
		RESULT=$3
	elif [ $1 == 3 ]; then
		RESULT=$4
	elif [ $1 == 4 ]; then
		RESULT=$5
	elif [ $1 == 5 ]; then
		RESULT=$6
	elif [ $1 == 6 ]; then
		RESULT=$7
	elif [ $1 == 7 ]; then
		RESULT=$8
	elif [ $1 == 8 ]; then
		RESULT=$9
	elif [ $1 == 9 ]; then
		RESULT=$10
	elif [ $1 == 10 ]; then
		RESULT=$11
	else
		RESULT="WTF"
	fi
	echo $1" is: "$RESULT
}

#RollSkills () {
#each role has 10 skills that points are divided between. generates
#points per skill
#likely not working because of string vs int

#progress. the variables were not being set, called or operated correctly
#still a work in progress
#	TOTALPOINTS=40
#	SKILLPOINTS=$(Roll 10)
#	echo $SKILLPOINTS
#works> 	echo `expr $TOTALPOINTS - $SKILLPOINTS`
#	ROLLNUMBER=0
#	for  ((i = 0 ; i < 10 ; i++)); do
#		i=$(Roll 6)
#	fi
	

#}

RollCosemetic () {
#cyberpunk looks, randomised from book
	CLOTHES=$(Roll 10)
	if [ $CLOTHES == 1 ]; then
		RESULT="Biker leathes"
	elif [ $CLOTHES == 2 ]; then
		RESULT="Blue jeans"
	elif [ $CLOTHES == 3 ]; then
		RESULT="Corporate Suits"
	elif [ $CLOTHES == 4 ]; then
		RESULT="Jumpsuits"
	elif [ $CLOTHES == 5 ]; then
		RESULT="Miniskirts"
	elif [ $CLOTHES == 6 ]; then
		RESULT="High fasion"
	elif [ $CLOTHES == 7 ]; then
		RESULT="Cammos"
	elif [ $CLOTHES == 8 ]; then
		RESULT="Normal clothes"
	elif [ $CLOTHES == 9 ]; then
		RESULT="Nude"
	elif [ $CLOTHES == 10 ]; then
		RESULT="Bag Lady Chic"
	else
		RESULT="WTF"
	fi
	echo "Clothes are "$RESULT
}

RollStat INT 
RollStat REF
RollStat CL
RollStat TECH
RollStat LK
RollStat ATT
RollStat MA
RollStat EMP
#RollClass
#RollSkills
RollOneToTen Class Solo Rocker Netrunner Media Nomad Fixer Cop Corp Techie\
	Medtechie
RollCosemetic

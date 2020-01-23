#!/bin/sh

#character generator for pen and paper rpgs
#work in progress
#By Peeanio, on github

Roll () {
#rolls a single die up to number passed to function
	echo $((RANDOM%$1+1))
#	echo $(( ($(date +%N)+1)%$1 ))

}

RollStat () {
#take argument name of stat
	local STAT=$(($(Roll 6)+$(Roll 6)))

	if [ "$STAT" = "11" ]; then
		STAT=10
	elif [ "$STAT" = "12" ]; then
		STAT=10
	fi
	echo $1 is: $STAT
	
##$(Roll 10)+$(Roll 10)
}
RollOneToTen () {
#allows for one function to do multiple 1-10 roll generations. WTF 
# result is error somewhere, likely number is not matched
	Rolled=$(Roll 10)
	if [ $Rolled = 1 ]; then
		RESULT=$2
	elif [ $Rolled = 2 ]; then
		RESULT=$3
	elif [ $Rolled = 3 ]; then
		RESULT=$4
	elif [ $Rolled = 4 ]; then
		RESULT=$5
	elif [ $Rolled = 5 ]; then
		RESULT=$6
	elif [ $Rolled = 6 ]; then
		RESULT=$7
	elif [ $Rolled = 7 ]; then
		RESULT=$8
	elif [ $Rolled = 8 ]; then
		RESULT=$9
	elif [ $Rolled = 9 ]; then
		RESULT=${10}
	elif [ $Rolled = 10 ]; then
		RESULT=${11}
	else
		RESULT="WTF"
	fi
	echo $1" : "$RESULT
}

#RollSkills () {
#each role has 10 skills that points are divided between. generates
#points per skill
#likely not working because of string vs int (not a thing in sh)
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

RollStat INT
RollStat REF
RollStat TECH
RollStat COOL
RollStat LUCK
RollStat ATT
RollStat MA
RollStat EMP
RollStat BODY
#RollSkills
RollOneToTen Class Solo Rocker Netrunner Media Nomad Fixer Cop Corp Techie\
	Medtechie
RollOneToTen Clothes "Biker Leathers" "Blue Jeans" "Corporate Suits" \
	"Jumpsuits" "Miniskirts" "High Fashion" "Cammos" "Normal Clothes" \
	"Nude" "Bag Lady Chic"
RollOneToTen Ethnicity "Anglo-American" "African" "Japanese/Korean" \
	"Central European/Soviet" "Pacific Islander" \
	"Chinese/Southeast Asian" "Black American" "Hispanic American" \
	"Central/South American" "European"
RollOneToTen Parents "Corporate Executive" "Corporate Manager" \
	"Corporate Technician" "Nomad Pack" "Pirate Fleet" \
	"Gang Family" "Crime Lord" "Combat Zone Poor" "Urban Homeless" \
	"Arcology Family"

#!/bin/sh

#character generator for pen and paper rpgs
#work in progress


Roll () {
#rolls a single die up to number passed to function	
	echo $((RANDOM%$1+1))
}

RollStat () {
#take argument name of stat
	STAT=$(Roll 6)
	echo $STAT
	STAT=$STAT+$(Roll 6))
	echo $1 is: $STAT

##$(Roll 10)+$(Roll 10)
}

RollStat INT 
RollStat REF
RollStat CL
RollStat TECH
RollStat LK
RollStat ATT
RollStat MA
RollStat EMP



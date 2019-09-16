//a character generator for cyberpunk 2020 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int rollDie()
{
//rolls a six sided die
	int die = rand() % (6 - 1 + 1) + 1;
//	printf("%d\n", die);
	return die;

}

int rollStat()
{
//rolls number of statDice, then totals it up
	int statDice = 2;
	int rollNum = 0;
	srand(time(NULL));
	long total = 0;
	for( rollNum = 0; rollNum < statDice; rollNum++){
//	rolls dice and adds them up
		int dieRoll = rollDie();
//		printf("die roll: %d/n", dieRoll);
		unsigned time = time;
		total += dieRoll; 
//		printf("total: %d\n", total);
		}
//	printf("final: %d\n", total);
	return total;
//	prints grand total 
}

int main() {
// rolls for stat	
	int statInt = rollStat();
	srand(time(NULL));
	int statRef = rollStat();
	int statTech = rollStat();
	int statCool = rollStat();
	int statAttr = rollStat();
	int statLuck = rollStat();
	int statMA = rollStat();
	int statBody = rollStat();
	int statEmp = rollStat();
	printf("Int is: %d\n", statInt);
	printf("Ref is: %d\n", statRef);
//issue that srand time seed does not change fast enough, once per second (epoch time) to 
// each roll unique. either wait 1 sec between rolls, or get a new seed every roll?
}

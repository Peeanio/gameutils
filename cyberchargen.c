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
//rolls for one stat
	int statDice = 2;
	int rollNum = 0;
	srand(time(0));
	int total = 0;
	for( rollNum = 0; rollNum < statDice; rollNum++){
	
		int dieRoll = rollDie();
		printf("die roll: %d\n", dieRoll);
		total += dieRoll; // issue was here. was redeclaring total
		printf("total: %d\n", total);

		}
	printf("final: %d\n", total);
}

int main() {
	

	int stat = rollStat();
	printf("stat is: %d\n", stat);
}

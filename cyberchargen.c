//a character generator for cyberpunk 2020 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int rollDie()
{
//	srand(time(0));
	int die = rand() % (6 - 1 + 1) + 1;
//	printf("%d\n", die);
	return die;

}

int main()
{
int statDice = 3;
int rollNum = 0;
srand(time(0));
int result = 0;
for( rollNum = 0; rollNum < statDice; rollNum++){
	
	int die = rollDie();
	printf("die roll: %d\n", die);
	int result = result + die; // issue here. not sure why it cycles back to 0?
	printf("result: %d\n", result);

	}
//printf("%d\n", result);
}

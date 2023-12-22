#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


/**
 * infinite_while - keeps the program running until it is killed by a signal
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: 0 (SUCCESS)
 *
 * Description:
 * Creates 5 zombie processes
 */
int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();

		if (child == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
	infinite_while();
	return (0);
}

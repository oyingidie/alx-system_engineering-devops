#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void create_new_zombie(pid_t pid);
int infinite_while(void);

/**
 * main - Initiates creation of zombie processes
 * Return: Always 0
 */
int main(void)
{
	pid_t pid = 0;

	for (i = 0; i < 5; i++)
	{
		create_new_zombie(pid);
	}

	infinite_while();
	return (0);
}

/**
 * create_new_zombie - Create a new zombie process
 * @pid: Process identification number
 */
void create_new_zombie(pid_t pid)
{
	pid = fork();
	if (pid == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * infinite_while - An infinite loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

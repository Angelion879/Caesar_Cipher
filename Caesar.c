#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

// variable declaration for all functions
int n, k, c, o;
char key[3], opt[0], message[100];
bool t, check;

/*still got problems with reading the message, it only encodes 1 word at a time*/

// functions declaration
bool numericcheck(char value[]);
void encrypt(char key[]);
void decrypt(char key[]);

// main function
int main (void)
{
	do
	{
	printf("What do you want to do? (Encript = 1; Decript = 2)\n");
	scanf("%s", opt);
	check = numericcheck(opt);
	}
	while (check != true);
	
	o = atoi(opt);
	
	if (o == 1)
	{
		do
		{
		printf("Ok! Now, please, insert your key (numbers only): ");
		scanf("%s", key);
		check = numericcheck(key);
		}
		while (check != true);
		encrypt(key);
	}
	else if (o == 2)
	{
		printf("Ok! Now, please, insert your key (numbers only): ");
		scanf("%s", key);
		decrypt(key);
	}
	else
	{
		printf("ERROR 403: FORBIDEN\n");
	}
	return 0;
}

bool numericcheck(char value[]) // this function tests if the input is or not a numeric character
{
	for (int i = 0, n = strlen(value); i < n; i++)
	{
		if ((int)(value[i]) < '0' || (int)(value[i]) > '9')
		{
			printf("Please insert an valid key\n");
			t = false;
		}
		else
		{
			t = true;
		}
	}
	return t;
}

void encrypt(char key[]) // this function encrypt a message
{
	printf("Clear message:\n");
	scanf("%s", message);
	n = strlen(message);
	k = atoi(key);

	printf("Cipher message:\n");
	for (int i = 0; i < n; i++)
	{
		if (((int)(message[i]) >= 'A' && (int)(message[i]) <= 'Z') || ((int)(message[i]) >= 'a' && (int)(message[i]) <= 'z')) // letters
		{
			while (k > 26)
			{
				k = abs(k - 26);
			}
			c = abs((int)(message[i]) + k);

			if ((int)(message[i]) >= 'A' && (int)(message[i]) <= 'Z') // upper case letters
			{
				while (c > 90)
				{
					c = abs(c - 26);
				}
				printf("%c", c);
			}
			else if ((int)(message[i]) >= 'a' && (int)(message[i]) <= 'z') // lower case letters
			{
				while(c > 148)
				{
					c = abs(c - 26);
				}
				printf("%c", c);
			}
		}
		else // not letters
		{
			printf("%c", message[i]);
		}
	}
	printf("\n");
}

void decrypt(char key[]) // this function decrypt a message
{
	printf("Cipher message:\n");
	scanf("%s", message);
	n = strlen(message);
	k = atoi(key);

	printf("Clear message:\n");
	for (int i = 0; i < n; i++)
	{
		if (((int)(message[i]) >= 'A' && (int)(message[i]) <= 'Z') || ((int)(message[i]) >= 'a' && (int)(message[i]) <= 'z'))
		{
			while (k > 26)
			{
				k = abs(k - 26);
			}
			c = abs((int)(message[i]) - k);

			if ((int)(message[i]) >= 'A' && (int)(message[i]) <= 'Z') // upper case letters
			{
				while (c < 65)
				{
					c = abs(c + 26);
				}
				printf("%c", c);
			}
			else if ((int)(message[i]) >= 'a' && (int)(message[i]) <= 'z') // lower case letters
			{
				while (c < 97)
				{
					c = abs(c + 26);
				}
				printf("%c", c);
			}
			else // not letters
			{
				printf("%c", c);
			}
		}
	}
	printf("\n");
}

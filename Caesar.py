import math
import string
import sys
import os

def opReader ():
	#This read what the user wants 2 do
	op = input('What do you want to do today?\nEncipher = 1\nDecipher = 2\n')
	if (op in string.ascii_letters or (1 > int(op) or int(op) > 2)):
		sys.stdout.write('Please insert an valid option\n')
		opReader()
	return op

def keyReader ():
	#this reads the key to encode or decode
	key = input('Please insert your numeric secret key: ')
	for n in range(0, len(list(key)), 1):
		if (key[n] in string.ascii_letters):
			sys.stdout.write('Please insert a valid Key\n')
			keyReader()
	#keep the loop with only alphabetic characters
	if(int(key) > 26):
		while (int(key) > 26):
			key = int(key) - 26
	return int(key)
	

def encrypt (K):
	#this code encrypts a message
	message = input('What do you want to encrypt?\n')
	for n in range(0, len(list(message))):
		#this guarantee only letters will change
		if (message[n] in string.ascii_letters):
			if (message[n] in string.ascii_lowercase):
				ALPHA = list(string.ascii_lowercase)
				cipher = ALPHA.index(message[n]) + K
				sys.stdout.write(string.ascii_lowercase[cipher])
			elif (message[n] in string.ascii_uppercase):
				ALPHA = list(string.ascii_uppercase)
				cipher = ALPHA.index(message[n]) + K
				sys.stdout.write(string.ascii_uppercase[cipher])
		else:
			sys.stdout.write(message[n])

#def decrypt (k):
	#this code decrypts a message

if __name__ == '__main__':
	#This is the main class c: 
	option = opReader()
	if option == '1':
		encrypt(keyReader())
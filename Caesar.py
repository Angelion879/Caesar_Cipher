import math
import string
import curses.ascii
import sys
import os

def opReader ():
	#This read what the user wants 2 do
	op = input('What do you want to do today?\nEncipher = 1\nDecipher = 2\n')
	if (curses.ascii.isalpha(op) == 1 or (1 > int(op) or int(op) > 2)):
		sys.stdout.write('Please insert an valid option\n')
		opReader()
	return op

def keyReader ():
	#this reads the key to encode or decode
	key = input('Please insert your numeric secret key: ')
	for n in range(0, len(list(key)), 1):
		if (curses.ascii.isalpha(key[n]) == 1):
			sys.stdout.write('Please insert a valid Key\n')
			keyReader()
	if(int(key) > 26):
		while (int(key) > 26):
			key = int(key) - 26
	return int(key)
	

def encrypt (K):
	#this code encrypts a message
	message = input('What do you want to encrypt?\n')
	for n in range(0, len(list(message))):
		#this guarantee only letters will change
		if (('Z' >= message[n] >= 'A') or ('z' >= message[n] >= 'a')):
			#keep the loop with only alphabetic characters
			while (K > 26):
				K = abs(K - 26)
			cipher = str(int(message[n]) + K)
			sys.stdout.write(cipher)
		else:
			sys.stdout.write(message[n])

#def decrypt (k):
	#this code decrypts a message

if __name__ == '__main__':
	#This is the main class c: 
	option = opReader()
	if option == '1':
		encrypt(keyReader())
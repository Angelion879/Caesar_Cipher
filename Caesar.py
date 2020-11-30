import math
import string
import boolean
import sys
import os

def opReader ():
	#This read what the user wants 2 do & calls the key reader
	op = input('What do you want to do today?\nEncipher = 1\nDecipher = 2\n')
	if ((op != '1') and (op != '2')):
		sys.stdout.write('Please insert an valid option\n')
		opReader()
	keyReader()

def keyReader ():
	#this reads the key to encode or decode
	key = input('Please insert your numeric secret key: ')
	for n in range(0, len(key), 1):
		if((key[n] < '0') or (key[n] > '9')):
			sys.stdout.write('Please insert a valid Key\n')
			keyReader()
	print(int(key))
	

#def encrypt (K):
	#this code encripts a message

#def decrypt (k):
	#this code decrypts a message

if __name__ == '__main__':
	#This is the main code c: 
	opReader()
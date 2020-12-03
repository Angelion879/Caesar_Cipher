import math
import string
import sys
import os

def op_Reader ():
	os.system('cls')
	#This read what the user wants 2 do
	op = input('What do you want to do today?\nEncipher = 1\nDecipher = 2\n')
	if (op in string.ascii_letters or (1 > int(op) or int(op) > 2)):
		sys.stdout.write('Please insert an valid option\n')
		op_Reader()
	return op

def key_Reader ():
	os.system('cls')
	#this reads the key to encode or decode
	key = input('Please insert your numeric secret key: ')
	for n in range(0, len(list(key)), 1):
		if (key[n] in string.ascii_letters):
			sys.stdout.write('Please insert a valid Key\n')
			key_Reader()
	return int(key)
	

def encrypt (k):
	#this code encrypts a message
	message = input('What do you want to encrypt?\n')
	for n in range(0, len(list(message))):
		#this guarantee only letters will change
		if (message[n] in string.ascii_letters):
			if (message[n] in string.ascii_lowercase):
				ALPHA = list(string.ascii_lowercase)
				cipher = ALPHA.index(message[n]) + k
				#keep the loop with only alphabetic characters
				while (cipher > 25):
					cipher = (cipher - 26)
				sys.stdout.write(string.ascii_lowercase[cipher])
			elif (message[n] in string.ascii_uppercase):
				ALPHA = list(string.ascii_uppercase)
				cipher = ALPHA.index(message[n]) + k
				#keep the loop with only alphabetic characters
				while (cipher > 25):
					cipher = (cipher - 26)
				sys.stdout.write(string.ascii_uppercase[cipher])
		else:
			sys.stdout.write(message[n])

def decrypt (k):
	#this code decrypts a message
	message = input('What do you want to decrypt?\n')
	for n in range(0, len(list(message))):
		#this guarantee only letters will change
		if (message[n] in string.ascii_letters):
			if (message[n] in string.ascii_lowercase):
				ALPHA = list(string.ascii_lowercase)
				clear = ALPHA.index(message[n]) - k
				#keep the loop with only alphabetic characters
				while (clear < 0):
					clear = clear + 26
				sys.stdout.write(string.ascii_lowercase[clear])
			elif (message[n] in string.ascii_uppercase):
				ALPHA = list(string.ascii_uppercase)
				clear = ALPHA.index(message[n]) - k
				#keep the loop with only alphabetic characters
				while (clear < 0):
					clear = clear + 26
				sys.stdout.write(string.ascii_uppercase[clear])
		else:
			sys.stdout.write(message[n])

if __name__ == '__main__':
	#This is the main class c: 
	option = op_Reader()
	if option == '1':
		encrypt(key_Reader())
	elif option == '2':
		decrypt(key_Reader())
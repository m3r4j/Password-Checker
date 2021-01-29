import os # List files
import re # Regular expressions / pattern matching
import getpass # Hide characters when asking 
from colorama import Fore, Back, Style # Command Line colors
import sys # Terminating the program


# If 'passlists' directory is not found then terminate program
if not os.path.exists('passlists'):
	print(Fore.RED + 'passlists directory not found.')
	sys.exit()

# Go into 'passlists' directory
os.chdir('passlists')

# Get the password input / use getpass module for input to hide the characters
password = getpass.getpass(Fore.BLUE + 'Enter your password: ')

# Get all the files in a directory
contentsDir = os.listdir()

if len(contentsDir) == 0:
	print(Fore.RED + 'No files were found in passlists directory')
	sys.exit()

# Find files only that end with .txt
TxtRegex = re.compile(r'.txt$')


# Check if their isn't any that is ending with .txt and delete it
for files in range(len(contentsDir)):
	if not TxtRegex.search(contentsDir[files]):
		del contentsDir[files]



# This is the amount of times it gets detected
count = 0

# Scan all the files
for files in contentsDir:
	with open(files, 'r', encoding='utf8', errors='ignore') as file:
		data = file.readlines()
		
		# Get rid of all the \n characters because they mess things up when matching data with password
		for passes in range(len(data)):
			data[passes] = data[passes].rstrip('\n')


	for passwords in data:
		if password == passwords:
			print(Fore.RED + f'Password was found in - {files}')

			# Amount of times detected adds one
			count += 1

# Display extra info
print()
if count:
	print(f'Password detected {count} times.')
	print('Password Strength: Weak')
else:
	print(Fore.GREEN + 'No matches found.')
	print(Fore.GREEN + 'Password Strength: Strong')





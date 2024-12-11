#import needed libraries
import random
import string

#create variables
emptyPassword = []
charType = []

#verify wanted legnth of the password
numOfCharacters = input("How many characters would you like your password to be?")

#verify the types of characters the user wants in their password
wantLower = input("Would you like lower case letters? (y/n)")
if wantLower == 'y':
  charType.append('lower')

wantUpper = input("Would you like upper case letters? (y/n)")
if wantUpper == 'y':
  charType.append('upper')

wantNums = input("Would you like digits? (y/n)")
if wantNums == 'y':
  charType.append('nums')

wantSpecialCharacters = input("Would you like special characters? (y/n)")
if wantSpecialCharacters == 'y':
  charType.append('punctuation')

#create the random password
for x in range(int(numOfCharacters)):
  #randomize the character type
  randCharType = random.choice(charType)

  #randomize the character value based on the random character
  if randCharType == 'lower' :
    char = random.choice(string.ascii_lowercase)
  elif randCharType == 'upper' :
    char = random.choice(string.ascii_uppercase)
  elif randCharType == 'nums' :
    char = random.choice(string.digits)
  else :
    char = random.choice(string.punctuation)

  #append the character to the password list
  emptyPassword.append(char)

#conver the list to a string
password = ''.join(str(x) for x in emptyPassword)

print(password)
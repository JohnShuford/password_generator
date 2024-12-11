# Chat GPT Improvements
import random
import string

# User input for password length
while True:
    numOfCharacters = input("How many characters would you like your password to be? ")
    if numOfCharacters.isdigit():
        numOfCharacters = int(numOfCharacters)
        break
    else:
        print("Please enter a valid integer.")

# Determine character types
charType = []
if input("Would you like lower case letters? (y/n) ").lower() == 'y':
    charType.append('lower')
if input("Would you like upper case letters? (y/n) ").lower() == 'y':
    charType.append('upper')
if input("Would you like digits? (y/n) ").lower() == 'y':
    charType.append('nums')
if input("Would you like special characters? (y/n) ").lower() == 'y':
    charType.append('punctuation')

if not charType:
    print("No character types selected. Exiting...")
    exit()

char_map = {
    'lower': string.ascii_lowercase,
    'upper': string.ascii_uppercase,
    'nums': string.digits,
    'punctuation': string.punctuation
}

# Build the password
password_chars = []
for _ in range(numOfCharacters):
    randCharType = random.choice(charType)
    password_chars.append(random.choice(char_map[randCharType]))

# Join into final password string
password = ''.join(password_chars)
print(password)

'''
~~~Begining of John's OG work and first attempt~~
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
'''
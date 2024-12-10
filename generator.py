import random
import string

numOfCharacters = input("How many characters would you like your password to be?")

password01 = []

for x in range(int(numOfCharacters)):
  num = random.choice(string.digits)
  password01.append(num)

password = ''.join(str(x) for x in password01)

print(password)

'''
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation
random.choice(string.ascii_letters)
'''
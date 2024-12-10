import random
import string

password01 = []

for x in range(4):
  num = random.randint(0, 9)
  password01.append(num)

password = ''.join(str(x) for x in password01)

print(password)

string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation
random.choice(string.ascii_letters)
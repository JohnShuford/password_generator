import secrets
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

if numOfCharacters < len(charType):
    print(f"Password length must be at least {len(charType)} to satisfy all selected character types. Exiting...")
    exit()

char_map = {
    'lower': string.ascii_lowercase,
    'upper': string.ascii_uppercase,
    'nums': string.digits,
    'punctuation': string.punctuation
}

# Guarantee at least one character from each selected type
password_chars = [secrets.choice(char_map[t]) for t in charType]

# Fill remaining positions from the combined pool for a uniform distribution
pool = ''.join(char_map[t] for t in charType)
password_chars += [secrets.choice(pool) for _ in range(numOfCharacters - len(charType))]

# Shuffle using Fisher-Yates with a cryptographically secure source
for i in range(len(password_chars) - 1, 0, -1):
    j = secrets.randbelow(i + 1)
    password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

password = ''.join(password_chars)
print(password)

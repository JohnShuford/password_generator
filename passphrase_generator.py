import secrets
import os

# Load word list from words.txt (1024 words = exactly 10 bits of entropy per word
# when selected with a cryptographically secure RNG)
_script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_script_dir, "words.txt")) as _f:
    WORD_LIST = [line.strip() for line in _f if line.strip()]

# User input for number of words
while True:
    numOfWords = input("How many words would you like in your passphrase? (recommended: 4-6) ")
    if numOfWords.isdigit() and int(numOfWords) > 0:
        numOfWords = int(numOfWords)
        break
    else:
        print("Please enter a valid positive integer.")

# Choose a separator
print("\nChoose a separator between words:")
print("  1. Hyphen  ( - )")
print("  2. Underscore ( _ )")
print("  3. Period  ( . )")
print("  4. Space   (   )")
print("  5. None    (no separator)")

while True:
    separatorChoice = input("Enter choice (1-5): ")
    separatorMap = {
        '1': '-',
        '2': '_',
        '3': '.',
        '4': ' ',
        '5': '',
    }
    if separatorChoice in separatorMap:
        separator = separatorMap[separatorChoice]
        break
    else:
        print("Please enter a number between 1 and 5.")

# Ask about capitalization
capitalize = input("\nWould you like to capitalize each word? (y/n) ").lower() == 'y'

# Ask about appending a number
addNumber = input("Would you like to add a random number at the end? (y/n) ").lower() == 'y'

# Build the passphrase using a cryptographically secure RNG
words = [secrets.choice(WORD_LIST) for _ in range(numOfWords)]

if capitalize:
    words = [word.capitalize() for word in words]

passphrase = separator.join(words)

if addNumber:
    # secrets.randbelow(10000) gives a uniform draw over 0-9999 (~13.3 bits of entropy)
    passphrase += str(secrets.randbelow(10000))

print("\nYour passphrase is:", passphrase)

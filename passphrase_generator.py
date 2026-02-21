import random

# A list of common, easy-to-remember words for building passphrases
WORD_LIST = [
    "apple", "brave", "cabin", "dance", "eagle", "fence", "grape", "happy",
    "irony", "juice", "kneel", "lemon", "mango", "night", "ocean", "piano",
    "queen", "river", "stone", "tiger", "uncle", "vivid", "whale", "xenon",
    "yacht", "zebra", "amber", "blaze", "coral", "delta", "ember", "flute",
    "glory", "honey", "ivory", "jewel", "karma", "lunar", "maple", "noble",
    "olive", "pearl", "quill", "raven", "solar", "torch", "ultra", "valor",
    "water", "pixel", "youth", "zonal", "arena", "brush", "cloud", "drift",
    "epoch", "frost", "grain", "haste", "inlet", "joust", "knack", "latch",
    "mirth", "nerve", "onset", "prism", "quirk", "realm", "swift", "thorn",
    "umbra", "vault", "wrath", "bison", "crisp", "dwarf", "fairy", "gecko",
    "hotel", "index", "jelly", "koala", "llama", "magic", "ninja", "otter",
    "panda", "radar", "salsa", "talon", "using", "vivid", "waltz", "extra",
    "yodel", "zesty", "abbey", "bluff", "craft", "daisy", "elbow", "flair",
    "guava", "hinge", "image", "jumbo", "kayak", "lingo", "marsh", "notch",
    "outdo", "plumb", "quest", "risky", "scalp", "tabby", "unify", "venom",
]

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

# Build the passphrase
words = [random.choice(WORD_LIST) for _ in range(numOfWords)]

if capitalize:
    words = [word.capitalize() for word in words]

passphrase = separator.join(words)

if addNumber:
    passphrase += str(random.randint(10, 999))

print("\nYour passphrase is:", passphrase)

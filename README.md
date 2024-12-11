# Password Generator
This command-line Python tool allows users to generate a random password based on their desired criteria, including lowercase letters, uppercase letters, digits, and special characters.

## Features
Customizable Character Sets:
- Users can choose which character types (lowercase, uppercase, digits, punctuation) are included in the generated password.

Dynamic Length Input:
- Users are prompted to specify the password length, ensuring that the password fits their requirements.

Error Handling & Validation:
- The script validates the user’s input for password length, requiring a valid integer before proceeding. It also checks that at least one character type is selected.

## Installation
1. Ensure you have Python 3 installed.
2. Clone this repository or download the script file.
3. Install any necessary dependencies (though this tool only uses the standard library, so no additional installations should be needed).

## Usage
### Run the script:
```
python password_generator.py
```

### Follow the prompts in the terminal:
  - Password Length: Enter the desired number of characters (must be a valid integer).
  - Include Lowercase? (y/n)
  - Include Uppercase? (y/n)
  - Include Digits? (y/n)
  - Include Special Characters? (y/n)

### Once all inputs are provided, the script generates and displays a random password that meets the specified criteria.
*Example*
  - How many characters would you like your password to be? 12
  - Would you like lower case letters? (y/n) y
  - Would you like upper case letters? (y/n) y
  - Would you like digits? (y/n) y
  - Would you like special characters? (y/n) n
  - Example Output:
    - aBc9dE3fGhX2


## Code Overview
- Input Validation:
  - The script uses a while True: loop to repeatedly prompt the user for a password length until a valid integer is received.
- Character Type Verification:
  - It checks whether the user selected at least one character type. If not, the script notifies the user and exits.
- Random Selection:
  - Each character in the password is chosen randomly from the selected character sets.

## Contributing

If you’d like to contribute improvements or fixes:
1. Fork the repository.
2. Create a new branch for your changes.
3. Commit and push your changes.
4. Open a Pull Request explaining the modifications.

> [!NOTE]
> All constructive feedback and suggestions are welcome!


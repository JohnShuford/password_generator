# Password Generator

A command-line Python toolkit for generating secure passwords. Two generators are included: one that builds passwords from randomized characters, and one that assembles memorable passphrases from a word list.

Both tools use Python's `secrets` module, which draws from the operating system's cryptographically secure random number generator (`/dev/urandom` on Linux/macOS). This makes the output suitable for real security use, unlike `random`, which is not designed for cryptographic purposes.

---

## Understanding Password Security

### Why Length and Complexity Matter

Password strength is measured in **bits of entropy** — the number of possible guesses an attacker must make to crack it by brute force. Every additional character or word multiplies the difficulty exponentially. Modern hardware can test billions of guesses per second against stolen password hashes, so length is your primary defense.

---

### Random Character Passwords (`generator.py`)

When you enable all four character types, your pool is **94 possible characters** per position. Entropy scales with every character added:

| Length | Entropy (all 4 types) | Security Level | Suitable For |
|--------|----------------------|----------------|--------------|
| 8 chars | ~52 bits | Weak | Do not use — crackable in hours with modern hardware |
| 10 chars | ~66 bits | Low | Minimal risk accounts only |
| 12 chars | ~79 bits | Moderate | Low-stakes accounts (streaming, forums) |
| 16 chars | ~105 bits | Strong | Standard accounts (email, social media) |
| 20 chars | ~131 bits | Very Strong | High-value accounts (banking, primary email) |
| 24+ chars | ~157+ bits | Excellent | Encryption keys, root credentials, password manager master password |

> **Important:** Using fewer character types shrinks the pool and reduces entropy at every length. A 12-character password with only lowercase letters has ~56 bits of entropy — significantly weaker than a 12-character password using all four types (~79 bits). Enable all four types for maximum strength.

**Recommended minimum:** 16 characters with all four character types enabled for any account you care about.

---

### Passphrases (`passphrase_generator.py`)

Passphrases trade raw character entropy for human memorability. This generator draws from the **EFF Large Wordlist**, the industry standard for diceware-style passphrases. The list contains **7,776 words**, giving each word approximately **12.9 bits of entropy** (log₂ 7776 ≈ 12.92). The EFF list was specifically designed so words are unambiguous, easy to spell, and comfortable to type.

| Word Count | Entropy (words only) | With Number Suffix | Security Level | Suitable For |
|------------|---------------------|-------------------|----------------|--------------|
| 4 words | ~52 bits | ~65 bits | Low | Low-stakes accounts only |
| 5 words | ~65 bits | ~78 bits | Moderate | Low-stakes accounts |
| 6 words | ~78 bits | ~91 bits | Strong | Standard accounts (email, social media) |
| 7 words | ~90 bits | ~104 bits | Very Strong | High-value accounts (banking, primary email) |
| 8 words | ~103 bits | ~117 bits | Excellent | Critical accounts, password manager master password |
| 10 words | ~129 bits | ~143 bits | Outstanding | Encryption keys, root credentials |

> **Note:** The number suffix adds ~13.3 bits of entropy (uniform draw over 0–9999). Capitalization adds roughly 1 bit per word. For best results, enable both options. A 6-word passphrase with a number suffix reaches ~91 bits — strong enough for most accounts and far easier to remember than a random character password of equivalent strength.

---

### Best Practices

- **Use a unique password for every account.** If one site is breached, your other accounts stay safe.
- **Use a password manager** (Bitwarden, 1Password, KeePass, etc.) to store your credentials. You only need to memorize one strong master password.
- **Enable multi-factor authentication (MFA)** on every account that supports it. Even a weak password becomes much harder to exploit with MFA enabled.
- **Never use personal information** — birthdays, names, addresses, or dictionary words on their own — as a password.
- **Never reuse passwords** across accounts, especially between low-value and high-value accounts.
- **Longer is almost always better.** If a site allows 64 or 128 characters, use them.

---

## Installation

1. Ensure you have **Python 3** installed.
2. Clone this repository or download the script files.
3. No external dependencies are required — both tools use only the Python standard library.

```
git clone <repository-url>
cd password_generator
```

---

## How to Use

### Random Character Generator (`generator.py`)

This tool generates a password by randomly selecting characters from the character sets you enable. All characters are drawn from a single combined pool, ensuring a uniform distribution across every selected type. The generator also guarantees that at least one character from each selected type appears in the final password, satisfying sites that require a mix of character types.

**Run the script:**
```
python generator.py
```

**How it gathers input:**

The generator walks you through a short series of interactive terminal prompts. You respond to each prompt before the password is generated:

1. **Password length** — Enter a whole number for how many characters you want. The script will keep asking until you enter a valid positive integer.
   ```
   How many characters would you like your password to be? 16
   ```

2. **Character type selection** — Four separate yes/no prompts, one for each character type. Answer `y` to include that type or `n` to exclude it. Input is case-insensitive.
   ```
   Would you like lower case letters? (y/n) y
   Would you like upper case letters? (y/n) y
   Would you like digits? (y/n) y
   Would you like special characters? (y/n) y
   ```

   If you answer `n` to all four prompts, the script exits and asks you to run it again with at least one type selected.

3. **Output** — The generated password is printed immediately.
   ```
   Generated password: tK#8mZ!qR2@wLvX9
   ```

**Example session (recommended settings):**
```
How many characters would you like your password to be? 20
Would you like lower case letters? (y/n) y
Would you like upper case letters? (y/n) y
Would you like digits? (y/n) y
Would you like special characters? (y/n) y

Generated password: r@4Xk!mZ8#wQ2TvLp9&N
```

---

### Passphrase Generator (`passphrase_generator.py`)

This tool builds a passphrase by randomly selecting words from the EFF Large Wordlist (7,776 words) and combining them with your chosen formatting options. The result is easier to remember than a random character password while still providing strong protection.

**Run the script:**
```
python passphrase_generator.py
```

**How it gathers input:**

The generator prompts you through four customization steps before assembling your passphrase:

1. **Word count** — Enter a whole number for how many words to include. The script recommends 4–6 but accepts any positive integer. Refer to the entropy table above and aim for at least 7 words for real protection.
   ```
   How many words would you like in your passphrase? (recommended: 4-6) 8
   ```

2. **Separator** — Choose how words are joined together by entering a number from the menu:
   ```
   Choose a separator:
   1. Hyphen (-)
   2. Underscore (_)
   3. Period (.)
   4. Space ( )
   5. None
   Enter choice (1-5): 1
   ```

3. **Capitalization** — Choose whether to capitalize the first letter of each word. Answers are case-insensitive.
   ```
   Capitalize each word? (y/n) y
   ```

4. **Number suffix** — Choose whether to append a random number (0–9999) to the end of the passphrase. This adds approximately 13.3 bits of entropy and is recommended.
   ```
   Add a random number to the end? (y/n) y
   ```

5. **Output** — The assembled passphrase is printed immediately.
   ```
   Generated passphrase: River-Stone-Eagle-Piano-Tiger-Ocean-Cabin-Dance-742
   ```

**Example session (recommended settings):**
```
How many words would you like in your passphrase? (recommended: 4-6) 8
Choose a separator:
1. Hyphen (-)
2. Underscore (_)
3. Period (.)
4. Space ( )
5. None
Enter choice (1-5): 1
Capitalize each word? (y/n) y
Add a random number to the end? (y/n) y

Generated passphrase: River-Stone-Eagle-Piano-Tiger-Ocean-Cabin-Dance-742
```

---

## Contributing

If you'd like to contribute improvements or fixes:
1. Fork the repository.
2. Create a new branch for your changes.
3. Commit and push your changes.
4. Open a Pull Request explaining the modifications.

> [!NOTE]
> All constructive feedback and suggestions are welcome!

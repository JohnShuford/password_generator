# Password Generator

This repository contains two command-line Python tools for generating secure passwords — one that builds traditional character-based passwords, and one that generates memorable word-based passphrases.

---

## Understanding Password Security

Not all passwords are created equal. The strength of a password comes down to **length** and **unpredictability**. Here's what you need to know to stay safe:

### Character-Based Passwords (`generator.py`)

The more character types you include and the longer the password, the harder it is to crack. Below are general thresholds to keep in mind:

| Length | Character Set Used | Security Level |
|--------|--------------------|----------------|
| 1–7    | Any                | **Weak** — crackable in seconds with modern hardware |
| 8–11   | Lowercase only     | **Weak** — brute-forceable in minutes to hours |
| 8–11   | Mixed (upper + lower + digits + symbols) | **Moderate** — sufficient for low-risk accounts |
| 12–15  | Mixed              | **Strong** — good for most personal accounts |
| 16+    | Mixed              | **Very Strong** — recommended for email, banking, and sensitive accounts |
| 20+    | Mixed              | **Excellent** — exceeds what most attacks can reasonably target |

**Best Practices:**
- Use at least **12 characters** for any account that matters.
- Always include **uppercase, lowercase, digits, and special characters** when the site allows it.
- Never reuse passwords across accounts — a leaked password from one site becomes a key to all your others.
- Store passwords in a password manager rather than writing them down or reusing them.

---

### Passphrase Passwords (`passphrase_generator.py`)

Passphrases are a sequence of random words strung together (e.g. `coral-Tiger-Frost-Ninja42`). They are longer by nature, which makes them extremely resistant to brute-force attacks, and they are far easier for humans to remember.

| Number of Words | Example | Security Level |
|-----------------|---------|----------------|
| 1–2 words       | `apple-mango` | **Weak** — too short, too guessable |
| 3 words         | `river-stone-tiger` | **Moderate** — acceptable for low-risk use |
| 4 words         | `coral-frost-noble-torch` | **Strong** — recommended minimum |
| 5–6 words       | `brave-maple-prism-solar-inlet` | **Very Strong** — great for master passwords |
| 6+ words with number | `Whale-Ember-Vault-Kneel-Blaze-Orbit99` | **Excellent** — exceeds most attack capabilities |

**Best Practices:**
- Use at least **4 words** for any real account.
- Add a number or separator to increase entropy further.
- Passphrases are ideal for **master passwords** (e.g. your password manager) because they're long, strong, and memorable.
- Avoid using famous phrases, song lyrics, or quotes — random is the key word here.

---

## Installation

1. Ensure you have **Python 3** installed.
2. Clone this repository or download the script files.
3. No additional dependencies are required — both scripts use only the Python standard library.

```bash
git clone https://github.com/JohnShuford/password_generator.git
cd password_generator
```

---

## How to Use

### Character-Based Password Generator (`generator.py`)

Run the script:
```bash
python generator.py
```

This script walks you through a series of yes/no prompts to build your password. Here is how it gathers input from you, step by step:

1. **Password length** — You are asked how many characters you want. You must enter a valid whole number. If you enter anything else (letters, decimals, symbols), the script will reject it and ask again until you provide a valid integer.

2. **Character types** — You are then asked four separate yes/no questions:
   - Would you like lowercase letters? (`a–z`)
   - Would you like uppercase letters? (`A–Z`)
   - Would you like digits? (`0–9`)
   - Would you like special characters? (`!@#$%` etc.)

   Answer `y` or `n` for each. You must select at least one type — if you skip all four, the script will exit and ask you to start over.

Once all inputs are collected, the script randomly picks from your chosen character sets and prints a password of your requested length.

**Example session:**
```
How many characters would you like your password to be? 14
Would you like lower case letters? (y/n) y
Would you like upper case letters? (y/n) y
Would you like digits? (y/n) y
Would you like special characters? (y/n) n

Output: aB3dEfG2hIjK4m
```

---

### Passphrase Generator (`passphrase_generator.py`)

Run the script:
```bash
python passphrase_generator.py
```

This script also guides you through a series of prompts, but instead of building a password character by character, it selects random words from a built-in word list. Here is how it gathers input from you, step by step:

1. **Number of words** — You are asked how many words you want in your passphrase. You must enter a valid positive whole number. The script recommends 4–6 words for a strong result.

2. **Separator** — You are shown a numbered menu and asked to pick how the words should be joined together:
   - `1` — Hyphen (`-`)
   - `2` — Underscore (`_`)
   - `3` — Period (`.`)
   - `4` — Space (` `)
   - `5` — No separator

   You must enter a number between 1 and 5. Invalid entries will prompt you to try again.

3. **Capitalization** — You are asked whether you want each word capitalized (e.g. `Coral` instead of `coral`). Answer `y` or `n`.

4. **Trailing number** — You are asked whether you want a random number (between 10 and 999) added to the end. Answer `y` or `n`. This adds extra entropy without making the passphrase harder to remember.

Once all inputs are collected, the script assembles your passphrase and prints it.

**Example session:**
```
How many words would you like in your passphrase? (recommended: 4-6) 4

Choose a separator between words:
  1. Hyphen  ( - )
  2. Underscore ( _ )
  3. Period  ( . )
  4. Space   (   )
  5. None    (no separator)
Enter choice (1-5): 1

Would you like to capitalize each word? (y/n) y
Would you like to add a random number at the end? (y/n) y

Your passphrase is: Coral-Tiger-Frost-Ninja42
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

# Security Audit & Vault Integration Guide

*For the `password_generator` project — covering code hygiene, Bitwarden setup, cross-device use, and agentic workflows.*

---

## 1. Code Security Audit

### Verdict: ✅ Cryptographically Sound

Both `generator.py` and `passphrase_generator.py` use Python's `secrets` module, which draws from `/dev/urandom` (Linux/macOS) or `CryptGenRandom` (Windows) — the OS-level cryptographically secure random number generator. This is the correct choice. The `random` module should never be used for security-sensitive generation; `secrets` is what the Python docs recommend for exactly this use case.

**Specific findings:**

| Item | File | Status | Notes |
|------|------|--------|-------|
| CSPRNG usage | Both | ✅ Pass | `secrets.choice()` and `secrets.randbelow()` are correct |
| Fisher-Yates shuffle | `generator.py` | ✅ Pass | Implemented correctly using `secrets.randbelow()` — avoids the modulo bias that plagues naive implementations |
| EFF Large Wordlist | `passphrase_generator.py` | ✅ Pass | 7,776 words ≈ 12.9 bits/word — industry standard |
| Guaranteed character class coverage | `generator.py` | ✅ Pass | At least one character per selected type before filling the pool |
| No hardcoded secrets | Both | ✅ Pass | No API keys, tokens, or credentials in source |
| `.gitignore` | `.gitignore` | ✅ Pass | `.env` and `venv/` are excluded — nothing sensitive will leak to git |
| Password printed to stdout | Both | ⚠️ Note | Terminal output can be captured by process monitors or screen recording. Acceptable for personal CLI use, but worth being aware of. |
| No clipboard integration | Both | ℹ️ Info | Passwords are printed, not copied. Consider piping to `pbcopy` (macOS) or `xclip` (Linux) for clipboard use — see Section 4. |

**No changes required to the code itself.** The cryptographic implementation is correct.

---

## 2. Bitwarden Setup (Cross-Device)

### Install

| Platform | Method |
|----------|--------|
| macOS | `brew install bitwarden-cli` or download from bitwarden.com |
| Linux | `npm install -g @bitwarden/cli` or download AppImage |
| iOS / Android | Install Bitwarden app from App Store / Play Store |
| Browser | Install the Bitwarden browser extension |

All devices sync to the same vault via your Bitwarden account. Changes made on one device appear on all others within seconds.

### First-time setup

```bash
# Log in
bw login your@email.com

# Unlock the vault (required each session)
export BW_SESSION=$(bw unlock --raw)

# Verify sync
bw sync
```

> **Master password strength:** Use your `passphrase_generator.py` with 8 words + number suffix. That gives ~117 bits of entropy — well above the 80-bit minimum recommended for vault master passwords. Write it on paper and store it somewhere physically secure (safe, locked drawer). Do NOT store it digitally anywhere.

---

## 3. Integrating the Generator with Bitwarden

You can pipe output from either generator directly into the Bitwarden CLI to create a new item without ever seeing the password on screen:

### Store a generated password directly into Bitwarden

```bash
# Generate a password and store it immediately
PASSWORD=$(python generator.py | tail -1)

bw get template item | \
  jq --arg name "example.com" \
     --arg username "you@example.com" \
     --arg password "$PASSWORD" \
  '.name=$name | .login.username=$username | .login.password=$password | .type=1' | \
  bw encode | \
  bw create item

unset PASSWORD
```

> The `unset PASSWORD` at the end removes the secret from your shell's environment. `tail -1` captures only the password line from the generator output.

### Simpler: Copy generated password to clipboard

```bash
# macOS
python generator.py | tail -1 | pbcopy && echo "Copied to clipboard."

# Linux (requires xclip)
python generator.py | tail -1 | xclip -selection clipboard && echo "Copied to clipboard."
```

Then paste into Bitwarden's browser extension or app to create a new item manually.

---

## 4. Agentic Use — Claude Code & Scripts

For automated/agentic workflows, you should **never** have secrets in:
- `.env` files committed to git
- Hardcoded in scripts
- In shell history (`~/.zsh_history`, `~/.bash_history`)

### Recommended pattern: Inject at runtime via `bw`

```bash
# Unlock once at the start of a session
export BW_SESSION=$(bw unlock --raw)

# Retrieve a secret when needed (never stored in a file)
export MY_API_KEY=$(bw get password "My Service API Key")

# Run your script
python my_script.py

# Clear when done
unset MY_API_KEY BW_SESSION
```

Your script reads `os.environ["MY_API_KEY"]` — the secret is never written to disk.

### For Claude Code specifically

Claude Code can run `bw get password "item name"` as a bash command to retrieve credentials mid-task. To enable this safely:

1. Create a **locked item** in Bitwarden for each credential Claude Code needs
2. Name items clearly (e.g., `"GitHub Token - Claude Code"`)
3. Keep the `BW_SESSION` environment variable set in your terminal session before invoking Claude Code
4. Use minimal-scope tokens — create API keys with read-only or limited permissions where possible
5. Rotate tokens regularly (quarterly is a reasonable baseline)

### Bitwarden Secrets Manager (optional, for heavier use)

If you're running many automated workflows, Bitwarden's **Secrets Manager** product is purpose-built for this:
- Separate from your personal vault
- Machine credentials scoped to specific projects
- Audit logs for every secret access
- Available on the Teams/Enterprise plan

---

## 5. Attack Vectors — Priority Order

### 🔴 Critical (address first)

**1. Master password phishing**
Someone tricks you into entering your Bitwarden master password on a fake site. Mitigation: Enable TOTP 2FA in Bitwarden account settings (`Settings → Security → Two-step login`). Use an authenticator app (Ente Auth, Aegis, or 1Password TOTP) — not SMS.

**2. Device compromise**
If your laptop or phone has malware, a vault can't protect against a keylogger or memory scraper. Mitigation: Keep OS and apps patched. Enable FileVault (macOS) or BitLocker (Windows) full-disk encryption. Don't install software from untrusted sources.

**3. Vault session left unlocked**
A logged-in vault session on a shared or unattended device exposes everything. Mitigation: Set a vault timeout in Bitwarden settings — 15 minutes of inactivity is a good default. Enable lock-on-sleep. On mobile, enable biometric unlock but keep PIN/passphrase as fallback.

### 🟡 Medium (address next)

**4. Clipboard sniffing**
When a password is copied to clipboard, other apps can read it. Mitigation: Enable "Clear clipboard" in Bitwarden settings (30 seconds). Use autofill where possible instead of copy-paste.

**5. Browser extension attack surface**
Malicious browser extensions can interact with the vault extension. Mitigation: Regularly audit installed extensions. Keep the Bitwarden extension updated. Use a dedicated browser profile for high-security accounts if needed.

**6. Shell history leakage**
Commands with secrets typed inline get saved to `~/.zsh_history`. Mitigation: Prefix sensitive commands with a space (disables history in most shells), or use the `bw get` injection pattern above so secrets never appear in the command itself.

**7. Agentic token over-scoping**
Claude Code or scripts using API keys with more permissions than needed. Mitigation: Create narrowly-scoped tokens per use case. A token used for read-only data access should not have write permissions.

### 🟢 Low (good hygiene, lower urgency)

**8. Password reuse across environments**
Using the same password in dev/staging/prod. Mitigation: Generate unique credentials for every environment — this is exactly what your generator is for.

**9. Unencrypted backup of vault export**
Bitwarden lets you export your vault, but the default JSON export is unencrypted. Mitigation: If you export for backup, use the encrypted export option, and store the backup in an encrypted location (encrypted disk image, etc.).

**10. Weak 2FA backup codes**
Backup codes stored in a plain text file. Mitigation: Store 2FA backup codes inside Bitwarden itself (in a secure note), not in an unprotected file.

---

## 6. Quick-Start Checklist

- [ ] Install Bitwarden CLI (`bw`) on laptop
- [ ] Install Bitwarden app on phone
- [ ] Install Bitwarden browser extension
- [ ] Create a strong master passphrase using `passphrase_generator.py` (8 words + number)
- [ ] Enable TOTP 2FA on your Bitwarden account
- [ ] Set vault timeout to 15 minutes in Bitwarden settings
- [ ] Enable "Clear clipboard after 30 seconds" in Bitwarden settings
- [ ] Set `BW_SESSION` pattern in your shell profile for agentic workflows
- [ ] Enable FileVault / BitLocker on your laptop
- [ ] Audit browser extensions for anything unfamiliar

---

*Generated by Claude for Delta — February 2026*

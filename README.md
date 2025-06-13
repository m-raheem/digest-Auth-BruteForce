# Digest Auth Brute-Forcer

A multithreaded Python script for brute-forcing HTTP Digest Authentication endpoints using customizable user and password wordlists. Designed for red team operators and penetration testers conducting authorized engagements.

> ⚠️ **Legal Notice**: This tool is intended for **authorized testing** and **educational purposes only**. Unauthorized use is strictly prohibited.

---

## 🚀 Features

- ✅ Multi-user and multi-password brute-force support
- 🚀 Fast execution with configurable multithreading
- 💥 Graceful handling of Ctrl+C interruptions
- 📜 Simple CLI with `argparse`
- 🛡️ Timeout and exception-safe requests

---

## 🛠 Requirements

- Python 3.6+
- `requests` library

Install dependencies with:

```bash
pip install requests
```

## ⚙️ Usage

```bash
python3 digest_bruteforce.py \
  -u usernames.txt \
  -p passwords.txt \
  -t http://target.com/protected \
  -th 20
```

| 🧩 Argument        | 📘 Description                                 |
| ------------------ | ---------------------------------------------- |
| `-u`, `--userlist` | 📂 Path to the username wordlist file          |
| `-p`, `--passlist` | 🔐 Path to the password wordlist file          |
| `-t`, `--target`   | 🎯 Target URL (Digest Auth protected endpoint) |
| `-th`, `--threads` | 🚀 Number of threads to use (default: `10`)    |

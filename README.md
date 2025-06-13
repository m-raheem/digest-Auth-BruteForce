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

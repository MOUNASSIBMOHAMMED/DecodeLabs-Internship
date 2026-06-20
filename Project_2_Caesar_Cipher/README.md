---

```markdown
# 🔐 DecodeLabs Project 2: The Evolution of Data Confidentiality 

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Cryptography-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
This project was developed during the **DecodeLabs Cybersecurity Internship**. The objective of this module is to practically demonstrate the evolution of data security from classical classical ciphers to modern enterprise encryption standards. 

By building both offensive and defensive cryptographic scripts from scratch, this repository illustrates how readable plaintext is transformed into secure ciphertext, and critically, why classical encryption models completely fail against modern computing power.

---

## 🏛️ Part 1: The Classical Engine (`caesar.py`)
The first phase of the project implements a classical substitution cipher. Unlike basic scripts that manually swap letters using hardcoded dictionaries, this engine utilizes pure mathematical logic, **Zero-Indexing**, and modular arithmetic to manipulate ASCII values.

### The Cryptographic Math
The engine relies on Python's `ord()` and `chr()` functions to convert text into integers. To handle extreme shift keys without generating invalid characters, the script standardizes the alphabet to a 0-25 scale and applies a strict modulo operation (`% 26`).

* **Encryption Formula:** $E_n(x) = (x + n) \% 26$
* **Decryption Formula:** $D_n(x) = (x - n) \% 26$

### Key Features
* **Intelligent Edge-Case Handling:** The script actively identifies spaces, numbers, and punctuation, allowing them to pass through unaltered while only encrypting alphabetical characters.
* **Symmetric Architecture:** Uses a single numeric key for both locking and unlocking data.

---

## ⚠️ Part 2: The Brute-Force Vulnerability (`bruteforce.py`)
The Caesar Cipher has a fatal architectural flaw: **an incredibly small key space.** Because the English alphabet only contains 26 letters, there are only **25 possible cryptographic keys**. 

To demonstrate this vulnerability, this repository includes an offensive security tool (`bruteforce.py`). This script does not attempt to mathematically reverse the cipher or trick the system. Instead, it utilizes raw computational power to aggressively test every single possible shift key simultaneously. 

When fed an intercepted ciphertext, this script cracks the encryption and reveals the original plaintext in a fraction of a millisecond, proving that classical ciphers are entirely obsolete in the modern computing era.

---

## 🛡️ Part 3: The Enterprise Standard (`aes_encrypting.py`)
To bridge the gap between classical theory and modern security, the final phase of this project implements military-grade encryption using the **Advanced Encryption Standard (AES-128)** via the official Python `cryptography` library (Hazmat layer).

### Architectural Upgrades
Where the Caesar cipher fails, this AES implementation succeeds by changing the fundamental rules of the encryption:
1. **The Key Space:** Instead of 25 keys, AES-128 uses a 128-bit key, creating $3.4 \times 10^{38}$ possible combinations. Brute-forcing this algorithm would take all the supercomputers on Earth longer than the age of the universe.
2. **Block Cipher Mechanics:** Instead of encrypting letter-by-letter, AES processes data in strict 16-byte blocks, utilizing bitwise XOR logic to create mathematical confusion and diffusion.
3. **PKCS7 Padding:** The script intelligently injects dummy bytes to ensure all data perfectly aligns with the 16-byte block requirement.
4. **Initialization Vectors (IV):** The engine generates cryptographically secure random IVs (`os.urandom`) so that encrypting the exact same message twice produces completely different ciphertexts, neutralizing frequency analysis attacks.

---

## 🚀 Execution & Usage

### Prerequisites
* Python 3.x
* The `cryptography` library (required only for AES):
  ```bash
  pip install cryptography

```

### Running the Toolset

**1. Secure a message using the classical cipher:**

```bash
python caesar.py

```

**2. Attack an intercepted ciphertext via Brute-Force:**

```bash
python bruteforce.py

```

**3. Run the modern AES-128 block cipher pipeline:**

```bash
python aes_encrypting.py

```

---

*Developed by Mohammed Mounassib | DecodeLabs Batch 2026*

```

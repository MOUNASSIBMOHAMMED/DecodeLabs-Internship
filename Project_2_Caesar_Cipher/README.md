Here is the complete, unified Master `README.md`. It seamlessly combines your portfolio introduction with the detailed breakdown of the Project 2 cryptography engines and the AES comparison.

You can copy this entire block and paste it directly into the main `README.md` file at the root of your `decode labs` folder.

```markdown
# 🛡️ DecodeLabs Cybersecurity Internship Portfolio

Welcome to my professional cybersecurity portfolio. This repository documents my technical progression and hands-on engineering projects completed during the DecodeLabs Internship (Batch 2026).

## 👨‍💻 About the Author
**Mohammed Mounassib**
* Engineering Student at ENSA d'Oujda
* Specializing in Network Administration, Cybersecurity, and Python Development.

---

## 📂 Project 1: The Gatekeeper Engine
A fail-fast authentication script designed to simulate strict access control mechanisms. *(Located in the `Project_1_Gatekeeper` directory)*.

---

## 📂 Project 2: The Caesar Cipher & Cryptographic Vulnerabilities
This project explores the fundamental mechanics of symmetric encryption by building a mathematical Caesar Cipher. It demonstrates how classical cryptography transforms readable plaintext into secure ciphertext, and critically, why classical ciphers completely fail against modern computing power. *(Located in the `Project_2_Caesar_Cipher` directory)*.

### ⚙️ The Classical Engine (`caesar.py`)
Unlike manual "letter-swapping," this engine uses **Zero-Indexing** and modular arithmetic to securely shift ASCII characters. It bypasses numbers and punctuation while scrambling the alphabet.

* **Encryption Formula:** $E_n(x) = (x + n) \% 26$
* **Decryption Formula:** $D_n(x) = (x - n) \% 26$

By utilizing the modulo operator (`% 26`), the engine ensures a perfect finite wrap around the alphabet, allowing it to handle extreme shift keys without crashing.

### ⚠️ The Brute-Force Vulnerability (`bruteforce.py`)
The Caesar Cipher has a fatal architectural flaw: **an incredibly small key space.** Because there are only 26 letters in the alphabet, there are only **25 possible shift keys**. It does not matter how complex the message is; an attacker does not need the key. 

The included `bruteforce.py` script exploits this weakness by aggressively testing all 25 possible shifts against a locked message, allowing a standard CPU to crack the encryption and reveal the plaintext in a fraction of a millisecond.

### 🛡️ The AES Contrast (`aes_encrypting.py`)
To demonstrate how modern security engineers solve this brute-force vulnerability, this project also includes an enterprise-grade AES-128 implementation.
* **Caesar Cipher:** 25 possible keys. (Instantly cracked by a basic script).
* **AES-128:** $3.4 \times 10^{38}$ possible keys. (Impossible to brute-force; would take all the supercomputers on Earth longer than the age of the universe to crack).

Instead of shifting letters, the AES script processes raw data in 16-byte blocks, utilizes PKCS7 padding, and relies on complex bitwise XOR logic to create mathematical confusion and diffusion.

---

## 🚀 How to Run the Toolset

**1. Secure a message using the classical cipher:**
```bash
cd Project_2_Caesar_Cipher
python caesar.py

```

**2. Attack an intercepted ciphertext via Brute-Force:**

```bash
python bruteforce.py

```

**3. Run the modern AES-128 block cipher demonstration:**

```bash
python aes_encrypting.py

```


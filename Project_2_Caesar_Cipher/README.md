# 🔐 DecodeLabs Enigma Engine  
### Classical Cryptography & Modern Block Cipher Implementation  

---

## 📌 Project Overview

DecodeLabs Enigma Engine is a Python-based cryptographic toolset developed during my internship at DecodeLabs.

The project demonstrates the evolution of data confidentiality by comparing classical substitution ciphers with modern block encryption standards.

Unlike standard implementations that rely on hardcoded character mappings, this engine uses pure mathematical logic and zero-indexing to manipulate ASCII values. It then evaluates classical cipher weaknesses through brute-force analysis before transitioning into a modern AES-based encryption system.

---

## 🎯 Background and Motivation

The initial goal of this internship project was to implement a basic mathematical Caesar Cipher to demonstrate symmetric encryption using a numeric shift key.

While this satisfies the basic requirement, I explored deeper into why classical ciphers are considered obsolete in modern cybersecurity systems.

A Caesar cipher has a critical weakness:  
it contains an extremely small key space (only 25 possible keys), making it trivial to break.

To better demonstrate real-world cryptographic principles, I expanded the project into a three-stage security pipeline:

1. Implementation of the classical Caesar Cipher  
2. Development of a brute-force attack to exploit its weaknesses  
3. Integration of AES-128 encryption using industry standards  

This transformation turned the project into a full study of cryptographic evolution, from insecure substitution systems to modern block cipher architectures.

---

## ⚙️ Key Features

- Mathematical substitution cipher using modular arithmetic (% 26)  
- Robust handling of spaces, numbers, and punctuation  
- Automated brute-force attack simulation  
- AES-128 block cipher implementation using the Python cryptography library  
- Secure Initialization Vectors (IVs) generated via OS-level randomness  
- PKCS7 padding for strict block alignment  

---

## 🧠 How It Works

The toolset is structured into three progressive stages:

---

### 🔹 Stage 1: Classical Engine (`caesar.py`)

The Caesar Cipher encrypts plaintext by converting characters into ASCII values using `ord()`.

It then:
- Applies zero-indexing to normalize alphabet positions  
- Uses modular arithmetic to apply the shift  
- Converts values back into characters  

This ensures proper wrap-around behavior within the alphabet range.

---

### ⚠️ Stage 2: Vulnerability Exploitation (`bruteforce.py`)

Due to its extremely limited key space (only 25 possible shifts), the Caesar Cipher is highly vulnerable.

This script demonstrates a brute-force attack by:
- Iterating through all possible shift values  
- Decoding the ciphertext for each key  
- Outputting all potential plaintext results  

This shows that security based on small key spaces is fundamentally broken.

---

### 🔐 Stage 3: Modern Block Cryptography (`aes_encrypting.py`)

To overcome classical limitations, the project implements AES-128 encryption.

Unlike substitution ciphers, AES:
- Processes data in 16-byte blocks  
- Uses multiple rounds of transformation  
- Applies XOR-based bitwise operations  
- Ensures randomness using Initialization Vectors (IVs)  
- Uses PKCS7 padding for proper block alignment  

This expands the key space to approximately:  
**3.4 × 10³⁸ possible combinations**, making brute-force attacks computationally infeasible.

---

## 🧰 Technologies Used

- Python 3  
- OS module (os.urandom)  
- Cryptography Library (hazmat primitives)  
- Advanced Encryption Standard (AES)  
- Cipher Block Chaining (CBC Mode)  

---

## 📁 Project Structure


decode-labs-internship/
│
├── Project_2_Caesar_Cipher/
│ ├── aes_encrypting.py
│ ├── bruteforce.py
│ ├── caesar.py
│ └── README.md


---

## 🚀 Installation and Usage

### 1. Install dependencies
```bash
pip install cryptography
2. Clone repository
git clone https://github.com/MOUNASSIBMOHAMMED/DecodeLabs-Internship.git
cd DecodeLabs-Internship/Project_2_Caesar_Cipher
3. Run Caesar Cipher
python caesar.py
4. Run brute-force attack
python bruteforce.py
5. Run AES encryption demo
python aes_encrypting.py
🚀 Future Improvements
File encryption support (.txt, .pdf, etc.)
HMAC-based integrity verification
RSA asymmetric encryption integration
Graphical User Interface (GUI) for AES tool
Enhanced key management system
📚 Learning Outcomes

This project provided hands-on experience in both classical and modern cryptography.

Key concepts learned include:

ASCII manipulation and modular arithmetic
Weaknesses of symmetric substitution ciphers
Brute-force attack methodologies
AES block cipher architecture
CBC (Cipher Block Chaining) mode
True cryptographic randomness vs pseudo-randomness
PKCS7 padding for block alignment

Most importantly, it demonstrated how to evolve a basic internship assignment into a full cryptographic study showing the transition from insecure classical systems to modern secure encryption standards.

👨‍💻 Author

Mohammed Mounassib
Cybersecurity Engineering Student
Cybersecurity Intern at DecodeLabs

🔗 GitHub: https://github.com/MOUNASSIBMOHAMMED
🔗 LinkedIn: https://www.linkedin.com/in/mohammed-mounassib-093098171/

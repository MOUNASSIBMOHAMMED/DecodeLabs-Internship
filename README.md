# 🛡️ DecodeLabs Gatekeeper: Cloud-Native Password Threat Engine

## Project Overview

DecodeLabs Gatekeeper is a Python-based password security analysis tool developed during my internship at DecodeLabs. The project evaluates password strength by combining traditional security policy validation, behavioral password analysis, and real-world breach intelligence to provide a more complete assessment of password security.

Unlike conventional password checkers that rely solely on length and character requirements, Gatekeeper incorporates modern cybersecurity practices such as breach detection through the Have I Been Pwned (HIBP) API and advanced entropy analysis using Dropbox's zxcvbn library. This allows the application to identify weak or compromised passwords while preserving user privacy.

## Background and Motivation

The initial objective of this internship project was to create a password validation tool that checked compliance with standard password policies and compared user passwords against a local rockyou.txt wordlist.

While this approach met the minimum requirements, I wanted to explore how modern security systems handle password analysis at scale. Maintaining large local dictionaries introduces storage overhead, limits portability, and cannot effectively account for newly leaked credentials from recent data breaches.

To address these limitations, I redesigned the project into a cloud-native security solution. Instead of relying on large local wordlists, Gatekeeper integrates live breach intelligence through the Have I Been Pwned API while preserving privacy using the k-Anonymity model. I also incorporated behavioral password analysis through zxcvbn to evaluate real-world password strength rather than relying exclusively on traditional complexity rules.

This transformation allowed the project to evolve from a simple compliance checker into a lightweight password threat assessment engine.

## Key Features

* Password policy compliance validation
* Real-time breached password detection using the Have I Been Pwned API
* Privacy-preserving password verification through k-Anonymity
* Advanced entropy and pattern analysis using zxcvbn
* Detection of predictable human password patterns
* Secure hidden password input using Python's getpass module
* Optimized fail-fast validation pipeline to reduce unnecessary processing

## How It Works

The application evaluates passwords through a three-stage security pipeline.

### Stage 1: Compliance Validation

The password is first checked against common security requirements, including minimum length, uppercase and lowercase letters, numbers, and special characters. If the password fails these checks, the process stops immediately to avoid unnecessary resource consumption.

### Stage 2: Breach Intelligence Verification

If the password satisfies the compliance requirements, it is hashed locally using SHA-1. Only the first five characters of the hash are transmitted to the Have I Been Pwned API. The remaining verification process occurs locally, ensuring that the complete password hash is never exposed.

This implementation follows the k-Anonymity privacy model, allowing the application to determine whether a password has appeared in known data breaches without revealing the password itself.

### Stage 3: Behavioral Security Analysis

The password is then analyzed using Dropbox's zxcvbn algorithm. This stage identifies predictable human behaviors such as common names, dates, dictionary words, keyboard patterns, and other weak structures that may satisfy complexity requirements while remaining vulnerable to attacks.

The result is a more realistic assessment of password strength and estimated resistance against brute-force and dictionary-based attacks.

## Technologies Used

* Python 3
* Requests
* Hashlib
* Zxcvbn
* Getpass
* Have I Been Pwned API

## Project Structure

```text
decode-labs-gatekeeper/
│
├── gatekeeper.py
├── .gitignore
└── README.md
```

## Installation and Usage

Install the required dependencies:

```bash
pip install requests zxcvbn
```

Clone the repository:

```bash
git clone https://github.com/MOUNASSIBMOHAMMED/DecodeLabs-Internship.git
cd DecodeLabs-Internship
```

Run the application:

```bash
python gatekeeper.py
```

## Future Improvements

Several enhancements could further expand the project's capabilities:

* Secure audit logging for security events
* Argon2id password hashing integration
* Rate limiting and abuse prevention mechanisms
* Password history validation
* Multi-factor authentication readiness checks
* Web-based dashboard for password security reporting

## Learning Outcomes

This project provided valuable hands-on experience in modern cybersecurity engineering and secure software development. Through its development, I gained practical knowledge in:

* Secure API integration
* Privacy-preserving security architectures
* Password security best practices
* Threat intelligence utilization
* Cloud-native security concepts
* Git and GitHub version control workflows
* Technical documentation and project presentation

Most importantly, this project taught me how to take a basic set of internship requirements and transform them into a more advanced and innovative cybersecurity solution by applying industry practices and modern security concepts.

## Author

**Mohammed Mounassib**
Cybersecurity Engineering Student
Cybersecurity Intern at DecodeLabs

🔗 GitHub: https://github.com/MOUNASSIBMOHAMMED

🔗 LinkedIn: https://www.linkedin.com/in/mohammed-mounassib-093098171/

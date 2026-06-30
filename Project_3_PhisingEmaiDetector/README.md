This version is designed to be comprehensive and professional, perfect for a high-level cybersecurity portfolio. It dives into the "why" and "how" of your security logic.

---

# Project 3: Enterprise Phishing Triage Engine

## 📖 Executive Summary

The **Enterprise Phishing Triage Engine** is a specialized, production-grade security utility engineered to identify, isolate, and document sophisticated phishing attempts in real-time. Developed as the milestone project for the **DecodeLabs** industrial training program, this engine transitions from basic string-matching to an advanced, multi-layered threat analysis system.

The primary mission of this tool is to act as a **Human Firewall**, bridging the gap between passive email filtering and active threat hunting. It is designed to assist security analysts in conducting rapid triage of suspicious communications, utilizing automated decision-tree logic to decide whether to close an incident, warn a user, or initiate a full-scale escalation.

---

## 🛠 Architectural Overview

The engine utilizes a **Modular Threat Analysis Architecture**. By decoupling detection logic, threat intelligence, and reporting, the tool remains highly scalable and easy to maintain as the threat landscape evolves.

### 1. The Ingestion Engine (`eml_parser.py`)

This module handles the dirty work of processing raw SMTP traffic. Unlike simple scripts, it performs deep inspection of the `.eml` file structure:

* 
**Cryptographic Header Validation**: Instead of relying on display names, the engine parses hidden `Authentication-Results` headers to verify **SPF, DKIM, and DMARC** mathematical signatures.


* 
**MIME-Type Intelligence**: It dynamically inspects email parts, specifically flagging image attachments for potential **Quishing (QR Code Phishing)** attempts.



### 2. The Intelligence Core (`utils/rules.py`)

This is the "brain" of the operation. It acts as a centralized repository for enterprise threat intelligence.

* 
**Regex-Based Signature Matching**: Utilizes YARA-style regex signatures to hunt for technical artifacts, including crypto-wallets, obfuscated IPs, and browser-in-the-browser (BitB) iframe injections.


* 
**Homoglyph Mapping**: Features an advanced normalization engine that maps internationalized characters to their Latin equivalents, neutralizing attempts to spoof legitimate brands like Microsoft or PayPal via character substitution.



### 3. The Enterprise Scanner (`triage_enterprise.py`)

The main pipeline coordinates three critical analysis streams:

* 
**Heuristic Analysis**: Integrates the NLTK Sentiment Intensity Analyzer to detect psychological triggers—such as urgency, panic, or financial demand—that force users to bypass logical verification.


* **External API Integration**: Includes native support for **VirusTotal** queries, allowing the engine to cross-reference extracted links against 70+ global security vendors for real-time reputation scoring.
* 
**Behavioral Triage**: Specifically detects modern "Multi-Channel" lures such as **TOAD (Telephone-Oriented Attack Delivery)**, where an email contains zero URLs but forces a callback to a malicious support center.



---

## 🛡 Advanced Threat Taxonomy

The tool implements detection for the 11 Red Flags identified in the DecodeLabs curriculum :

* 
**Sender-Domain Mismatch & Display Name Spoofing** 


* 
**Fake Forwarded Chains** 


* 
**Browser-in-the-Browser (BitB) Attacks** 


* 
**Dangerous Attachments (ISO/JS/SCR)** 


* 
**Urgent Bypass Requests (BEC)** 


* 
**MFA Fatigue & Push Bombing** 


* 
**Security Callback Scams (TOAD)** 


* 
**QR Code (Quishing) Prompts** 


* 
**Deepfake/Voicemail Lures** 



---

## 📁 Artifacts & Reporting

### Sample Lures (`/samples`)

The engine is bundled with a suite of simulation templates designed to test the limits of our detection rules:

* **TOAD Attack**: Tests callback scams with no URLs.
* **Crypto Extortion**: Tests for Base64 obfuscation and high-panic sentiment language.
* **Quishing Simulation**: Validates the engine's ability to correlate image attachments with QR-specific keywords.

### Automated SOC Reporting (`/reports`)

Every scan generates a structured **JSON Incident Report**. These logs include the full header history, cryptographic validation status, extracted Indicators of Compromise (IoCs), and the final risk score. This data is structured to be ingested directly into SIEM (Security Information and Event Management) platforms, significantly reducing the "mean time to respond" (MTTR) for security analysts.

---

## ⚖️ Ethical & Defensive Mandate

This engine is built on the **Pause, Verify, Report** philosophy. It is intended for defensive use only, enabling security teams to mirror real-world attack tactics safely. By automating the triage of common lures, we empower security teams to focus on the high-value threats that truly require human intervention.

---

### ⚙️ Usage

To scan an email:

```bash
python triage_enterprise.py -f samples\toad_attack.eml

```

*Final Verdict Action Loop:*

* 
**Safe**: Close Incident 


* 
**Suspicious**: Warn User 


* 
**Malicious**: Block Domain & Escalate 



---

*Built with security-first engineering by MOHAMMED MOUNASSIB

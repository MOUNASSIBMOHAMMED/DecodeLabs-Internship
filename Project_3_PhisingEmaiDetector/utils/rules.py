# utils/rules.py

class ThreatIntelligence:
    """Central repository for enterprise threat intelligence, signatures, and heuristics."""
    
    @staticmethod
    def get_protected_brands():
        """High-target brands frequently impersonated in credential harvesting."""
        return [
            "amazon", "paypal", "microsoft", "google", "decodelabs", 
            "office365", "docusign", "apple", "netflix", "bankofamerica",
            "chase", "wellsfargo", "linkedin", "facebook", "meta", "instagram",
            "twitter", "x.com", "adobe", "salesforce", "zoom", "dropbox",
            "onedrive", "sharepoint", "github", "gitlab", "stripe", "fedex", "ups"
        ]

    @staticmethod
    def get_yara_regex_rules():
        """
        Comprehensive dictionary of Regular Expressions hunting for technical artifacts,
        obfuscation methodologies, malware infrastructure, and crypto leakage.
        """
        return {
            # Cryptocurrency Indicators (Extortion/Ransomware)
            "Bitcoin Wallet": r"\b(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}\b",
            "Ethereum Wallet": r"\b0x[a-fA-F0-9]{40}\b",
            "Monero Wallet": r"\b4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}\b",
            "Litecoin Wallet": r"\b[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}\b",
            
            # Network & Infrastructure Obfuscation
            "Obfuscated IP (Hex)": r"0x[0-9a-fA-F]{2}\.0x[0-9a-fA-F]{2}\.0x[0-9a-fA-F]{2}\.0x[0-9a-fA-F]{2}",
            "Obfuscated IP (Octal)": r"0[0-7]{3}\.0[0-7]{3}\.0[0-7]{3}\.0[0-7]{3}",
            "IP with Embedded Port": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}\b",
            
            # Delivery Mechanisms & Web Exploits
            "Hidden HTML Redirection": r"(?i)<meta\s+http-equiv=[\"']refresh[\"']\s+content=[\"']\d+;\s*url=",
            "Data URL Scheme (Phishing Link)": r"(?i)href=[\"']data:text/html;base64,",
            "Credential Harvesting Structure": r"(?i)(login|signin|verify|auth|account|secure).*\.php\?.*=",
            "Auto-Download Trigger": r"(?i)window\.location\.href\s*=\s*[\"'].*\.(exe|zip|scr|iso)[\"']",
            
            # Third-Party Infrastructure Abuse (C2 / Exfiltration)
            "Discord Webhook Abuse": r"(?i)discord\.com/api/webhooks/\d+/[A-Za-z0-9_-]+",
            "Telegram Bot API Usage": r"(?i)api\.telegram\.org/bot[0-9]+:[A-Za-z0-9_-]+",
            "Ngrok Tunneling Detection": r"(?i).*\.ngrok-free\.app",
            "Interactsh OOB Exfiltration": r"(?i).*\.interactsh\.com",

            # --- NEW DECODELABS PROJECT 3 RED FLAGS ---
            
            # [Red Flag 2] Fake Forwarded Chains (Spoofed FW: headers in body)
            "Fake Forwarded Thread": r"(?i)(From:|Date:|Subject:)\s+.*(FW:|RE:)",
            
            # [Red Flag 3] BitB (Browser-in-the-Browser) Fake SSO pop-ups
            "BitB Iframe Structure": r"(?i)<iframe.*src=.*(login|signin|oauth).*>|window\.open\(.*(login|popup)",
            
            # [Red Flag 9] TOAD (Telephone-Oriented Attack Delivery) Call center scams
            "Suspicious Callback Number": r"\b(1-)?(800|888|877|866|855|844|833)-\d{3}-\d{4}\b",
            
            # [Red Flag 11] Deepfake / Voicemail Lures
            "Voice/Voicemail Attachment": r"(?i)(new voicemail|audio message|missed call|vmsg_.*\.wav|.*\.mp3)"
        }

    @staticmethod
    def get_homoglyph_map():
        """
        Maps lookalike Cyrillic, Greek, or Latin extended characters 
        frequently used to bypass string matching filters.
        """
        return {
            'а': 'a', 'с': 'c', 'е': 'e', 'о': 'o', 'р': 'p', 'х': 'x', 'у': 'y',
            'і': 'i', 'ѕ': 's', 'ԁ': 'd', 'ԛ': 'q', 'ԝ': 'w', '┱': 't', 'м': 'm',
            'Α': 'A', 'Β': 'B', 'Ε': 'E', 'Ζ': 'Z', 'Η': 'H', 'Ι': 'I', 'Κ': 'K',
            'Μ': 'M', 'Ν': 'N', 'Ο': 'O', 'Ρ': 'P', 'Τ': 'T', 'Χ': 'X', 'Υ': 'Y'
        }

    @staticmethod
    def get_toxic_keywords():
        """Psychological trigger words signaling BEC, extortion, or urgency."""
        return [
            # Original keywords
            "wire transfer", "payment failed", "password expired", "mfa bypass", 
            "billing issue", "invoice overdue", "account suspended", "unauthorized login",
            "w2 statement", "tax refund", "gift card", "helpdesk ticket", "it support",
            "immediate action", "final notice", "deactivation warning", "payroll update",
            "ceo demand", "urgent request", "action required", "secure verification",
            
            # --- NEW DECODELABS PROJECT 3 RED FLAGS ---
            "approve sign-in", "authenticator push", "mfa fatigue", # [Red Flag 8]
            "scan to unlock", "qr code", "scan this code",          # [Red Flag 10]
            "strictly confidential", "bypass standard procedure",   # [Red Flag 5 addition]
            "account locked", "unusual sign-in"                     # [Red Flag 7 addition]
        ]

    @staticmethod
    def get_suspicious_tlds():
        """Top-Level Domains statistically tied to high volumes of malicious infrastructure."""
        return [
            ".xyz", ".top", ".click", ".club", ".work", ".ru", ".cn", ".tk", ".ml", 
            ".ga", ".cf", ".gq", ".live", ".info", ".biz", ".download", ".online"
        ]

    @staticmethod
    def get_malicious_extensions():
        """File attachments or extensions wrapped inside scripts that pose critical risks."""
        return [
            r"(?i)\.exe\b", r"(?i)\.scr\b", r"(?i)\.vbs\b", r"(?i)\.bat\b", 
            r"(?i)\.ps1\b", r"(?i)\.iso\b", r"(?i)\.img\b", r"(?i)\.cab\b", 
            r"(?i)\.cmd\b", r"(?i)\.msi\b", r"(?i)\.jar\b", r"(?i)\.hta\b"
        ]
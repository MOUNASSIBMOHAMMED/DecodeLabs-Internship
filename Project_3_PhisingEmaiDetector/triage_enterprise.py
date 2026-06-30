import re
import base64
import urllib.parse
import argparse
import json
import os
import requests
from datetime import datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from utils.eml_parser import EMLAnalyzer
from utils.rules import ThreatIntelligence

nltk.download('vader_lexicon', quiet=True)

# ---------------------------------------------------------
# LEVEL 1: EXTERNAL THREAT INTELLIGENCE (VirusTotal)
# ---------------------------------------------------------
VT_API_KEY = "YOUR_API_KEY_HERE"  # Replace with a free VirusTotal API key later

def check_virustotal(url):
    """Queries the VirusTotal API to see if global vendors flagged the URL."""
    if VT_API_KEY == "YOUR_API_KEY_HERE":
        return "[Skipped] No API Key configured."
        
    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        headers = {"x-apikey": VT_API_KEY}
        response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)
        
        if response.status_code == 200:
            stats = response.json()['data']['attributes']['last_analysis_stats']
            malicious_count = stats['malicious']
            if malicious_count > 0:
                return f"[CRITICAL] VirusTotal: {malicious_count} security vendors flagged this URL as malware."
            return "[SAFE] VirusTotal: 0 vendors flagged this URL."
    except Exception as e:
        return f"[Error] VT API failed: {e}"
    return "[Unknown] URL not found in VT database."

class EnterprisePhishingScanner:
    def __init__(self):
        self.flags = []
        self.risk_score = 0
        self.sia = SentimentIntensityAnalyzer()
        
        self.protected_brands = ThreatIntelligence.get_protected_brands()
        self.regex_rules = ThreatIntelligence.get_yara_regex_rules()
        self.toxic_keywords = ThreatIntelligence.get_toxic_keywords()
        self.suspicious_tlds = ThreatIntelligence.get_suspicious_tlds()
        self.malicious_extensions = ThreatIntelligence.get_malicious_extensions()
        self.homoglyph_map = ThreatIntelligence.get_homoglyph_map()
        
    def add_flag(self, severity, message, score_increase):
        self.flags.append(f"[{severity}] {message}")
        self.risk_score += score_increase

    def normalize_homoglyphs(self, text):
        normalized_chars = []
        for char in text:
            normalized_chars.append(self.homoglyph_map.get(char, char))
        return "".join(normalized_chars)

    def deobfuscate_content(self, text):
        decoded_text = text
        for match in re.findall(r"(?:[A-Za-z0-9+/]{4}){10,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?", text):
            try:
                decoded = base64.b64decode(match).decode('utf-8', errors='ignore')
                if any(char.isalnum() for char in decoded):
                    self.add_flag("HIGH", f"Obfuscation: Hidden Base64 string payload -> {decoded[:40]}...", 30)
                    decoded_text += f" {decoded}"
            except: pass
        return decoded_text

    def run_regex_hunter(self, text):
        for threat_name, pattern in self.regex_rules.items():
            if re.findall(pattern, text):
                self.add_flag("CRITICAL", f"Signature Match: {threat_name} pattern identified.", 45)

    def analyze_heuristics(self, text):
        if self.sia.polarity_scores(text)['neg'] > 0.15:
            self.add_flag("HIGH", f"NLP Analysis: Strong negative sentiment / panic language.", 25)
        for word in self.toxic_keywords:
            if word in text.lower():
                self.add_flag("MEDIUM", f"Contextual Heuristic: Phishing indicator triggered -> '{word}'", 15)

    def scan_email(self, parsed_data):
        print("🛡️  V3 ENTERPRISE THREAT ENGINE INITIATED")
        print("=" * 65)
        
        clean_text = self.deobfuscate_content(self.normalize_homoglyphs(parsed_data.body))
        self.run_regex_hunter(clean_text)
        self.analyze_heuristics(clean_text)

        # TOAD and Quishing
        phone_matches = re.findall(r"\b(1-)?(800|888|877|866|855|844|833)-\d{3}-\d{4}\b", clean_text)
        if phone_matches and len(parsed_data.urls) == 0:
            self.add_flag("CRITICAL", "TOAD Attack: High-prominence phone number detected with zero URLs.", 50)

        if parsed_data.has_image_attachments and any(q in clean_text.lower() for q in ["qr code", "scan to"]):
            self.add_flag("CRITICAL", "Quishing: Image attachment detected with QR scanning instructions.", 50)

        # LEVEL 1: API Integration (VirusTotal)
        for url in parsed_data.urls:
            vt_result = check_virustotal(url)
            print(f"[*] VT API Check: {url} -> {vt_result}")
            if "[CRITICAL]" in vt_result:
                self.add_flag("CRITICAL", f"Threat Intel API: Domain flagged by VirusTotal -> {url}", 100)

        # Verdict Generation
        verdict = "SAFE"
        if self.risk_score >= 50: verdict = "MALICIOUS"
        elif self.risk_score > 0: verdict = "SUSPICIOUS"

        print(f"\n--- THREAT DIAGNOSTICS (Total Risk Score: {self.risk_score}) ---")
        print(f"Verdict: {verdict}")
        for flag in self.flags:
            print(f"  {flag}")
        print("=" * 65)
        
        # LEVEL 3: SOC Automation Trigger
        self.generate_soc_report(parsed_data, verdict)

    # ---------------------------------------------------------
    # LEVEL 3: AUTOMATED SOC REPORTING (SIEM INTEGRATION)
    # ---------------------------------------------------------
    def generate_soc_report(self, parsed_data, verdict):
        """Dumps a professional JSON log file for SIEM ingestion."""
        if not os.path.exists("reports"):
            os.makedirs("reports")
            
        report_data = {
            "scan_timestamp": datetime.now().isoformat(),
            "verdict": verdict,
            "risk_score": self.risk_score,
            "headers": parsed_data.headers,
            "auth_results": parsed_data.auth_results,
            "extracted_urls": parsed_data.urls,
            "indicators_of_compromise": self.flags
        }
        
        filename = f"reports/scan_{datetime.now().strftime('%Y%md_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=4)
        print(f"\n[+] Automated SOC Report generated: {filename}")

if __name__ == "__main__":
    cli_parser = argparse.ArgumentParser(description="DecodeLabs Enterprise SOC Triage Engine")
    cli_parser.add_argument("-f", "--file", required=True, help="Path to the target raw .eml file")
    args = cli_parser.parse_args()
    
    parser = EMLAnalyzer(args.file)
    print(f"\n[*] Ingesting: {args.file}...")
    
    if parser.parse():
        parser.print_extracted_data() 
        scanner = EnterprisePhishingScanner()
        
        # LEVEL 2: Cryptographic Header Enforcement
        if parser.auth_results['SPF'] == 'Fail' or parser.auth_results['DKIM'] == 'Fail':
            scanner.add_flag("CRITICAL", "Cryptographic Failure: SPF/DKIM mathematical signature validation failed.", 50)
            
        scanner.scan_email(parser)
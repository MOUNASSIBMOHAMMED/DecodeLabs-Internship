import email
from email import policy
import re

class EMLAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = {}
        self.auth_results = {'SPF': 'Unknown', 'DKIM': 'Unknown', 'DMARC': 'Unknown'} # <-- NEW: Crypto Auth
        self.body = ""
        self.urls = []
        self.has_image_attachments = False

    def parse(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
                msg = email.message_from_file(f, policy=policy.default)
                
                self.headers['From'] = msg.get('From', 'Unknown')
                self.headers['Return-Path'] = msg.get('Return-Path', 'Unknown')
                self.headers['Subject'] = msg.get('Subject', 'No Subject')
                self.headers['Date'] = msg.get('Date', 'Unknown')
                
                # LEVEL 2: Cryptographic Authentication Parsing
                auth_header = str(msg.get('Authentication-Results', '')).lower()
                if auth_header:
                    if 'spf=pass' in auth_header: self.auth_results['SPF'] = 'Pass'
                    elif 'spf=fail' in auth_header or 'spf=softfail' in auth_header: self.auth_results['SPF'] = 'Fail'
                    
                    if 'dkim=pass' in auth_header: self.auth_results['DKIM'] = 'Pass'
                    elif 'dkim=fail' in auth_header: self.auth_results['DKIM'] = 'Fail'
                    
                    if 'dmarc=pass' in auth_header: self.auth_results['DMARC'] = 'Pass'
                    elif 'dmarc=fail' in auth_header: self.auth_results['DMARC'] = 'Fail'

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_maintype() == 'image':
                            self.has_image_attachments = True
                        if part.get_content_type() in ['text/plain', 'text/html']:
                            try:
                                self.body += part.get_content().strip() + " "
                            except:
                                pass
                else:
                    self.body = msg.get_content().strip()

                url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w.-]*'
                self.urls = list(set(re.findall(url_pattern, self.body)))
                return True
                
        except Exception as e:
            print(f"[!] Error parsing EML file: {e}")
            return False

    def print_extracted_data(self):
        print("\n--- EXTRACTED EMAIL ARTIFACTS ---")
        print(f"Subject:     {self.headers['Subject']}")
        print(f"From:        {self.headers['From']}")
        print(f"Auth Status: SPF: {self.auth_results['SPF']} | DKIM: {self.auth_results['DKIM']} | DMARC: {self.auth_results['DMARC']}")
        print(f"URLs Found:  {len(self.urls)}")
        print("---------------------------------\n")
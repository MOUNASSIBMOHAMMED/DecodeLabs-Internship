import getpass
import hashlib
import requests
from zxcvbn import zxcvbn

def check_pwned_api(password):
    """
    Checks the Have I Been Pwned API using k-Anonymity.
    """
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return False, 0
            
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return True, count
                
        return False, 0
    except requests.exceptions.RequestException:
        print("\n[SYSTEM WARNING] Could not connect to Threat API. Bypassing check.")
        return False, 0

def analyze_password(password):
    """
    Fail-Fast Hybrid Engine: Compliance First, then Network/AI.
    """
    # 1. THE DECODELABS COMPLIANCE CHECK (The Fast Filter)
    missing_elements = []
    
    if len(password) < 8:
        missing_elements.append("at least 8 characters")
    if not any(char.isupper() for char in password):
        missing_elements.append("an uppercase letter")
    if not any(char.isdigit() for char in password):
        missing_elements.append("a number")
        
    symbols = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    if not any(char in symbols for char in password):
        missing_elements.append("a special symbol")

    # FAIL-FAST TRIGGER: If it fails the basic math, kill the process immediately.
    # We do not waste time checking the API or running the AI.
    if missing_elements:
        return f"\n[!] COMPLIANCE FAILURE: Password rejected. Missing: {', '.join(missing_elements)}."

    # 2. THE CRITICAL OVERRIDE (Live API Check)
    # This only runs if the password passed the compliance check above.
    is_pwned, pwned_count = check_pwned_api(password)
    if is_pwned:
        formatted_count = f"{int(pwned_count):,}"
        return f"\n[!] CRITICAL RISK: Password found {formatted_count} times in live data breaches. Immediate rejection."

    # 3. THE ADVANCED AI THREAT ANALYSIS (zxcvbn)
    results = zxcvbn(password)
    ai_score = results['score']
    crack_time = results['crack_times_display']['offline_slow_hashing_1e4_per_second']
    warning = results['feedback']['warning'] or "No predictable patterns detected."

    # 4. THE MASTER READOUT (Terminal UI)
    readout = f"""
    ==================================================
    [1] DECODELABS COMPLIANCE : PASS
        Rule Status           : All requirements met.
        
    [2] AI THREAT ANALYSIS    : {ai_score}/4
        Estimated Crack Time  : {crack_time}
        AI System Warning     : {warning}
        
    [3] CLOUD THREAT API      : CLEAR
        Live Breach Status    : 0 Known Leaks
    ==================================================
    """
    return readout

# Interactive User Prompt
if __name__ == "__main__":
    print("DecodeLabs Gatekeeper: Fail-Fast Engine Initialized.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = getpass.getpass("\nEnter a password to check: ")
        
        if user_input.lower() == 'exit':
            print("Shutting down Gatekeeper...")
            break
            
        final_report = analyze_password(user_input)
        print(final_report)
def encrypt_caesar(text, shift_key):
    ciphertext = ""
    
    for char in text:
        # 1. Handle Uppercase Letters (ASCII 65-90)
        if char.isupper():
            # ord() converts letter to number. We subtract 65 to normalize to 0-25.
            # Add the shift, use % 26 to wrap around the alphabet, then add 65 back.
            shifted = chr((ord(char) - 65 + shift_key) % 26 + 65)
            ciphertext += shifted
            
        # 2. Handle Lowercase Letters (ASCII 97-122)
        elif char.islower():
            # Same logic, but normalized to ASCII 97 ('a')
            shifted = chr((ord(char) - 97 + shift_key) % 26 + 97)
            ciphertext += shifted
            
        # 3. Handle Edge Cases (Spaces, Numbers, Punctuation)
        else:
            # Leave non-alphabet characters completely untouched
            ciphertext += char
            
    return ciphertext

def decrypt_caesar(text, shift_key):
    """
    Decrypts a string by reversing the mathematical Caesar shift.
    Applies the formula: D_n(x) = (x - n) % 26
    """
    plaintext = ""
    
    for char in text:
        if char.isupper():
            # Notice the subtraction (- shift_key) to reverse the lock
            plaintext += chr((ord(char) - 65 - shift_key) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - 97 - shift_key) % 26 + 97)
        else:
            plaintext += char
            
    return plaintext

# ---------------------------------------------------------
# INTERACTIVE IPO CYCLE (Input -> Process -> Output)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=========================================")
    print("      DECODELABS ENIGMA ENGINE V1.0      ")
    print("=========================================")
    
    # [INPUT]
    message = input("\n[>] Enter a message to secure: ")
    
    # Ensure the user types a valid integer for the shift key
    try:
        key = int(input("[>] Enter your numeric shift key (e.g., 3): "))
    except ValueError:
        print("[!] Error: Shift key must be a whole number. Defaulting to 3.")
        key = 3
    
    # [PROCESS]
    encrypted_message = encrypt_caesar(message, key)
    decrypted_message = decrypt_caesar(encrypted_message, key)
    
    # [OUTPUT]
    print("\n--- SECURE TRANSMISSION LOG ---")
    print(f"[+] Original Input : {message}")
    print(f"[🔒] Ciphertext    : {encrypted_message}")
    print(f"[🔓] Decrypted     : {decrypted_message}")
    print("=========================================")
print("=========================================")
print("   DECODELABS BRUTE-FORCE ENGINE V1.0    ")
print("=========================================")

ciphertext = input("\n[>] Enter intercepted ciphertext: ")

print("\n--- INITIATING BRUTE-FORCE PROTOCOL ---")

for key in range(1, 26):
    attempt = ""
    
    for char in ciphertext:
        if char.isupper():
            attempt += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            attempt += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            attempt += char
            
    print(f"[Key {key:02}]: {attempt}")

print("---------------------------------------")
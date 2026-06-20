import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def encrypt_aes_128(plaintext, key):
    """
    Encrypts a string using AES-128 in CBC Mode.
    """
    # 1. Initialization Vector (IV): A random 16-byte block to ensure the same 
    # message encrypts differently every single time.
    iv = os.urandom(16)
    
    # 2. Setup the Cipher Engine
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 3. PKCS7 Padding: AES requires exactly 16-byte (128-bit) blocks. 
    # This automatically adds dummy bytes to fill the final block.
    padder = padding.PKCS7(128).padder()
    
    # Convert text to bytes, pad it, and encrypt it
    plaintext_bytes = plaintext.encode('utf-8')
    padded_data = padder.update(plaintext_bytes) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # We return both the IV and Ciphertext (the receiver needs the IV to decrypt)
    return iv, ciphertext

def decrypt_aes_128(iv, ciphertext, key):
    """
    Decrypts AES-128 ciphertext and automatically removes the padding.
    """
    # 1. Setup the Decryption Engine using the exact same Key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # 2. Decrypt the data back into padded blocks
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # 3. Unpad the data (strip away the dummy bytes)
    unpadder = padding.PKCS7(128).unpadder()
    plaintext_bytes = unpadder.update(padded_data) + unpadder.finalize()
    
    return plaintext_bytes.decode('utf-8')

# ==========================================
# INTERACTIVE AES-128 PIPELINE
# ==========================================
if __name__ == "__main__":
    print("--- Enterprise AES-128 Engine ---")
    
    # Generate a cryptographically secure 128-bit (16-byte) random key
    # In a real app, this key is locked away in a secure vault.
    SECRET_KEY = os.urandom(16)
    print(f"\n[!] 128-bit Key Generated: {SECRET_KEY.hex()}")
    
    message = input("\n[>] Enter a highly classified message: ")
    
    # ENCRYPT
    iv, encrypted_data = encrypt_aes_128(message, SECRET_KEY)
    
    print("\n--- SECURE TRANSMISSION LOG ---")
    print(f"[+] Original   : {message}")
    print(f"[+] IV Used    : {iv.hex()}")
    print(f"[🔒] Ciphertext : {encrypted_data.hex()}")
    
    # DECRYPT
    decrypted_message = decrypt_aes_128(iv, encrypted_data, SECRET_KEY)
    print(f"[🔓] Decrypted  : {decrypted_message}")
    print("=================================")
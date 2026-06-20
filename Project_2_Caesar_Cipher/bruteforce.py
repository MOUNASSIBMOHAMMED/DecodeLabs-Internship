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
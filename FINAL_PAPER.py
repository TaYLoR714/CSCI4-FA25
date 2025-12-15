#final paper
# import Fernet from the cryptography library
from cryptography.fernet import Fernet

def run_encryption_demo():
    # 1. Generate a Key / Password
    key = Fernet.generate_key()
    
    # 2. Create the "Cipher Suite"
    cipher_suite = Fernet(key)
    
    # 3. The Message -  encrypt this text. It must be encoded to bytes (b'').
    original_message = b"This is a secret message for the final paper."
    print(f"Original: {original_message}")

    # 4. Encrypt - Automatically encrypts the message
    encrypted_text = cipher_suite.encrypt(original_message)
    print(f"Encrypted: {encrypted_text}")

    # 5. Decrypt - Use the same key to turn it back to readable text
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")

# Execute the code
if __name__ == "__main__":
    run_encryption_demo() 
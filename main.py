from cryptography.fernet import Fernet
import os

# Generate a new symmetric key and save it to 'key.key'
def generate_key(file_path="key.key"):
    key = Fernet.generate_key()
    with open(file_path, "wb") as f:
        f.write(key)
    return key

# Load the symmetric key from 'key.key'
def load_key(file_path="key.key"):
    if not os.path.exists(file_path):
        print(f"No key found. Generating a new key and saving to '{file_path}'.")
        return generate_key(file_path)
    with open(file_path, "rb") as f:
        return f.read()

# Encrypt a plaintext string
def encrypt_text(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

# Decrypt an encrypted string
def decrypt_text(encrypted_text, key):
    f = Fernet(key)
    return f.decrypt(encrypted_text.encode()).decode()

# Command-line interface
if __name__ == "__main__":
    print("=== Symmetric Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    key = load_key()  # Load or create key if missing

    if choice == "e":
        text = input("Enter text to encrypt: ").strip()
        if not text:
            print("Error: No text entered.")
        else:
            encrypted = encrypt_text(text, key)
            print("\nEncrypted text:\n" + encrypted)

    elif choice == "d":
        text = input("Enter the encrypted text: ").strip()
        try:
            decrypted = decrypt_text(text, key)
            print("\nDecrypted text:\n" + decrypted)
        except Exception:
            print("Error: Invalid encrypted text or key mismatch.")

    else:
        print("Invalid choice. Please type 'E' or 'D'.")

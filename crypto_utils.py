# crypto_utils.py

from cryptography.fernet import Fernet

# generate key (temporary for now)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(data):
    return cipher.encrypt(data)

def decrypt_file(data):
    return cipher.decrypt(data)
  

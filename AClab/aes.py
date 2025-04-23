from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import os

def get_key(password):
    return SHA256.new(password.encode()).digest()

def encrypt_file(file_path, key, output_path):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(output_path, 'wb') as f:
        f.write(ciphertext)

def decrypt_file(file_path, key, output_path):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as f:
        ciphertext = f.read()
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_path, 'wb') as f:
        f.write(plaintext)

def main():
    print("=== Lab 9: AES File Encryption/Decryption ===")
    password = input("Enter password: ")
    key = get_key(password)

    input_file = "input.txt"
    encrypted_file = "encrypted.enc"
    decrypted_file = "decrypted.txt"

    if os.path.exists(input_file):
        encrypt_file(input_file, key, encrypted_file)
        print(f"Encrypted '{input_file}' to '{encrypted_file}'")

        decrypt_file(encrypted_file, key, decrypted_file)
        print(f"Decrypted '{encrypted_file}' to '{decrypted_file}'")
    else:
        print(f"[!] File '{input_file}' not found.")

if __name__ == "__main__":
    main()

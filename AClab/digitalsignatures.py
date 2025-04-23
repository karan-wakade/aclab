# pip install pycryptodome ecdsa

from Crypto.PublicKey import RSA, ElGamal
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto import Random
from ecdsa import SigningKey, SECP256k1
import hashlib


def rsa_sign_verify(message):
    print("\n--- RSA Digital Signature ---")
    key = RSA.generate(2048)
    h = SHA256.new(message)

    signature = pkcs1_15.new(key).sign(h)
    try:
        pkcs1_15.new(key.public_key()).verify(h, signature)
        print("RSA Signature Verified Successfully.")
    except (ValueError, TypeError):
        print("RSA Signature Verification Failed.")
    print("Signature (hex):", signature.hex())


def elgamal_sign_verify(message):
    print("\n--- ElGamal Digital Signature ---")
    key = ElGamal.generate(1024, Random.new().read)
    h = int.from_bytes(SHA256.new(message).digest(), byteorder='big')

    while True:
        k = Random.new().read(128)
        k = int.from_bytes(k, byteorder='big') % key.p
        if k > 1 and sympy.gcd(k, key.p - 1) == 1:
            break

    r = pow(key.g, k, key.p)
    try:
        k_inv = pow(k, -1, key.p - 1)
        s = ((h - key.x * r) * k_inv) % (key.p - 1)
        print("ElGamal Signature Generated.")
        print(f"Signature: (r: {r}, s: {s})")
    except ValueError:
        print("Error computing modular inverse in ElGamal.")


def ecc_sign_verify(message):
    print("\n--- ECC Digital Signature ---")
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key

    signature = sk.sign(message)
    try:
        vk.verify(signature, message)
        print("ECC Signature Verified Successfully.")
    except:
        print("ECC Signature Verification Failed.")
    print("Signature (hex):", signature.hex())


def menu():
    while True:
        print("\n=== Digital Signature Menu ===")
        print("1. RSA DS")
        print("2. ElGamal DS")
        print("3. ECC DS")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice")
            continue

        if choice == '4':
            print("Exiting.")
            break

        message = input("Enter message: ").encode()
        if choice == '1':
            rsa_sign_verify(message)
        elif choice == '2':
            elgamal_sign_verify(message)
        elif choice == '3':
            ecc_sign_verify(message)


if __name__ == "__main__":
    import sympy  # Required for ElGamal modular inverse
    menu()

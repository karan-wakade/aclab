import random
import sympy

def generate_rabin_keys(bits=16):
    """Generates Rabin cryptosystem public and private keys."""
    while True:
        p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        # Ensure p and q are both congruent to 3 mod 4
        if p % 4 == 3 and q % 4 == 3:
            break

    n = p * q  # Public key
    private_key = (p, q)  # Private key
    return n, private_key

def encrypt_rabin(plaintext, n):
    """Encrypts a message using Rabin cryptosystem."""
    m = int.from_bytes(plaintext.encode(), 'big')  # Convert string to int
    if m >= n:
        raise ValueError("Message must be smaller than n")
    c = (m ** 2) % n  # Ciphertext
    return c

def decrypt_rabin(ciphertext, private_key):
    """Decrypts a Rabin ciphertext using the private key."""
    p, q = private_key
    n = p * q

    # Compute square roots using modular arithmetic
    mp = pow(ciphertext, (p + 1) // 4, p)
    mq = pow(ciphertext, (q + 1) // 4, q)

    # Solve using Chinese Remainder Theorem (CRT)
    yp, yq = sympy.mod_inverse(p, q), sympy.mod_inverse(q, p)
    r1 = (yp * p * mq + yq * q * mp) % n
    r2 = n - r1
    r3 = (yp * p * (-mq) + yq * q * mp) % n
    r4 = n - r3

    # Convert back to string if possible
    possible_messages = [r1, r2, r3, r4]
    decrypted_texts = []
    for r in possible_messages:
        try:
            decrypted_texts.append(r.to_bytes((r.bit_length() + 7) // 8, 'big').decode())
        except:
            pass  # Skip invalid conversions

    return decrypted_texts if decrypted_texts else possible_messages

if __name__ == "__main__":
    print("Generating Rabin Key Pair...")
    n, private_key = generate_rabin_keys(16)
    print(f"Public Key (n): {n}")
    print(f"Private Key (p, q): {private_key}")

    plaintext = "Hi"
    print(f"\nOriginal Message: {plaintext}")

    ciphertext = encrypt_rabin(plaintext, n)
    print(f"Ciphertext: {ciphertext}")

    decrypted_messages = decrypt_rabin(ciphertext, private_key)
    print(f"Possible Decryptions: {decrypted_messages}")

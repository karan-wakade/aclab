import random
from sympy import isprime, mod_inverse

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Generate large prime numbers
def generate_prime(bits=8):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# RSA Key Generation
def rsa_keygen(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # Common choice for e
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    return (e, n), (d, n), p, q

# RSA Encryption
def rsa_encrypt(m, public_key):
    e, n = public_key
    return pow(m, e, n)

# RSA Decryption
def rsa_decrypt(c, private_key):
    d, n = private_key
    return pow(c, d, n)

# Example
public, private, p, q = rsa_keygen(8)
message = 42
ciphertext = rsa_encrypt(message, public)
plaintext = rsa_decrypt(ciphertext, private)

print("RSA Encryption:", ciphertext)
print("RSA Decryption:", plaintext)

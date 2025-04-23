import random
from sympy import isprime, mod_inverse

def elgamal_keygen(p):
    g = random.randint(2, p-1)
    x = random.randint(2, p-2)  # Private key
    y = pow(g, x, p)  # Public key component
    return (p, g, y), x

def elgamal_encrypt(m, public_key):
    p, g, y = public_key
    k = random.randint(2, p-2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def elgamal_decrypt(c1, c2, private_key, p):
    s = pow(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    return (c2 * s_inv) % p

p = 23
public, private = elgamal_keygen(p)
message = 10
c1, c2 = elgamal_encrypt(message, public)
plaintext = elgamal_decrypt(c1, c2, private, p)

print("ElGamal Encryption:", (c1, c2))
print("ElGamal Decryption:", plaintext)

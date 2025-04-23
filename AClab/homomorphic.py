import random
import sympy

def generate_paillier_keys(bits=16):
    """Generates Paillier cryptosystem public and private keys."""
    while True:
        p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        if p != q:
            break

    n = p * q  # Public Key (modulus)
    g = n + 1  # Common choice for g
    lambda_ = (p - 1) * (q - 1) // sympy.gcd(p - 1, q - 1)  # Private key
    mu = sympy.mod_inverse(lambda_, n)  # Multiplicative inverse

    public_key = (n, g)
    private_key = (lambda_, mu)
    return public_key, private_key

def encrypt_paillier(m, public_key):
    """Encrypts a message m using Paillier cryptosystem."""
    n, g = public_key
    r = random.randint(1, n - 1)
    c = (pow(g, m, n**2) * pow(r, n, n**2)) % (n**2)  # Homomorphic encryption formula
    return c

def decrypt_paillier(c, public_key, private_key):
    """Decrypts a ciphertext c using Paillier cryptosystem."""
    n, g = public_key
    lambda_, mu = private_key
    L = lambda x: (x - 1) // n  # L function
    m = (L(pow(c, lambda_, n**2)) * mu) % n
    return m

def homomorphic_addition(c1, c2, public_key):
    """Adds two encrypted values homomorphically."""
    n, _ = public_key
    return (c1 * c2) % (n**2)  # Encrypted addition: Enc(m1) * Enc(m2) = Enc(m1 + m2)

if __name__ == "__main__":
    print("Generating Paillier Key Pair...")
    public_key, private_key = generate_paillier_keys(16)
    print(f"Public Key (n, g): {public_key}")
    print(f"Private Key (λ, μ): {private_key}")

    m1, m2 = 7, 5  # Example messages
    print(f"\nOriginal Messages: m1 = {m1}, m2 = {m2}")

    c1 = encrypt_paillier(m1, public_key)
    c2 = encrypt_paillier(m2, public_key)
    print(f"Encrypted m1: {c1}")
    print(f"Encrypted m2: {c2}")

    c_sum = homomorphic_addition(c1, c2, public_key)
    decrypted_sum = decrypt_paillier(c_sum, public_key, private_key)

    print(f"\nHomomorphic Addition Result (Decrypted): {decrypted_sum}")

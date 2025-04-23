import random

def diffie_hellman(p, g):
    a = random.randint(2, p-2)  # Alice's secret
    b = random.randint(2, p-2)  # Bob's secret
    
    A = pow(g, a, p)  # Alice sends to Bob
    B = pow(g, b, p)  # Bob sends to Alice
    
    shared_key_alice = pow(B, a, p)  # Alice computes key
    shared_key_bob = pow(A, b, p)  # Bob computes key
    
    return shared_key_alice, shared_key_bob

p = 23
g = 5
alice_key, bob_key = diffie_hellman(p, g)
print("Shared Key:", alice_key)  # Both should be same

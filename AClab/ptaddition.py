def mod_inverse(n, p):
    """Computes modular inverse of n modulo p using Extended Euclidean Algorithm."""
    return pow(n, -1, p)  # Equivalent to Fermat's theorem when p is prime

def ecc_point_addition(P, Q, a, p):
    """Performs point addition P + Q on the elliptic curve y^2 = x^3 + ax + b mod p."""
    if P == "O":  # Identity element (point at infinity)
        return Q
    if Q == "O":
        return P
    
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and y1 == -y2 % p:  # If P + (-P) = Identity element
        return "O"
    
    if P != Q:
        slope = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p
    else:
        slope = ((3 * x1**2 + a) * mod_inverse(2 * y1, p)) % p  # Point doubling case
    
    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)

# Example usage
if __name__ == "__main__":
    p = 23  # Prime number (finite field)
    a = 1   # Curve coefficient a
    P = (3, 10)
    Q = (9, 7)

    result = ecc_point_addition(P, Q, a, p)
    print(f"P + Q = {result}")

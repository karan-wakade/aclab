def mod_inverse(n, p):
    """Computes modular inverse of n modulo p using Extended Euclidean Algorithm."""
    return pow(n, -1, p)  # Using Python's built-in modular inverse function

def ecc_point_doubling(P, a, p):
    """Performs point doubling (2P) on the elliptic curve y^2 = x^3 + ax + b mod p."""
    if P == "O":  # Identity element (point at infinity)
        return "O"

    x1, y1 = P

    # Check if y1 == 0, in which case the result is the identity element
    if y1 == 0:
        return "O"

    # Compute the slope λ = (3x1^2 + a) / (2y1) mod p
    slope = ((3 * x1**2 + a) * mod_inverse(2 * y1, p)) % p

    # Compute new point (x3, y3)
    x3 = (slope**2 - 2 * x1) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)

# Example usage
if __name__ == "__main__":
    p = 23  # Prime number (finite field)
    a = 1   # Curve coefficient a
    P = (3, 10)

    result = ecc_point_doubling(P, a, p)
    print(f"2P = {result}")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD of 56 and 98:", gcd(56, 98))  # Output: 14

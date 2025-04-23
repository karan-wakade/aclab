def mod_inverse(a, m):
    m0 = m
    x0, x1 = 0, 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m  # Quotient
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0

    return x1


def main():
    a = int(input("Enter a: "))
    m = int(input("Enter m (modulus): "))

    if gcd(a, m) != 1:
        print("Modular inverse does not exist (a and m are not coprime).")
    else:
        inv = mod_inverse(a, m)
        print(f"The modular inverse of {a} mod {m} is: {inv}")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()

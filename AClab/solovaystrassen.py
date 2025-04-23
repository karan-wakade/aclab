import random

def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be an odd positive integer")
    
    a = a % n
    result = 1
    
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        
        a, n = n, a  # Quadratic reciprocity
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        
        a %= n
    
    return result if n == 1 else 0

def solovay_strassen(n, k=5):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = jacobi(a, n) % n
        if x == 0 or pow(a, (n - 1) // 2, n) != x:
            return False
    
    return True

# Example
print("Solovay-Strassen 97:", solovay_strassen(97))  # Output: True

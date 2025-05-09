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

print("Jacobi Symbol (100/13):", jacobi(100, 13))  # Output: 1

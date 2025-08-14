def power(a, b):
    # Base Case 1: b = 0 → a^0 = 1
    if b == 0:
        return 1
    # Base Case 2: b < 0 → a^b = 1 / a^(-b)
    # Base Case 2: If exponent (b) is negative, return 1 / (a^|b|)
    elif b < 0:
        return 1 / power(a, -b)
    
    # Recursive Case: Compute a^(b//2) once and reuse it
    half = power(a, b // 2)  # e.g., power(2, 3//2) = power(2, 1)
    
    # If b is even → a^b = (a^(b//2))^2
    if b % 2 == 0:
        return half * half
    # If b is odd → a^b = a * (a^(b//2))^2
    else:
        return a * half * half  # e.g., 2 * power(2,1) * power(2,1)


print(power(2, -3))  # Output: 8 (2^3 = 8)
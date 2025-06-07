def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)   
# means factorial of any number is factorial of (number-1) multiplied by that number



print(factorial(50))
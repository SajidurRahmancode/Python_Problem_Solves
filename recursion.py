def recursion(n):
    if n==1:
        return 1
    else:
        print(n)
        return recursion(n-1) 
print(recursion(8))


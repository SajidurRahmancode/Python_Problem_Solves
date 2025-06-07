def prime(n,i=2):
    if n<=1:
        return False
    if i * i > n: 
            return True
    if n%i==0:
            print(n)
            return False
    
    return prime(n,i+1) 



print(prime(15))


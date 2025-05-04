fib1 = 1
fib2 = 1

for num in range(-0,10):

  if (num == 0 or num == 1):
    
    print(fib1, end =" ")

  else:

    result = fib1 + fib2

    fib1 = result

    fib2 = fib2

    print(result,end =" ")


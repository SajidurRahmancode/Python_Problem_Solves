for num in range (2,20+1):
      for i in range(2, num):
    if (num % i) == 0:
      x=0
      break
    else: 
      x=1
  if (x==1):
    print(num, "is prime")
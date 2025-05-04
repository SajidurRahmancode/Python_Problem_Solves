#print a hollow triangle with amount of integer input from user
""" n=int(input("please enter an integer:"))
print(n)
print()

for i in range(n,0,-1):
    for j in range (1,i+1):
        if i==n:
            print('*',end='')
        elif j==1 or j==i:
            print('*',end='')
        else:
            print(" ",end='')
    print()
  """
 
def donut(r):
    for i in range(-r, r):
        for j in range(-r, r):
            if ((i*i + j*j < r*r)) and (i*i + j*j >= ((r/2)*(r/2))):
                print('#', end='')
            else:
                print('.', end='')
        print('')

donut(int(input("Radius:\n")))
    
    

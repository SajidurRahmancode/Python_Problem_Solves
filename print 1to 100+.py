sum=0
for i in range(1,101): 
 
        sum = sum + i
        if (i == 100):
            print(i, "=",end =" ")
        else:
            print(i, "+",end =" ")
 
print(sum) 

""" 
for i in range(1,101): 
        
        if (i == 100):
           print(i)
        else:
            print(i,",",end='')
 """
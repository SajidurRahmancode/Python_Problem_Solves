#class performance 4

list=["01","banana",5.00,"unit","02","mango",20.00,"kg","03","apple",15.00,"kg","04","papaya",25.00,"unit","05","guava",15.00,"kg"]

""" x=input("enter name:")
if(x in list):
    p=list.index(x)
    print(list[p],list[p+1],list[p+2])
else:
      print("not in list") """

""" 
fruit=input("enter fruit name:")
index=0

for i in range (0,20):
  if fruit==list[i]:
        index=i
print (list[index],list[index+1],list[index+2])

try: print("not in list")
except:
  print("An exception occurred") """
 

""" 
p = ["01","banana",5.00,"unit","02","Mango",20.00,"kg","03","apple",15.00,"kg","04","papaya",25.00,"unit","05","guava",15.00,"kg"]
item = input("Enter :")
i=0
while i < 20:
    if p[i]==item:
        Index = i
    i = i + 1
pi = Index + 1
pr = p[pi]
print(pr)
 """

#p = ["01","banana",5.00,"unit","02","Mango",20.00,"kg","03","apple",15.00,"kg","04","papaya",25.00,"unit","05","guava",15.00,"kg"]
item = input("Enter :")
i=0
try:
    while i < 20:
        if list[i] == item:
            Index = i
        i = i + 1
    pi = Index + 1
    pr = list[pi]
    print(pr)
except :
    print("NOT FOUND")



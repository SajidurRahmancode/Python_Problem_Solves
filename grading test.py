num=int(input("enter value"))
if(num<=100 and num>=90):
  print("A")
elif (num<90 and num>81):
  print('A-')
elif (num<71 and num>=80):
  print("b+")
elif  (num< 61 and num>=70):
  print  ("b") 
elif (num<60 and num>=51):
  print("b-")
else:
  print("f")
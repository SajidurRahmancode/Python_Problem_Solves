def area_cir (r):
      return (3.1416*r*r)
 
def area_tri (b,h):
  return (0.5*b*h)
 
option =10
 
while option !="0":
  print( "*****Menu*****")
  print("1. Area of Circle")
  print("2. Area of Triangle")
  print("0. Exit")
  option=input("Enter Your Choice : ")
 
  if (option =="1"):
    r=float(input("Enter the radius:"))
    print (area_cir (r))
 
  elif (option =="2"):
    b=float(input("Enter the base:"))
    h=float(input("Enter the height:"))
    print (area_tri (r,h))

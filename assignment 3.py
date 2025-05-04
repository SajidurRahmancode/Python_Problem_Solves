#assignment 3
#1.a program that implements the following system

""" num=int(input(' Please Enter Your Mark: \n'))
if num<=100 and num>=85:
    print('You got A grade!')
elif num<=84 and num>=80:
    print('You got A- grade')
elif num<=79 and num>=75:
    print('You got B+ grade')
elif num <= 74 and num >= 70:
    print('You got B grade')
elif num <= 69 and num >= 65:
    print('You got B- grade')
elif num <= 64 and num >= 60:
    print('You got C+ grade')
elif num <= 59 and num >= 55:
    print('You got C grade')
elif num <= 54 and num >= 50:
    print('You got C- grade')      
elif num <= 49 and num >= 45:
    print('You got D+ grade')
elif num <= 44 and num >= 40:
    print('You got D grade')                
else :
    print('You are fail')  """

""" 
#6
num=int(input(' Please Enter Your age:'))
if num<3:
    print('Infancy')
elif num>=3 and num<12:
    print('aildhood')
elif num>=12 and num<20:
    print('Adolescence')
elif num>=20 and num<40:
    print('Young adulthood')
elif num>=40 and num<65:
    print('Mature adulthood')
else : print('Late adulthood')  """


""" # Python Program to if a character is Lowercase or Uppercase
character = input("Enter Your Own character : ")

if(ord(character) >= 65 and ord(character) <= 90): 
    print("The character ", character, "is Uppercase") 
elif(ord(character) >= 97 and ord(character) <= 122):
    print("The character ", character, "is  Lowercase")
elif(ord(character) >= 48 and ord(character) <= 57):
        print("The character ", character, "is  Digit")
else:
    print("The character ", character, "is symbol") """



""" 
print("1. Area of circle")
print("2. Area of a rectangle")
print("3. Area of a triangle")
print("4. Volume of a cylinder")
print("5. Volume of a sphere")
print("6. Volume of a cube")

selection=int(input("Enter choice:"))

if selection==1:
         PI = 3.14
         radius = float(input(' Please Enter the radius of a circle: '))
         area = PI * radius * radius
         print(" Area Of a Circle = %.2f" %area)

    
elif selection==2:
         width = float(input('Please Enter the Width of a Rectangle: '))
         height = float(input('Please Enter the Height of a Rectangle: '))
         Area = width * height
         print("\n Area of a Rectangle is: %.2f" %Area)
elif selection==3:
    a = float(input('Enter the length of first side: '))  
    b = float(input('Enter  the length of second side: '))  
    c = float(input('Enter  the length of third side: '))  
    s = (a + b + c) / 2  
    Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
    print('The area of the triangle is %0.2f' %Area)

elif selection==4:
    PI = 3.14
    height = float(input('Height of cylinder: '))
    radian = float(input('Radius of cylinder: '))
    volume = PI * radian * radian * height
    print("Volume is: ", volume)

elif selection==5:
    PI = 3.14
    radius = float(input('Please Enter the Radius of a Sphere: '))
    Volume = (4 / 3) * PI * radius * radius * radius
    print("\n The Volume of a Sphere = %.2f" %Volume)

elif selection==6:
    l = float(input('Please Enter the Length of any Side of a Cube: '))
    Volume = l * l * l
    print(" Volume of cube = %.2f" %Volume)
else:
    print("invalid input") """


""" x_coordinates = float(input("X_coordinates :"))

y_coordinates = float(input("Y_coordinates :"))

if x_coordinates > 0 and y_coordinates >0:
          print("1st Quadrant")
elif x_coordinates<0 and y_coordinates>0:
          print("2nd Quadrant")
elif x_coordinates<0 and y_coordinates<0:
         print("3rd Quadrant")
elif x_coordinates>0 and y_coordinates<0:
          print("4th Quadrant")
elif x_coordinates == 0 and y_coordinates==0:
          print("Origin")
elif y_coordinates==0 and x_coordinates!=0:
          print("X Axis")
elif x_coordinates==0 and y_coordinates!=0:
          print("Y Axis")  
else:
          print("Exit")     """


x_side = float(input("First Side :"))

y_side = float(input("Second Side :"))

z_side = float(input("Third Side :"))

if (x_side*x_side+y_side*y_side==z_side*z_side) or (z_side*z_side+y_side*y_side==x_side*x_side) or (x_side*x_side+z_side*z_side==y_side*y_side) :

        print("right triangle")

else:
        print("not right triangle") 


    
    
    


   

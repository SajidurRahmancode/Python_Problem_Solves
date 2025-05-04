#Area of an Equilateral Triangle
""" 
import math

side = float(input('Please Enter Length of any side of Triangle: '))

Area = (math.sqrt(3)/ 4)*(side * side)

print("Area of Equilateral Triangle = %.2f" %Area)

 """


""" 
#height of user meter to feet

user_height_meter=float(input('Your height in meter:'))


user_heightin_feet= user_height_meter * 3.280


print("user height in feet = %.2f" %user_heightin_feet) """

""" 
temp_in_f=float(input('tempreture in Fahrenheit:'))

celsius = (5.0/9.0)*(temp_in_f - 32)

kelvin = celsius + 273.15

print("Temp in celcius = %.2f" %celsius)
print("Temp in kelvin = %.2f" %kelvin)
 """

""" 
number = int(input("Please Enter any Number: "))

last_digit = number % 10

print("The Last Digit in a Given Number %d = %d" %(number, last_digit))  """
""" 

#Take an integer number
a = int(input("An integer:"))
#Convert the number in to String
b = str(a)
#Reverse the string and store it in b
b = b[::-1]
#Convert string to Integer
a = int(b)
#Print the reverse integer
print("The reverse integer number is: ",a) """

''' 
days = int(input("Enter number of days "))

years = int (days/ 365)
days1 = int(days % 365)
months = int(days1 / 30)
days2 =  int(days1 % 30)


print("years ", years)
print("months ", months)
print("days ", days2)
 '''
''' 

#area of Trapezoid


a_base=float(input("base1:"))
b_base=float(input("base2:"))
height=float(input("height:"))

Area = (a_base+b_base)/2 * height

print(Area)
 '''

 #decimal number

''' 
decimal=float(input("decimal number:"))


print("Binary to decimal: ", int(decimal))

decimal_part=decimal%1
print("Binary to decimal: ",decimal_part)

 '''
''' 
import math

num =float(input("number:"))


separated_num = math.modf(num)

#print("Binary to decimal: ", int(num))

#print("{0:.2f}".format(separated_num)) 

print("separated_num: ",separated_num)
 '''
''' 
hours = int(input("number of hours "))

days1 = hours / 24;
hours2 = hours %24;   
weeks = days1 / 7;

print("Weeks ", weeks)
print("Days remaining  ", days1)
print("Hours remaining  ", hours2)
 '''



num1 = 5
num2 = 7
 
print ("Before swapping: ")
print("Value of num1 : ", num1, " and num2 : ", num2)
 
num1, num2 = num2, num2
 
print ("After swapping: ")
print("Value of num1 : ", num1, " and num2 : ", num2)

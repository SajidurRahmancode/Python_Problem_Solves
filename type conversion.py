# Python program to demonstrate
# implicit type Casting

# Python automatically converts
# a to int
a = input("value of a:")
print(type(a))

# Python automatically converts
# b to float
b = input("value of b:")
print(type(b))

# Python automatically converts
# c to int as it is a floor addition
c = a + b
print(c)
print(type(c))

# Python automatically converts
# c to int as it is a floor multiplication
d = a * b
print(d)
print(type(d))

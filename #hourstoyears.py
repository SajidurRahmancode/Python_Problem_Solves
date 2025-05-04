#No.12 and No.14    
# Year = y, Month = m,Weeks = w,  days = d, Hours = h ;

x= int ( input("Enter number in hours:"))
y= int (x/8760)
m= int (x%8760)
m1= int (m/720)
w= int (m%720)
w1= int (w/168)
d= int (w%168)
d1= int (d/24)
h= int (d%24)
h1= int (h/1)

print(f"{y} {m1} {w1} {d1} {h1} ")


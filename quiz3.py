list = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for row in list:
  for i in range (len(row)):
    row[i]=row[i]**2
    
for row in list:
   for b in row:
      print(b,end = " ")
   print()
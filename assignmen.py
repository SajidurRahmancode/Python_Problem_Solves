""" 
a=input("enter:")
b=input("enter:")
c=int(a)+int(b)

#print("value is:{0}".format(c))


print("{0}+{1}={2}".format(a,b,c)) """


""" Price = int(input("price _of_the_fruit:"))
Item = input("Name_of_the_item:")  
Amount = int(input("How many bananas do you wish to buy: "))
Total=Price * Amount
print('{0} {1} will cost {2} taka'.format(Amount, Item, Total)) """


""" 
Item="banana"
Amount = float(input("How many bananas do you wish to buy: "))
Price = int(input("Price of bananas: "))
Total=Price * Amount

print('{0} {1} will cost {2} taka'.format(Amount, Item, Total)) """



""" 

price=5
item="banana"
amount=float(input("how many"))

total=price*amount

print('{0}{1}{2}'.format(total,amount,item)) """
""" 
#id:2120352 
item=input("which item do you want to buy?:")
price=int(input("price of {0}".format(item)))
amount=float(input("how many item do you wish to buy"))
total=price*amount
print('{0}{1} will cost{2}taka'.format(amount,item,total)) """

""" Item = input("Which item do you want to buy?: ")
Price = float(input("Price of {0}: ".format(Item)))
Amount = float(input("Weight of {0}: ".format(Item)))
Total=Price * Amount
print('{0} {1} will cost {2} taka'.format(Amount, Item, Total)) """



print('{0}{1}will cost{2:.f}taka'.format(amount),item,total)
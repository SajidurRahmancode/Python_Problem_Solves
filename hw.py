list=["01","banana",5.00,"unit","02","mango",20.00,"kg","03","apple",15.00,"kg","04","papaya",25.00,"unit","05","guava",15.00,"kg"]

print("price list:")
print("-----------")
print("item no item name price")

for i in range(0,20,4):
    print("{0:7}  {1:9} {2:5}".format(list[i],list[i+1],list[i+2]))
    print("\n")

item=int(input("which item you want to buy:"))

price_index= item+ 1

price =list[price_index]

unit_index=item+2
unit =list[unit_index]

if unit =="unit":
    amount=int(input("how many {0}:".format(item)))
elif unit=="kg":
    amount=float(input("weight of {0}:".format(item)))


print(amount)

if amount>1:
    unit=unit+"s"

amount_price=price*amount
vat=amount_price*.1 
total =amount_price+vat
print("\n")


print("{0}{1}of{2} will cost {3:.2f} taka".format(amount,unit,item,amount_price))

print("vat (10%)={0:20.2f} taka".format(vat))
print("total price ={0:20.2f} taka".format(total))
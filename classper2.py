#class performance3

appamount=int(input("enter amount of apple in kg:"))
oraamount=int(input("enter amount of orange in kg:"))
bananaamount=float(input("enter amount of banana in dozen:"))
mangamount=int(input("enter amount of mango in kg:"))
oilamount=int(input("enter amount of oil in litre:"))

apple=120*appamount
orange=150*oraamount
banana=60*bananaamount
mango=80*mangamount
oil=110*oilamount
tax=0.15




total=apple+orange+banana+mango+oil

gross_payable=total+(total*tax)





print("total price without vat",int(total))
print("with vat",int(gross_payable))



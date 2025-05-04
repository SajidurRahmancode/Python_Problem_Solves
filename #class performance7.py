l = [["01","Bananu",5.00,"unit"],["02","Mango",20.00,"Kg"],["03","Apple",15.00,"Kg"],["04","papaya",25.00,"Unit"],["05","Guava",15.00,"Kg"]]
o = 10
while o!= '0':
    print("What do You want :")
    print("1->ADD item :")
    print("2->Price List")
    print("3->Exit")
    o = input("Select :")
    if o=='1':
        id = input("Item ID :")
        n = input("Item Name :")
        p = float(input("Item Price :"))
        u = input("Unit/KG")
        ni [id,n,p,u]
        l.append(ni)
        print("Item Inserted")
    elif o=='2':
        print("Price List :")
        print("..................")
        print("Item NO Item Name Price Sold by")
        for i in range(0,len(l)):
            print("{0:7} {1:9} {2:5} {3:4} ".format(l[i][0],l[i][1],l[i][2],l[i][3]))
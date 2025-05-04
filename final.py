Account_details = [["1011047", "Md. Abrar Hossain", 39000, "1234"],["1011048", "Rabeya Ahmed", 19000, "1235"],["1011049", "Ashraf Uddin", 38000, "1236"],["1011050", "Tawsifur Rahman", 9000, "1237"],["1011051", "Synthia Choudhury", 53000, "1238"],["1011052", "Rajib Halder", 11000, "1239"],["1011053", "Shojib Das ", 29000, "1240"],["1011054", "Abdur Rab", 55000, "1241"],["1011055", "Shanjidur Rahman", 62000, "1242"],["1011056", "Shahnaz Choudhury", 61000, "1243"]]

# checking login credentials
def login():
      chk = "true"    
 print("Welcome to IUB student savings bank")    
 while chk == "true" or chk == "fail":        
   if chk == "fail":            
     print("Incorrect credentials, please try again.")            
     print("\n")        
     acc_id = input("Enter your account number: ")        
     pin = input("Enter your pin: ")        
     for i in range(len(Account_details)):            
       if acc_id == Account_details[i][0] and pin == Account_details[i][3]:                
         print("\n")                
         print("Login Successful.")                
         print("\n")                
         print("Welcome,", Account_details[i][1])                
         chk = "False"                
         return i            
         else:                
           chk = "Fail"

def check_balance(ind_1):  # define check_balance function    print("Your current balance is {}tk".format(Account_details[ind_1][2]))

def withdrawal(ind_2):  # define withdrawal function    amount = int(input("Enter the amount you want to withdraw: (min 1000, max 10000) \n "))    if Account_details[ind_2][2] < amount:  # if account doesn't have enough money        print("Insufficient funds.")    elif amount < 1000 or amount > 10000:  # if amount is more/less than the withdrawal limit        print("Amount is not within limit")    else:  # if withdrawal conditions are met        calculate = Account_details[ind_2][2] - amount        print("Your new balance will be ", calculate, "tk")        confirm = input("Would you like to proceed? (y/n) ")        if confirm == "y" or confirm == "Y":  # confirmation for withdrawal            Account_details[ind_2][2] = calculate            print("\n")            print("Withdraw Successful.")        else:  # withdrawal cancelled            print("\n")            print("Withdraw cancelled.")

def deposit(ind_3):  # define deposit function    amnt = int(input("Enter the amount you want to deposit: (min 1000, max 10000) \n "))    if 1000 <= amnt <= 10000:  # if amount is within the deposit limit        calc = Account_details[ind_3][2] + amnt        print("Your new balance will be ", calc, "tk")        conf = input("Would you like to proceed? (y/n) ")        if conf == "y" or conf == "Y":  # confirmation for deposit            Account_details[ind_3][2] = calc            print("\n")            print("Deposit successful.")        else:  # deposit cancelled            print("\n")            print("Deposit cancelled.")    else:  # if amount is more/less than the deposit limit        print("Amount is not within limit")

indx = login()  # deposit cancelledoption = 10
while option != 0:  # loop till logging out    
  # Display the menu    
  print("What do you wish to do?")    
  print("1 -> Check your balance")    
  print("2 -> Withdraw cash")    
  print("3 -> Deposit cash")    
  print("0 -> Logout")    
  print("\n")    
  option = int(input("Select option: "))    
  if option == 0:  # logout        
    print("Thank you for using IUB student savings bank.")        
    check = "unlogged"    
    elif option == 1:  # call the check_balance function        
    check_balance(indx)        
    print("\n")    
    elif option == 2:  # call the withdrawal function       
      withdrawal(indx)        
      print("\n")    
      elif option == 3:  # call the deposit function        
        deposit(indx)       
         print("\n")    
         else:  # wrong option        
           print("Incorrect selection")        
           print("\n")
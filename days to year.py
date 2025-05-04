
days = int(input("Enter num of days "))

years = int (days/ 365)
days1 = int(days % 365)
months = int(days1 / 30)
days2 =  int(days1 % 30)

print("Remaining days ", days2)
print("Remaining years ", years)
print("Remaining months ", months)

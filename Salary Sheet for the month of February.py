# Salary Sheet for the month of February 2021

Hours_served =int(input("Number of hours student served  : "))

rate_per_hour=100

total =Hours_served*rate_per_hour

tax_detuctable=100/10

tax=total/tax_detuctable

Gross_Payable=total-tax

print("Salary Sheet for the month of February 2021")

print("-----------------------------------------")

print("Hours_served\t\t\t:\t  ",Hours_served)

print("rate_per_hour\t\t\t:\t ", rate_per_hour )

print("-----------------------------------------")

print("total\t\t\t\t:\t", total )

print("-10%_tax_amount\t\t\t:\t-",int(tax) )

print("-----------------------------------------")

print("Gross_payable\t\t\t:\t",int(Gross_Payable))

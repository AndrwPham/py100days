bill = float(input("Enter the total bill: "))
tip_percent = float(input("How many percent you would like to tip: 10 , 12 or 15: "))
people = int(input("How many people to split the bill: "))

splitted_bill = bill / people
each_pay = "{:.2f}".format(splitted_bill * (1 + tip_percent / 100)) #Return with 2 decimal digits

print(f"Each people pay {each_pay} for the bill")
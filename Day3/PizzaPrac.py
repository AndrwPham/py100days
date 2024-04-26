#PizzaOrder:

size = input("What size do you want? S, M or L ")
add_pepperoni = input("Do you want to add pepperoni? ")
extra_cheese = input("How about some extra cheese? ")

bill = 0
if size == "S": bill = 15
if size == "M": bill = 20
if size == "L": bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is : ${bill}")




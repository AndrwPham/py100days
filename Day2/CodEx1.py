number = (input("Pick a num: "))
char = str(number)
sum = 0

#add digits in a number

for i in char:
    sum = sum + int(i)
print(sum)

#add digits in a number
number = (input("Pick a num: "))
char = str(number)
nums = []
sum = 0
for i in char:
    sum = sum + int(i)
print(sum)

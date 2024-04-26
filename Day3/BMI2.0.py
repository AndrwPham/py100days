#Enter height
height = input("Enter height (m): ")
#Enter weight
weight = input("Enter weight (kg): ")
h = float(height)
w = float(weight)
BMI = w / (h*h)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else: 
    print(f"Your BMI is {BMI}, you are clinically obese.")
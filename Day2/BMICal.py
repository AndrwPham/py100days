#Enter height
height = input("Enter height (m): ")
#Enter weight
weight = input("Enter weight (kg): ")
h = float(height)
w = float(weight)
BMI = w / (h*h)
print("BMI = ", BMI)
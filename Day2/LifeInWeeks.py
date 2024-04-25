age = input("Enter age: ")
#Calculate how many weeks you have left within a 90 years lifespan

weeks = 90 * 52
ageInWeeks = int(age) * 52
res = weeks - ageInWeeks
print(f"You have {res} weeks left.") 

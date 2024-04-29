student_score = input().split()
highest = 0
for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
    if highest < student_score[n]:
        highest = student_score[n]
print(f"The highest score in the class is: {highest}")
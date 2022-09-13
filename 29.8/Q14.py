grades = []
sum = 0
i = 0
while len(grades) < 5:
    grade = (int(input("Enter grade")))
    if 0 <= grade <= 100:
        sum += grade
        grades.append(grade)
    else:
        print("illegal grade")
        grades.append(int(input("Enter grade")))
    i += 1
average = sum/5
print("The grades:", grades)
print("The average:", average)

new_average = 0
for i in range(5):
    if grades[i] > 90:
        grades[i] = 100
        new_average += grades[i]
    elif 80 <= grades[i] <= 90:
        grades[i] += 10
        new_average += grades[i]
    elif 60 <= grades[i] <= 80:
        grades[i] += 7
        new_average += grades[i]
    else:
        grades[i] += 5
        new_average += grades[i]

grades.sort()
print("The new grades:", grades)
print("The new average:", new_average/5)





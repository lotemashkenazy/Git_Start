grade = int(input("enter grade:"))
sum = 0
count_of_grades = 0
while grade != -1:
    sum += grade
    count_of_grades += 1
    grade = int(input("enter grade:"))
print(sum/count_of_grades)

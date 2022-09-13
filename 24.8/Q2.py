programming_grade = int(input("enter grade in programming- 0-10:"))
math_grade = int(input("enter grade in math- 0-10:"))
teamwork_grade = float(input("enter grade in teamwork- 0-7.5:"))

if programming_grade >= 9 and math_grade >= 9 and teamwork_grade >= 6:
    print("CLASS_A")
elif programming_grade >= 8 and math_grade >= 7 and teamwork_grade > 5.5:
    print("CLASS_B")
elif programming_grade >= 6 and math_grade+teamwork_grade >= 10/3:
    print("CLASS_C")
elif teamwork_grade > programming_grade or teamwork_grade > math_grade:
    print("CLASS_D")
else:
    print("Maybe next summer")

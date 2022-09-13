num1 = int(input("please enter a positive number:"))
num2 = int(input("please enter a positive number:"))
action = input("please enter the action- */+-")

if action == '+':
    print(num1+num2)
if action == '-':
    if num1-num2 > 0:
        print(num1-num2)
    else:
        print("the solution is negative")
if action == '/':
    if num1 == 0 or num2 == 0:
        print("can't divide by 0")
    else:
        print(num1/num2)
if action == '*':
    print(num1*num2)



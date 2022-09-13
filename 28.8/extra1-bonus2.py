num = int(input("please enter a range:"))
digit = int(input("please enter a number:"))
for i in range(1, num+1):
    if i % digit == 0:
        print("boom")
    elif str(digit) in str(i):
        print("boom")
    else:
        print(i)
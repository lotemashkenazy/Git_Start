num = int(input("please enter a range:"))
for i in range(1, num+1):
    if i % 7 == 0:
        print("boom")
    elif "7" in str(i):
        print("boom")
    else:
        print(i)
num = int(input("enter a number:"))
sum = 0

if num > 0:
    for i in range(1, 100):
        if num % i == 0:
            print(i)
elif num < 0:
    for i in range(1, 50):
        if i % 2 == 0:
            sum += 1
    print(sum)
else:
    for i in range(20, 0, -1):
        print(i)

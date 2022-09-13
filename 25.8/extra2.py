num = int(input("enter number:"))
count_of_unique_numbers = 0

if (num < 10) or num > 100:
    print("Not in range")
else:
    if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0):
        if num % 2 == 0:
            count_of_unique_numbers += 1
        if num % 3 == 0:
            count_of_unique_numbers += 1
        if num % 5 == 0:
            count_of_unique_numbers += 1
        if num % 7 == 0:
            count_of_unique_numbers += 1
        print("the number is not a prime number. the count of unique numbers is:" , count_of_unique_numbers)
    else:
        print("the number is a prime number")
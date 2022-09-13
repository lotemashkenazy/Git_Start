my_list = [3, 7, -68, 55, 100]
num = int(input("Enter number from the list:"))
if num in my_list:
    print(my_list.index(num))
else:
    print("The number is not in the list")
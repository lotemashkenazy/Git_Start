my_list = ["orange", "banana", "apple", "kiwi"]
i = int(input("Enter i:"))
if i < len(my_list):
    temp = my_list[i]
    my_list[i] = "pineapple"
    print(my_list)
    print(temp)
else:
    print("error")
my_list = [2, 4, 76, 198]
i = int(input("Enter i:"))
if i < len(my_list):
    num_int_list = my_list[i]
    my_list.remove(num_int_list)
    print(my_list)
else:
    print("error")

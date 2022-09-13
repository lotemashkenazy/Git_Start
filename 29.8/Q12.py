import random

my_list = [1, 2, 3, 4, 5]
new_list = []
check_list = []
while len(new_list) != len(my_list):
    index = random.randint(0, len(my_list)-1)
    if index not in check_list:
        check_list.append(index)
        new_list.append(my_list[index])
print(new_list)

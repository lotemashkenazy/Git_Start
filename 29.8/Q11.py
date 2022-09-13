#a

my_list = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
new_list = [x for x in my_list if x % 2 == 0]
print(new_list)
#b
my_list1 = [2, 3.75, 0.04, 59.354, 6, 7.777, 8, 9]
new_list1 = [x for x in my_list1 if type(x) != float]
print(new_list1)

#c
new_list = [x for x in range(1, 1001) if '3' in str(x)]
print(new_list)


first_list = ["father", "kayak", "madam", "Ronaldo", "Noa", "David"]
second_list = ["xavi", "Xman", "banana", "aoN", "madam", "kayak"]

third_list = []
for i in range(len(second_list)):
    third_list.append(second_list[i][::-1])
#print(third_list)

new_list = []
for y in range(len(first_list)):
    new_list.append(first_list[y])
    new_list.append(third_list[y])
#print(new_list)

x = 0
while x < len(new_list):
    if new_list.count(new_list[x]) > 1:
        new_list.remove(new_list[x])
    x += 1
print(new_list)
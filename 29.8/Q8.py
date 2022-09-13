my_list = ["o", "hat", "aba", "1221", "umbrella", "pickup", "22.3.22"]
for i in my_list:
    if len(i) > 1 and i[0] == i[-1]:
        print(i)
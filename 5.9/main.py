import ArithmeticProg

firs_num = int(input("Enter the first num:"))
step = int(input("Enter the step:"))
num_of_steps = int(input("Enter the number of steps:"))

sum_first_nth = ArithmeticProg.sum_n_items(firs_num, step, num_of_steps)

print(sum_first_nth)
the_n_item = ArithmeticProg.nth_item(firs_num, step, num_of_steps)
for i in range(the_n_item):
    if i % 2 == 0:
        print(i)

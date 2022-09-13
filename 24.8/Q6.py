sum_of_money =int(input("please enter your sum of money in the bank:"))
num_of_stocks = int(input("please enter the number of stocks you want to buy:"))

if 1 <= sum_of_money <= 10000:
    if 1 < num_of_stocks <= 500:
        print("The total amount to pay for the stocks is: ", 1.5+0.8)
    elif 500 < num_of_stocks:
        print("The total amount to pay for the stocks is: ", 1.5+0.7)
elif 10000 < sum_of_money <= 50000:
    if 1 < num_of_stocks <= 250:
        print("The total amount to pay for the stocks is: ", 1.3+0.4)
    elif 250 < num_of_stocks:
        print("The total amount to pay for the stocks is: ", 1.3+0.3)
elif 50000 < sum_of_money:
    print("The total amount to pay for the stocks is: ", 1.1+0.1)

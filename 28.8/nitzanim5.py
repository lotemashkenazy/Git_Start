payment = 0
num_of_people = 0
for i in range(10):
    if payment <= 300:
        payment += int(input("How much do you want to pay?"))
        num_of_people += 1
    else:
        break
if payment < 300:
    print("We didn't reach the amount needed. All friends payed.")
if payment >= 300:
    print("We reached the amount needed.", num_of_people, "payed.")

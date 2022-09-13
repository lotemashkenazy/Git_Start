large_orders = 0
for i in range(5):
    name = input("Enter the name of the customer")
    num_of_boxes = int(input("Enter the number of boxes:"))
    payment_amount = 25 * num_of_boxes
    if num_of_boxes < 3:
        payment_amount += 20
    if num_of_boxes > 20:
        large_orders += 1
    print(name, "need to pay", payment_amount)
print("The number of large orders is", large_orders)

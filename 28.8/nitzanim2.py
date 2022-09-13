sum_of_length = 0
names = ""
for i in range(5):
    name = input("enter the name:")
    length = float(input("enter the length:"))
    sum_of_length += length
    if length > 15:
        names += str(name + " ")
print("The total length of the Israel Trail is:", sum_of_length , "km")
print("The names of the trails that are longer than 15 kilometers:", names)
days_stated = int(input("enter number of days stated in hotel:"))
num_of_guests = int(input("enter number of guests:"))
room_type = input("enter room type- S/C:")

if (days_stated >= 1) and (days_stated <= 7):
    if room_type == 's' and num_of_guests > 4:
        print("You get 100 days!")
    elif room_type == 'c' and num_of_guests > 6:
        print("You get 200 days!")
elif (days_stated >= 8) and (days_stated <= 14):
    if room_type == 's' and num_of_guests > 3:
        print("You get 300 days!")
    elif room_type == 'c' and num_of_guests > 5:
        print("You get 400 days!")
elif days_stated >= 15:
    print("You get forever!")









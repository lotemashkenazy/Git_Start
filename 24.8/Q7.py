name = input("enter the new employee's name:")
ddmm = int(input("enter the new employee's birthday:"))

dd = ddmm // 100
mm = ddmm % 100

if ((mm == 1) or (mm == 3) or (mm == 5) or (mm == 7) or (mm == 8) or (mm == 10) or (mm == 12)) and 1 <= dd <= 31:
    print(name, "birthday is on ", dd, "/", mm)
elif ((mm == 4) or (mm == 6) or (mm == 9) or (mm == 11)) and 1 <= dd <= 30:
    print(name, "birthday is on ", dd, "/", mm)
elif mm == 2 and 1 <= dd <= 28:
    print(name, "birthday is on ", dd, "/", mm)
else:
    print("illegal date")
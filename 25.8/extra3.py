name1 = input("enter your name:")
name2 = input("enter your name:")

name1_lower = name1.lower()
name2_lower = name2.lower()

if name1_lower == name2_lower:
    print("not related")
else:
    family_name1_A = input("enter your family name (from parent a)")
    family_name2_A = input("enter your family name (from parent a)")
    if family_name1_A == family_name2_A:
        print("related")
    else:
        family_name1_B = input("enter your family name (from parent b)")
        family_name2_B = input("enter your family name (from parent b)")
        if family_name1_B == family_name2_B:
            parentB_1 = input("enter your parent (b) name")
            parentB_2 = input("enter your parent (b) name")
            if parentB_1 == parentB_2:
                print("not related")
            else:
                print("related")
        else:
            print("not related")
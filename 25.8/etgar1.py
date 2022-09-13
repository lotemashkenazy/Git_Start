print('the password must be at least 6, and no more than 15 characters long')

password = input('enter your password:')

if len(password) > 15:
    print('password is too long It must be between 6 and 15 characters')
elif len(password) < 6:
    print('password is too short It must be between 6 and 15 characters')
elif (len(password) >= 6) and (len(password) <= 15):
    digit=0
    big_letters=0
    small_letters=0
   for i in range(password):
        digit += 1
        password[i].isdigit()
        if True:
            big_letters+=1
            password.isupper()
            if True:
                small_letters += 1
                password.islower()


    if (password.islower()) and (password.isupper()) and (password.isdigit()):
        print('password ok. the password is:', password)
    else:
        print('password is too weak, It must be including numbers, big letters and small letters ')
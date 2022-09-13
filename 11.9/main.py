import os
import legitimate_behaviors
import behaviors
import util

file_path = input("Enter Folder Path:")
# C:\\Users\\User\\Desktop\\11.9
path_list = os.listdir(file_path)
users_list = behaviors.read_many_text_file(file_path, path_list)
new_users_list = behaviors.create_dicts_list1(users_list)
print(new_users_list)
print()

file_path_2 = input("Enter Folder Path:")
# C:\Users\User\Desktop\valid.txt
users_list2 = legitimate_behaviors.read_text_file(file_path_2)
new_users_list2 = legitimate_behaviors.create_dicts_list(users_list2)
print(new_users_list2)


for i in range(len(new_users_list)):
    user_behavior = new_users_list[i]
    for j in range(len(new_users_list2)):
        right_behavior = new_users_list2[j]

        if user_behavior["Action"] == 'Log In':
            if user_behavior["User"] == right_behavior["User"]:
                legitimate_time = right_behavior["legitimate time"].split("-")
                hour1 = float(legitimate_time[0].replace(':', '.'))
                hour2 = float(legitimate_time[-1].replace(':', '.'))
                user_time = float(user_behavior["Time"].replace(':', '.'))

                if (user_behavior["IP Address"] != right_behavior["IP Address"]) and \
                        ((user_time < hour1) or (user_time > hour2)):
                    util.alert_suspicious(user_behavior["User"] + " from " + user_behavior["IP Address"],
                                          "Wrong Time & Address")
                elif (user_time < hour1) or (user_time > hour2):
                    util.alert_suspicious(user_behavior["User"] + " from " + user_behavior["IP Address"], "Wrong Time")
                elif user_behavior["IP Address"] != right_behavior["IP Address"]:
                    util.alert_suspicious(user_behavior["User"] + " from " + user_behavior["IP Address"],
                                          "Wrong IP Address")

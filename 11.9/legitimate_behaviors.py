
def read_text_file(file_path):
    users_lst = []
    with open(file_path) as f:  # First, open a text file for reading
        for j in range(7):
            users_lst.append(f.readline())
            # print(f.readline())  # Second, read text from the text file
    return users_lst


def create_dicts_list(old_lst):
    new_users_lst = []
    for i in range(len(old_lst)):
        split_lst = old_lst[i].split(" ")
        user_dict = {"User": split_lst[0],
                      "IP Address": split_lst[1],
                      "legitimate time": split_lst[2].replace("\n", "")
                      }
        new_users_lst.append(user_dict)
    return new_users_lst
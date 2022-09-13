def read_many_text_file(file_path, path_list):
    users_lst = []
    for file in path_list:
        path1 = file_path + "\\" + file
        with open(path1) as f:  # First, open a text file (for reading)
            for line in f:
                users_lst.append(line.strip())
    return users_lst



def split_list(old_lst, action):
    split_lst = []
    for i in range(len(old_lst)):
        split_lst.append(old_lst[i].split(action))
    return split_lst


def create_flat_list(old_lst):
    split_lst = split_list(old_lst, ": ")
    # flat_list = [item for sublist in l for item in sublist]
    flat_list = []
    for sublist in split_lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def create_dicts_list1(old_lst):
    flat_list = create_flat_list(old_lst)
    new_users_lst = []
    times_run = 0
    for j in range(20):
        user_dict = {}
        for i in range(4):
            one_user = {flat_list[times_run]: flat_list[times_run + 1]}
            user_dict.update(one_user)
            times_run += 2
        new_users_lst.append(user_dict)
    return new_users_lst

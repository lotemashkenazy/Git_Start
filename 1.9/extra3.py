def new_students(list_new_students, reformat = True):
    if reformat == True:
        for j in range(len(list_new_students)):
            list_new_students[j] = list_new_students[j].title()
            #list_new_students[j] = list_new_students[j].replace(" ", "-")

            list_new_student = list(list_new_students[j])
            counter = 0
            for i in range(len(list_new_student)):
                if list_new_student[i] == " ":
                    counter += 1
                    if counter > 1:
                        list_new_student[i] = "-"
            list_new_student = ''.join(list_new_student)
            list_new_students[j] = list_new_student

    return list_new_students

def all_students(list_old_students, list_new_students):
    list2_new_students = new_students(list_new_students, reformat = True)
    list_all_students = list2_new_students + list_old_students
    list_all_students.sort()
    return list_all_students

list_new_students = ["avi cohen marhi", "aki ploob", "pini levi", "lotem ashkenazy ben david"]
list_old_students = ["Aaron Cotton", "Aki Ploob", "Zina Ashkara"]
print("the new students:", new_students(list_new_students))
print("the old students:", list_old_students)
print("all the students in the school now:", all_students(list_old_students, list_new_students))
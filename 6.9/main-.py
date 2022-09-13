import module_costants

#
def building_schedule():
    # relevant constant
    amount_of_days = module_costants.amount_of_days
    hours_per_day = module_costants.hours_per_day + 1
    DAY_LIST = module_costants.DAY_LIST
    schedule = module_costants.schedule
    # Initializing the schedule
    lst = []
    for row in range(hours_per_day):                     #שורה- שעות
        for col in range(amount_of_days):               #תור - ימים
            if row == 0:
                lst.append(DAY_LIST[col])
            else:
                lst.append("Free")
        schedule.append(lst)
        lst = []

    return schedule

#
def print_schedule(schedule):
    print()
    for row in range(len(schedule)):
        for col in range(len(schedule[row])):
            print(schedule[row][col], end=' ')
        print()
    print()

# step 2
def create_lessons_list():
    lessons_list = []
    lesson = input("Enter - [name_of_lesson]_[lesson_duration]_[day_lesson]_[hour_lessson]:")

    while lesson != 'done':
        lesson = lesson.split("_")
        lessons_list.append(lesson)                         #create list of all the lessons
        lesson = input("Enter - [name_of_lesson]_[lesson_duration]_[day_lesson]_[hour_lessson]:")

    return lessons_list

# step 3
def placement_lessons_in_schedule(lessons_outside_schedule):
    lessons_list = create_lessons_list()
    schedule = building_schedule()
    DAY_LIST = module_costants.DAY_LIST
    count = 0

    for i in range(len(lessons_list)):
        lesson = lessons_list[i]
        name_of_lesson = lesson[0]
        lesson_duration = int(lesson[1])
        day_lesson = lesson[2].lower()
        hour_lessson = int(lesson[3]) - 7

        check_true = 0
        # change the word day to the index of the day in the schedule
        for day in range(len(DAY_LIST)):
            if day_lesson == DAY_LIST[day]:
                day_lesson = day

        check_true = check_free

        if check_true == lesson_duration:
            for j in range(lesson_duration):
                schedule[hour_lessson + j][day_lesson] = name_of_lesson
        else:
            lessons_outside_schedule.append(lesson)

    return (schedule)


# check if all the hours in the schedule are free
def check_free():
    lessons_list = create_lessons_list()
    schedule = building_schedule()
    DAY_LIST = module_costants.DAY_LIST
    count = 0
    check_true = 0
    for i in range(len(lessons_list)):
        lesson = lessons_list[i]
        lesson = lessons_list[i]
        name_of_lesson = lesson[0]
        lesson_duration = int(lesson[1])
        day_lesson = lesson[2].lower()
        hour_lessson = int(lesson[3]) - 7
        for hour in range(lesson_duration):
            if hour_lessson + hour > schedule.index(schedule[-1]):
                count += 1
                break
            elif schedule[hour_lessson + hour][day_lesson] == "Free":
                check_true += 1
    if count > 0:
        print("A schedule cannot be built")
    else:
        return check_true


# step4
def placement_outside_lessons():
    lessons_outside_schedule = []
    schedule = placement_lessons_in_schedule(lessons_outside_schedule)
    print(lessons_outside_schedule)
    count1 = 0

    for i in range(len(lessons_outside_schedule)):
        lesson = lessons_outside_schedule[i]
        name_of_lesson = lesson[0]
        lesson_duration = int(lesson[1])

        for row in range(len(schedule)):
            for col in range(len(schedule[row])):

                check_true = 0
                # check if all the hours in the schedule are free
                check_true = check_free()
                if check_true == lesson_duration:
                    for j in range(lesson_duration):
                        schedule[row + j][col] = name_of_lesson
                    lessons_outside_schedule.remove(lesson)
                    lessons_outside_schedule.insert(i, 0)
                    break
                if lesson not in lessons_outside_schedule:
                    break
            if lesson not in lessons_outside_schedule:
                break
    count = 0
    for check0 in range(len(lessons_outside_schedule)):
        if lessons_outside_schedule[check0] != 0:
            print("A schedule cannot be built")
            break
        else:
            count += 1
    if count == len(lessons_outside_schedule) or count1 > 0:
        print_schedule(schedule)

lessons_outside_schedule = []
#placement_outside_lessons()
print_schedule(placement_lessons_in_schedule(lessons_outside_schedule))

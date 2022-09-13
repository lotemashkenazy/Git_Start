#a
# id_name_dict = {
#     "209857483": "Dan",
#     "348573485": "Shir",
#     "3294850695": "Rotem",
#     "291029485": "Mai",
#     "245769202": "Noam",
#     "294850394": "Matan"
# }
id_name_dict = {
    "1": "Dan",
    "2": "Shir",
    "3": "Rotem",
    "4": "Mai",
    "5": "Noam",
    "6": "Matan"
}

name_grade_dict = {}

while len(name_grade_dict) != len(id_name_dict):
    id = input("Enter id:")
    grade = input("Enter grade:")
    if id in id_name_dict:
        name_grade_dict.update({id_name_dict[id]: grade})

print(name_grade_dict)
print()

#b
name_grade_list = list(name_grade_dict.items())
key_list = list(id_name_dict.keys())
id_name_grade = {}

for i in range(len(id_name_dict)):
    id_name_grade.update({key_list[i]: name_grade_list[i]})

print(id_name_grade)
# for key, value in id_name_grade.items():
#     print(key, ' : ', value)
# print()
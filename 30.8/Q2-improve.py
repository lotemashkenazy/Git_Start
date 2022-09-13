import collections

#a
id_name_dict = {
    "1": "Dan",
    "2": "Shir",
    "3": "Rotem",
    "4": "Mai",
    "5": "Noam",
    "6": "Matan"
}

name_grade_dict = {}        #a
id_name_grade = {}          #b
name_id_grade = {}          #c

while len(name_grade_dict) != len(id_name_dict):
    id = input("Enter id:")
    grade = input("Enter grade:")

    if id in id_name_dict:
        name_grade_dict.update({id_name_dict[id]: grade})            #a
        id_name_grade.update({id: [id_name_dict[id], grade]})        #b
        name_id_grade.update({id_name_dict[id]: [id, grade]})        #c
#a
print(name_grade_dict)
print()

#b
for key, value in id_name_grade.items():
    print(key, ' : ', value)
print()

#c
name_id_grade = dict(sorted(name_id_grade.items()))
print(name_id_grade)

for key, value in name_id_grade.items():
    print(key, ' : ', value)
print()


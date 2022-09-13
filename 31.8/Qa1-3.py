#1
def sum_of_list(list1):
    sum= 0
    for i in range(len(list1)):
        sum += list1[i]
    return sum
#print(sum([1,2,3,4,5]))

#2
def double_num(list2):            #cheking if their double
    x = 0
    while x < len(list2):
        if list2.count(list2[x]) > 1:
            list2.remove(list2[x])
        x += 1
    return list2

#print(double_num([1, 1, 2]))

#3
def find_max_substring(word, word_list):
    max_len = 0
    for this_word in word_list:
        temp_indx = 0
        counter = 0
        for i in range(len(this_word)):
            for j in range(temp_indx, len(word)):
                if this_word[i] == word[j]:
                    temp_indx = j
                    counter += 1
                    break
        if counter == len(this_word):
            if counter > max_len:
                max_len = counter
    return max_len


word = "computer"
word_list = ["com", "pmo", "cpter", "cpmuter"]
max_len = find_max_substring(word, word_list)
print("Length of the longest substring:", max_len)

def max(list_numbers):
    max = 0
    for i in range(len(list_numbers)):
        if list_numbers[i] > max:
            max = list_numbers[i]
    return max

list_numbers = 1,7,3
print(max(list_numbers))
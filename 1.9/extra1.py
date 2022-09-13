def multiplyList(tuple):
    result = 1
    for i in tuple:
        result = result * i
    average = result ** (1/len(tuple))
    return average

tuple = (2,2,3)
print(multiplyList(tuple))
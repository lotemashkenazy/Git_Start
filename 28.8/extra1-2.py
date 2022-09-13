n=int(input('Please enter a positive integer between 1 and 10: '))
solution_str = ""
while n != -1:
    for row in range(1,n+1):
        solution_str = ""
        for col in range(1,n+1):
            solution = row*col
            solution_str += (str(solution) + "\t")
        print(solution_str)
    n=int(input('Please enter a positive integer between 1 and 10: '))

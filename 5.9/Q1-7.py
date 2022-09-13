# Q1- print matrix
def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=' ')
        print()

# Q2- print the sum of all the numbers in the matrix
def sum_matrix(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            sum += matrix[row][col]
    return (sum)

# Q3- print the sum of all the numbers in the matrix in the cross
def sum_matrix_in_cross(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == col:
                sum += matrix[row][col]
    return (sum)

# Q4- switch in the matrix between the invited that left to the new invited
def switch_members(lefft_VIP, new_VIP, matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == lefft_VIP:
                matrix[row][col] = new_VIP
            print(matrix[row][col], end=' ')
        print()

# Q5- create a matrix by the difference (row-col)
def matrix_by_diff(size):
    sum = 0
    matrix = []
    lst = []
    for row in range(size):
        for col in range(size):
            sum = row - col
            if sum < 0:
                sum = 0
            lst.append(sum)
        matrix.append(lst)
        lst = []

    return matrix

# Q5
def matrix_by_diff2(size):
    matrix2 = [[(0 if row-col<=0 else row-col) for col in range(size)] for row in range(size)]
    return matrix2


# Q6
def find_bad_tv(tv):
    list_of_tupples = []
    for row in range(len(tv)):
        for col in range(len(tv[row])):
            if tv[row][col] == "problem":
                list_of_tupples.append((row, col))
    return list_of_tupples


#########################################################

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
    ]

# Q1-3
print(print_matrix(matrix))
print(sum_matrix(matrix))
print(sum_matrix_in_cross(matrix))


#Q4-a
matrix_invited = [ ["Ofir", "Bar", "Neta"], ["Aviram", "Ohad"], ["Moti", "Liron", "Roni"] ]
#Q4-b
print_matrix(matrix_invited)
print()
#Q4-c
lefft_VIP = input("Enter the VIP that left:")
new_VIP = input("Enter the new VIP:")
switch_members(lefft_VIP, new_VIP, matrix_invited)


#Q5
size = int(input("Enter the size of the matrix:"))
matrix_Q5 = matrix_by_diff(size)
print_matrix(matrix_Q5)
# Q5-2
size = int(input("Enter the size of the matrix:"))
matrix_Q52 = matrix_by_diff2(size)
print(matrix_Q52)
print_matrix(matrix_Q52)


#Q6
WORKING_SCREEN = "work"
FAULTY_SCREEN = "problem"
tv = [
     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]
 ]
print(find_bad_tv(tv))


#Q7
SUBMARINE = 'X'
EMPTY = 'O'
board = [
     [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
     [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY],
     [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY],
     [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY]
 ]

def check_legal_place(row, col, board):
    while (row < 0 or col < 0) or (row > 4 or col > 4):
        print("The place is illegal, try again")
        row = int(input("Enter the row:")) -1
        col = int(input("Enter the col:")) -1

def run1_game():
    row = int(input("Enter the row:")) -1
    col = int(input("Enter the col:")) -1
    tries = 1
    missing_bombs = 0

    check_legal_place(row, col, board)
    while (board[row][col] != "X"):
        missing_bombs += 1
        row = int(input("Enter the row:")) -1
        col = int(input("Enter the col:")) -1
        check_legal_place(row, col, board)
        tries += 1

    print(board[row][col])
    board[row][col] = 'O'
    print("your number of tries:", tries)
    return missing_bombs

def check_SUBMARINE(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "X":
                return True
    return False


num_of_bad_bombs = 0
while check_SUBMARINE(board) == True:
    #run1_game()
    num_of_bad_bombs += run1_game()
print()
print("Well done, you win!! The number of Bombs that went in vain:", num_of_bad_bombs)

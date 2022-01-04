########################################################################################################################

'''
    Practice 1: Create one function from the two below, using arguments
'''


def get_board():
    board = [".", ".", ".", ".", ".", ".", "."]
    return board


def move_player1():
    while True:
        board = get_board()
        p1_input = int(input("player X move [from 0 to 6]: "))
        if p1_input < len(board) and p1_input > 0:
            board[p1_input] = "X"
            print(board)
            break
        else:
            print("Invalid input, please try again: ")


def move_player2():
    while True:
        board = get_board()
        p2_input = int(input("player O move [from 0 to 6]: "))
        if p2_input < len(board) and p2_input > 0:
            board[p2_input] = "O"
            print(board)
            break
        else:
            print("Invalid input, please try again: ")


# You will need a few arguments;)
def move_player(player_mark):
    pass


print("Start of function move_player")

move_player("X")
move_player("0")


########################################################################################################################

'''
    Practice 2: Create one function from the two below, using arguments
'''

import random


def get_board1():
    return ['.','O', 'X', '.',',']


def get_board2():
    return [',','X', 'O', '.','.']


def move_AI1():
    while True:
        board1 = get_board1()
        random_index = random.randint(0, len(board1))

        if board1[random_index] == ".":
            board1[random_index] = "O"
            print(board1)
            break
        else:
            print("That cell is already occupied")


def move_AI2():
    while True:
        board2 = get_board2()
        random_index = random.randint(0, len(board2))

        if board2[random_index] == ".":
            board2[random_index] = "X"
            print(board2)
            break
        else:
            print("That cell is already occupied")


# You will need a few arguments;)
def move_AI():
    pass


print("\n\nStart of function move_AI")

# move_AI("X")
# move_AI("0")


########################################################################################################################

'''
    Practice 3: Create one single function to count even numbers and use the return statement
'''


def get_numbers():
    return [33, 24, 44, 25, 101, 1, 10]


# You will need a few arguments;)
def is_even():
    pass


def print_even_count():
    numbers = get_numbers()

    # Use a function to make this simpler
    even_count = 0
    if numbers[0] % 2 == 0:
        even_count += 1
    if numbers[1] % 2 == 0:
        even_count += 1
    if numbers[2] % 2 == 0:
        even_count += 1
    if numbers[3] % 2 == 0:
        even_count += 1
    if numbers[4] % 2 == 0:
        even_count += 1
    if numbers[5] % 2 == 0:
        even_count += 1
    if numbers[6] % 2 == 0:
        even_count += 1

    print('From the', str(numbers), 'items, there are ' + str(even_count) + ' items which are divisible by 2')


print("\n\nStart of function print_even_count")

print_even_count()


########################################################################################################################
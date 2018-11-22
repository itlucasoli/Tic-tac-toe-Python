game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]


def player(turn):
    if turn % 2 == 0:
        print("O is or turn:")
        xo = "O"

    else:
        print("X is or turn:")
        xo = "X"

    row = int(input("Type where you will play (row):"))
    column = int(input("Type where you will play (column):"))

    while game_board[row][column] != "-":
        row = int(input("\nInvalid Input!\nType again where you will play (row):"))
        column = int(input("\nInvalid Input!\nType again where you will play (column):"))

    game_board[row][column] = xo


def win_verification_x(board):
    point_x = 0
    for a in range(3):  # row
        if board[a][0] == "X" and board[a][1] == "X" and board[a][2] == "X":
            print("X")
            return True

        elif board[0][a] == "X" and board[1][a] == "X" and board[2][a] == "X":
            return True

        elif board[a][a] == "X":
            point_x += 1
            if point_x == 3:
                return True

        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            return True
    return False


def win_verification_o(board):
    point_o = 0
    for a in range(3):  # row
        if board[a][0] == "O" and board[a][1] == "O" and board[a][2] == "O":
            return True

        elif board[0][a] == "O" and board[1][a] == "O" and board[2][a] == "O":
            return True

        elif board[a][a] == "O":
            point_o += 1
            if point_o == 3:
                return True

        elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            return True
    return False


def draw_verification(board):
    aux = 0
    for x in range(3):  # row
        for y in range(3):  # column
            if board[x][y] == "-":
                aux += 1
    if aux == 0:
        return True
    else:
        return False


def print_board(board):
    interface = " Game      Position \n" \
                "|{}|{}|{}|   |00|01|02|\n" \
                "|{}|{}|{}|   |10|11|12|\n" \
                "|{}|{}|{}|   |20|21|22|".format(board[0][0], board[0][1], board[0][2],
                                                 board[1][0], board[1][1], board[1][2],
                                                 board[2][0], board[2][1], board[2][2])
    print(interface)


def result():
    if win_verification_x(game_board) is True:
        print("The winner is Player X")

    elif win_verification_o(game_board) is True:
        print("The winner is Player O")

    elif draw_verification(game_board) is True:
        print("Draw!")


turn = 0
print_board(game_board)
while (win_verification_x(game_board) is False) and (win_verification_o(game_board) is False) and \
        (draw_verification(game_board) is False):
    turn += 1
    print("\n")
    player(turn)
    print("\n")
    print_board(game_board)
result()

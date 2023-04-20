board = [['-' for x in range(7)] for y in range(6)]
player = 'X'

def print_board():
    for row in board:
        print(' '.join(row))

def drop_piece(col):
    global player
    for i in range(5, -1, -1):
        if board[i][col] == '-':
            board[i][col] = player
            break

def check_win(player):
    # check horizontal
    for row in range(6):
        for col in range(4):
            if (board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player):
                return True

    # check vertical
    for row in range(3):
        for col in range(7):
            if (board[row][col] == player and
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player):
                return True

    # check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if (board[row][col] == player and
                board[row+1][col+1] == player and
                board[row+2][col+2] == player and
                board[row+3][col+3] == player):
                return True

    # check diagonal (bottom-left to top-right)
    for row in range(3):
        for col in range(4):
            if (board[row+3][col] == player and
                board[row+2][col+1] == player and
                board[row+1][col+2] == player and
                board[row][col+3] == player):
                return True

    return False

while True:
    print_board()
    col = int(input('Player ' + player + ', select column: '))
    drop_piece(col)
    if check_win(player):
        print_board()
        print('Player ' + player + ' wins!')
        break

    player = 'O' if player == 'X' else 'X'
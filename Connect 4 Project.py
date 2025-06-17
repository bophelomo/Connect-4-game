#Connect 4


ROWS = 6
COLUMNS = 7

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i) for i in range(COLUMNS)))

def drop_piece(board, column, piece):
    for row in reversed(range(ROWS)):
        if board[row][column] == " ":
            board[row][column] = piece
            return row  # return the row the piece was dropped in
    return -1  # column full

def check_direction(board, row, col, piece, delta_row, delta_col):
    count = 0
    r, c = row, col
    while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == piece:
        count += 1
        r += delta_row
        c += delta_col

    r, c = row - delta_row, col - delta_col
    while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == piece:
        count += 1
        r -= delta_row
        c -= delta_col

    return count >= 4

def check_win(board, row, col, piece):
    return (
        check_direction(board, row, col, piece, 0, 1) or    
        check_direction(board, row, col, piece, 1, 0) or    
        check_direction(board, row, col, piece, 1, 1) or    
        check_direction(board, row, col, piece, 1, -1)     
    )

def play_game():
    board = [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]
    current_player = "X"

    while True:
        print_board(board)
        col = input(f"Player {current_player}, choose a column (0-{COLUMNS-1}): ")

        if not col.isdigit() or not (0 <= int(col) < COLUMNS):
            print("Invalid input. Try again.")
            continue

        col = int(col)
        row = drop_piece(board, col, current_player)

        if row == -1:
            print("Column is full. Choose a different column.")
            continue

        if check_win(board, row, col, current_player):
            print_board(board)
            print(f" Player {current_player} wins! ")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()

# dhruv
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        
    print("\n")

def check_winner(board, player):
    win_states = (
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    )
    return [player]*3 in win_states

def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input! Choose between 1 and 9.")
            else:
                return (move - 1) // 3, (move - 1) % 3
        except ValueError:
            print("Please enter a valid number.")

def tic_tac_toe():
    board = [["1","2","3"],["4","5","6"],["7","8","9"]]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print("-----------------------")
    print_board(board)

    while True:
        row, col = get_move(current_player)
        if board[row][col] in ["X", "O"]:
            print("Spot already taken! Try again.")
            continue
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        if is_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()

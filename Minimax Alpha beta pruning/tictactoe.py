import math

# Initialize the board
board = [" " for _ in range(9)]

# Display the board
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

# Check for a winner
def check_winner(board):
    # Winning combinations
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

# Evaluate the board for minimax
def evaluate(board):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Human wins
        return -1
    else:
        return 0  # Draw or undecided

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizingPlayer):
    result = check_winner(board)
    if result is not None:
        return evaluate(board)

    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = " "
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval
    else:
        minEval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = " "
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval

# Find the best move for AI
def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("That space is already taken! Try again.")
            continue
        board[move] = "X"

        print_board(board)
        if check_winner(board):
            break

        # AI move
        print("AI is making a move...")
        ai_move = best_move(board)
        board[ai_move] = "O"
        print_board(board)

        winner = check_winner(board)
        if winner:
            break

    # Announce result
    winner = check_winner(board)
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

# Run the game
if __name__ == "__main__":
    play_game()

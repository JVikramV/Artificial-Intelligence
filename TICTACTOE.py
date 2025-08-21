import random

# Function to print the current game board
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

# Function to check if the game has a winner
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all(cell != ' ' for cell in board)

# Minimax algorithm to get the best move for the AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth  # AI wins
    elif check_winner(board, 'X'):
        return depth - 10  # Human wins
    elif check_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# Function to get the best move for the AI
def get_best_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to get human's move
def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That spot is already taken. Choose another.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to play Tic-Tac-Toe between Human and AI (Minimax)
def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human's turn
        move = get_human_move(board)
        board[move] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI is making a move...")
        ai_move = get_best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

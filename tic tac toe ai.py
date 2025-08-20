board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(b[i] == player for i in cond) for cond in win_conditions)

def minimax(b, depth, is_max):
    # Base cases
    if check_winner(b, "O"): 
        return 1
    if check_winner(b, "X"): 
        return -1
    if " " not in b: 
        return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best = max(best, score if score is not None else -float("inf"))
        return best if best != -float("inf") else 0  # ensure return
    else:
        best = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best = min(best, score if score is not None else float("inf"))
        return best if best != float("inf") else 0  # ensure return


def best_move():
    best_score = -float("inf")
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main Game Loop
while True:
    print_board()
    move = int(input("Enter your move (0-8): "))
    if board[move] != " ":
        print("Invalid move. Try again.")
        continue
    board[move] = "X"
    if check_winner(board, "X"):
        print_board()
        print("You win!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break

    ai = best_move()
    board[ai] = "O"
    if check_winner(board, "O"):
        print_board()
        print("AI wins!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break

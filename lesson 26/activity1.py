def print_board(board):
    print(f"{board[7]}  | {board[8]} | {board[9]} \n ---------") 
    print(f"{board[4]}  | {board[5]} | {board[6]} \n ---------") 
    print(f"{board[1]}  | {board[2]} | {board[3]} \n          ") 

def check_winner(board, player):
    if (board[7] == board[8] == board[9] == player or board[4] == board[5] == board[6] == player or board[1] == board[2] == board[3] == player or board[7] == board[4] == board[1] == player or board[8] == board[5] == board[2] == player or board[9] == board[6] == board[3] == player or board[7] == board[5] == board[3] == player or board[9] == board[5] == board[1] == player):
        return True
    return False

def game():
    board = {i: ' ' for i in range(1, 10)}
    turn = 'X'
    count = 0

    while count < 9:
        print_board(board)
        move = int(input(f"Player {turn}, enter your move (1-9): "))

        if board.get(move) == ' ':
            board[move] = turn
            count += 1
            if count >= 5 and check_winner(board, turn):
                print_board(board)
                print(f"Game over! Player {turn} wins!")
                break
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X' 
        
        else:
            print("Invalid move, try again")

    else: 
        print("It's a tie!")

    if input("Play again? (y/n): ").lower() == 'y':
        game()

game()

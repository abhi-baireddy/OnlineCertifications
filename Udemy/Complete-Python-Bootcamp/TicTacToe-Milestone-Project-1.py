import random

def display_board(board):
    row_1 = board[7:]
    row_2 = board[4:7]
    row_3 = board[1:4]
    print("\t".join(row_1))
    print("\t".join(row_2))
    print("\t".join(row_3))

def player_input():
    
    marker = input("Choose your marker (X/O): ")
    if marker == "X":
        print("You will go first")
        return marker
    elif marker == "O":
        print("You will go second")
        return marker
    else:
        print("Your marker can either be X or O")
        player_input()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if mark == "X":
        opponent = "O"
    else:
        opponent = "X"
        
    row1 = board[7:]
    row2 = board[4:7]
    row3 = board[1:4]

    col1 = [board[7], board[4], board[1]]
    col2 = [board[8], board[5], board[2]]
    col3 = [board[9], board[6], board[3]]

    diag1 = [board[7], board[5], board[3]]
    diag2 = [board[9], board[5], board[1]]
    
    sequences = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    
    win = False
    for sequence in sequences:
        if opponent not in sequence and "#" not in sequence:
            win = True
            break
    return win

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == "#"

def full_board_check(board):
    return "#"  not in board[1:]




def player_choice(board):
    position = int(input("Pick a position: "))
    if space_check(board, position):
        return position
    else:
        print("Position is already taken. Pick another position: ")
        player_choice(board)


def replay():
    flag = input("Do you want to play again? (Y/N): ")
    flag = flag.lower()
    if flag == 'y':
        return True
    return False


def main():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Set the game up here
        board = ["#"] * 10
        marker = player_input()
        game_on = True
        display_board(board)

        while game_on:
            # player 1's turn
            if not full_board_check(board):
                print("Player 1: ", end="")
                pos = player_choice(board)
                place_marker(board, "X", pos)
                print("\n"*100)
                display_board(board)
                if win_check(board, "X"):
                    print("Player 1 wins")
                    game_on = False
                    continue
            else:
                print("Tie")
                game_on = False
                continue
            # player 2's turn
            if not full_board_check(board):
                print("Player 2: ", end="")
                pos = player_choice(board)
                place_marker(board, "O", pos)
                print("\n"*100)
                display_board(board)
                if win_check(board, "O"):
                    print("Player 2 wins")
                    game_on = False

            else:
                print("Tie")
                game_on = False

        if not replay():
            break

if __name__ == "__main__":
    main()
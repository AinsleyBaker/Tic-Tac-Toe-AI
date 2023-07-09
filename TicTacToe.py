import random
import MediumAI as medium
import HardAI as hard

def reverse_symbol(symbol):
    """
    Reverses the symbol (X to 0 or 0 to X).
    """
    if symbol == "X":
        return "0"
    else:
        return "X"
    
def get_legal_moves(board):
    """
    Returns a list of legal moves on the board.
    """
    legal_moves = []
    for index, square in enumerate(board):
        if square == "-":
            legal_moves.append(index + 1)
    return legal_moves

def random_move(board, symbol):
    """
    Returns a random legal move on the board.
    """
    legal_moves = get_legal_moves(board)
    return random.choice(legal_moves)


def check_for_win(board):
    """
    Check if either player has won the game.
    """
    board_config = get_board_config()
    
    for line in board_config:
        positions = []
        for square in line:
            positions.append(board[square])
        
        if positions.count(positions[0]) == len(positions) and positions[0] != "-":
            return positions[0]
    return None

def check_for_draw(board):
    """
    Checks if the game results in a draw.
    """
    if "-" not in board:
        return True
    return False

def get_board_config():
    """
    Returns a list of every possible winning line configuration.
    """
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    cols = [[0, 3, 6], [1,4,7], [2, 5, 8]]
    diags = [[0, 4, 8], [2, 4, 6]]
    return rows + cols + diags

def new_board():
    """
    Creates a blank Tic-Tac-Toe board.
    """
    blank_board = [
            '-', '-', '-',
            '-', '-', '-',
            '-', '-', '-'
            ]
    return blank_board
    
def show_board(board):
    """
    Prints the board in a more aesthetic manner
    """
    print(board[0] + " | " + board[1] + " | " + board[2] + "          1 | 2 | 3") 
    print("---------          ---------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "          4 | 5 | 6")
    print("---------          ---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "          7 | 8 | 9")


        
def make_move(board, move, symbol):
    """
    Makes a move on the board with specified symbol.
    """
    board[move-1] = symbol
    return board
    
def game():
    name = input("What Is Your Name: ")
    while True:
        symbols = ["X", "0"]
        random.shuffle(symbols)
        turns = 0
        board = new_board()
        players = {
        symbols[0]: name,
        symbols[1]: "Computer"
        }

        while True:
            print("1. Easy   2. Medium   3. Hard")
            difficulty = input("Enter A Number For Difficulty: ")
            if difficulty in ["1", "2", "3"]:
                break
            else:
                print("Invalid difficulty. Please enter a number between 1 and 3.")

        while True:
            symbol = symbols[turns % 2]
            current_player = players[symbol]

            while True:
                show_board(board)
                print(f"\nIt is {current_player}'s turn!")
                if current_player == name:
                    move = int(input("Enter a square to place symbol: "))
                elif difficulty == "1":
                    move = random_move(board, symbol)
                elif difficulty == "2":
                    move = medium.mediumAI(board, symbol)
                elif difficulty == "3":
                    move = hard.hardAI(board, symbol)

                if move >= 1 and move <= 9 and board[move-1] == "-":
                    break
                else: 
                    print("Invalid move. Please try again.")
            board = make_move(board, move, symbol)

            winner = check_for_win(board)
            if winner is not None:
                show_board(board)
                print(f"The Winner Is {players[winner]}!")
                break
            if check_for_draw(board):
                show_board(board)
                print("The Game Is A Draw!")
                break

            turns += 1

        
        while True:  
            play_again = input("Would you Like To Play Again? (y/n): ").lower()
            if play_again in ['y', 'n']:
                break  
            else:
                print("Invalid input. Please Enter 'y' For Yes And 'n' For No.")
                
        if play_again == 'n':
            print("Thanks For Playing!")
            break
if __name__ == "__main__":
    game()

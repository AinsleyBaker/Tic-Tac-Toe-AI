import random
import TicTacToe as ttt

def mediumAI(board, symbol):
    """
    An AI with medium level difficulty

    The AI will attempt to win the game if it has two symbols in a row.
    It will block the opponent from winning if the opponent has two symbols in a row.
    It will choose a corner position if available.
    It will choose the center position if available.
    Otherwise, it will make a random move.
    """
    winning_move = find_winning_move(board, symbol)
    opp_move = opp_winning_move(board, symbol)
    legal_moves = ttt.get_legal_moves(board)

    open_corners = []
    for move in legal_moves:
        if move in [1, 3, 7,9]:
            open_corners.append(move)

    if winning_move:
        return winning_move
    elif opp_move:
        return opp_move
    elif open_corners:
        return random.choice(open_corners)
    elif 5 in legal_moves:
        return 5
    else:
        return ttt.random_move(board, symbol)
    
def opp_winning_move(board, symbol):
    """
    Finds the opponent's winning move on the tic-tac-toe board if possible.
    """
    if symbol == "X":
        return find_winning_move(board, "0")
    else:
        return find_winning_move(board, "X")


def find_winning_move(board, symbol):
    """
    Finds a winning move for the given symbol on the tic-tac-toe board.
    """
    board_config = ttt.get_board_config()

    for line in board_config:
        ai_symbol = 0
        opp_symbol = 0
        no_symbol = 0
        recent_square = None
        for square in line:
            if board[square] == symbol:
                ai_symbol += 1
            elif board[square] == "-":
                no_symbol += 1
                recent_square = square
            else:
                opp_symbol += 1

        if ai_symbol == 2 and no_symbol == 1:
            return recent_square + 1            

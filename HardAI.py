import TicTacToe as ttt
import copy

cache = {}
def hardAI(board, ai_symbol):
    best_move = None
    best_score = None

    for move in ttt.get_legal_moves(board):
        board_copy = copy.deepcopy(board)
        ttt.make_move(board_copy, move, ai_symbol)

        opp_symbol = ttt.reverse_symbol(ai_symbol)

        score = minimax(board_copy, opp_symbol, ai_symbol)
        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return best_move

def minimax(board, symbol_to_play, ai_symbol):
    cache_key = str(board)

    if cache_key not in cache:
        winner = ttt.check_for_win(board)
        if winner is not None:
            if winner == ai_symbol:
                cache[cache_key] = 10
            else:
                cache[cache_key] = -10
        elif ttt.check_for_draw(board):
            cache[cache_key] = 0
        else:
            legal_moves = ttt.get_legal_moves(board)

            scores = []
            for move in legal_moves:
                board_copy = copy.deepcopy(board)
                ttt.make_move(board_copy, move, symbol_to_play)

                opp_symbol = ttt.reverse_symbol(symbol_to_play)

                opp_best_score = minimax(board_copy, opp_symbol, ai_symbol)
                scores.append(opp_best_score)

            if symbol_to_play == ai_symbol:
                cache[cache_key] = max(scores)
            else:
                cache[cache_key] = min(scores)

    return cache[cache_key]

import chess
import chess.engine

def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval

def evaluate_board(board):
    # Évaluation simple pour illustration : matériel du joueur blanc contre matériel du joueur noir
    material_score = sum(piece_value(p) for p in board.piece_map().values())
    return material_score

def piece_value(piece):
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    return values.get(piece.piece_type, 0)

if __name__ == "__main__":
    board = chess.Board()
    
    # Exemple d'utilisation de l'algorithme Minimax avec une profondeur de 3
    best_move = None
    best_value = float('-inf')

    for move in board.legal_moves:
        board.push(move)
        move_value = minimax(board, 3, False)
        board.pop()
        if move_value > best_value:
            best_value = move_value
            best_move = move

    print("Meilleur mouvement selon Minimax:", best_move)

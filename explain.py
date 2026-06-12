import chess


def explain_move(board, move):
    piece = board.piece_at(move.from_square)

    explanations = []

    if board.is_capture(move):
        explanations.append("wins material")

    board.push(move)

    if board.is_check():
        explanations.append("gives check")

    if piece and piece.piece_type == chess.KNIGHT:
        explanations.append("improves knight activity")

    if not explanations:
        explanations.append("improves position")

    return ", ".join(explanations)
import chess


def validate_position(board_fen):
    candidates = [
        f"{board_fen} w - - 0 1",
        f"{board_fen} b - - 0 1"
    ]

    valid = []

    for fen in candidates:
        try:
            board = chess.Board(fen)

            if board.is_valid():
                valid.append(board)
        except:
            pass

    if not valid:
        raise RuntimeError("No legal position found")

    return valid[0]
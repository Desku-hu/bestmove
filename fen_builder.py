PIECE_MAP = {
    "wp": "P",
    "wn": "N",
    "wb": "B",
    "wr": "R",
    "wq": "Q",
    "wk": "K",
    "bp": "p",
    "bn": "n",
    "bb": "b",
    "br": "r",
    "bq": "q",
    "bk": "k",
}


def board_to_fen(predictions):
    rows = []

    for row in range(8):
        fen_row = ""
        empty = 0

        for col in range(8):
            idx = row * 8 + col

            piece = predictions[idx]

            if piece == "empty":
                empty += 1
            else:
                if empty:
                    fen_row += str(empty)
                    empty = 0

                fen_row += PIECE_MAP[piece]

        if empty:
            fen_row += str(empty)

        rows.append(fen_row)

    board_part = "/".join(rows)

    return board_part
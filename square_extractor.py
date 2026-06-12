def extract_squares(board_img):
    h, w = board_img.shape[:2]

    square_h = h // 8
    square_w = w // 8

    squares = []

    for row in range(8):
        for col in range(8):
            y1 = row * square_h
            y2 = (row + 1) * square_h

            x1 = col * square_w
            x2 = (col + 1) * square_w

            crop = board_img[y1:y2, x1:x2]

            squares.append(crop)

    return squares
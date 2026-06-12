import cv2

from board_detector import BoardDetector
from perspective import warp_board
from square_extractor import extract_squares
from piece_classifier import PieceClassifier
from fen_builder import board_to_fen
from legality import validate_position
from engine import ChessEngine
from explain import explain_move


def main(image_path):

    image = cv2.imread(image_path)

    detector = BoardDetector()

    corners = detector.detect_board(image)

    board_img = warp_board(image, corners)

    squares = extract_squares(board_img)

    classifier = PieceClassifier(
        "models/piece_classifier.pt"
    )

    predictions = [
        classifier.predict(sq)
        for sq in squares
    ]

    board_fen = board_to_fen(predictions)

    board = validate_position(board_fen)

    engine = ChessEngine("stockfish/stockfish")

    uci, san = engine.best_move(board)

    move = board.parse_uci(uci)

    explanation = explain_move(board, move)

    print("FEN:")
    print(board.fen())

    print()

    print("Best Move:")
    print("UCI:", uci)
    print("SAN:", san)

    print()

    print("Explanation:")
    print(explanation)

    engine.close()


if __name__ == "__main__":
    main("screenshot.png")
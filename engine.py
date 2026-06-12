import chess.engine


class ChessEngine:

    def __init__(self, stockfish_path):
        self.engine = chess.engine.SimpleEngine.popen_uci(
            stockfish_path
        )

    def best_move(self, board, time_limit=2.5):
        result = self.engine.play(
            board,
            chess.engine.Limit(time=time_limit)
        )

        move = result.move

        san = board.san(move)

        return move.uci(), san

    def close(self):
        self.engine.quit()
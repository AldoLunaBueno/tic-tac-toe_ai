from abc import ABC, abstractmethod
from game import Game
from tictactoe import TicTacToe

class Evaluator:
    @abstractmethod
    def evaluate(self, game: Game):
        """
        Evaluates statically a game state
        """
        pass

class TicTacToeStandardEvaluator(Evaluator):
    def __init__(self) -> None:
        self.heuristic_array = [[0, -1, -10],
                                [1, 0, 0],
                                [10, 0, 0]]
    def evaluate(self, game: TicTacToe, max_player: str) -> int:
        """
        Evaluates statically a TicTacToe game state
        """

        winner = game.get_winner()
        if winner != None:
            return float("inf") if (max_player == winner) else float("-inf")
        elif game.is_full():
            return 0

        eval = 0
        board = game.get_board()
        for line in game.get_winner_lines():
            x_count = sum(board[p] == "X" for p in line)
            o_count = sum(board[p] == "O" for p in line)
            eval += self.heuristic_array[x_count][o_count]
        return eval if max_player == "X" else -eval
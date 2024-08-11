import pytest
from ai_algorithms.ai import AI
from ai_algorithms.minimax import MinimaxAi
from evaluator import TicTacToeStandardEvaluator
from tictactoe import TicTacToe

# Abbreviation
parametrize = pytest.mark.parametrize

# Algorithms
@parametrize("Algorithm",[ MinimaxAi, ])
class TestAiAlgorithmsUsingStandardEvaluator:
    
    @pytest.fixture(autouse = True)
    def setup(self, Algorithm):
        self.game = TicTacToe()
        evaluator = TicTacToeStandardEvaluator()
        self.ai: AI = Algorithm(evaluator)
        # self.ai: AI = MinimaxAi(evaluator)

    @parametrize("board, expected_move",
                 [
                     (['O', ' ', ' ', 
                       'X', 'O', ' ', 
                       'X', ' ', ' '], 8),
                     (['O', ' ', ' ', 
                       'X', 'O', ' ', 
                       'X', 'O', 'X'], 1),
                     (['X', ' ', ' ', 
                       ' ', 'X', ' ', 
                       'O', ' ', 'O'], 7),
                     ([' ', 'X', 'O', 
                       ' ', 'X', ' ', 
                       'X', 'O', 'O'], 5)
                 ])
    def test_x_avoid_lose(self, board, expected_move):
        self.game.set_current_player("X")
        self.game.set_board(board)
        assert self.ai.move(self.game) == expected_move

    @parametrize("board, expected_move",
                 [
                     ([' ', 'X', ' ', 
                       ' ', 'X', ' ', 
                       ' ', ' ', 'O'], 7),
                     (['X', ' ', ' ', 
                       ' ', 'X', 'O', 
                       'O', ' ', ' '], 8),
                     ([' ', ' ', 'X', 
                       ' ', ' ', 'O', 
                       'X', ' ', 'O'], 4)
                 ])
    def test_o_avoid_lose(self, board, expected_move):
        self.game.set_current_player("O")
        self.game.set_board(board)
        assert self.ai.move(self.game) == expected_move

    @parametrize("board, expected_move", 
                 [
                     ([' ', 'X', 'O',
                       ' ', 'X', 'O', 
                       ' ', ' ', ' '], 7),
                     ([' ', ' ', 'X', 
                       ' ', 'X', 'O', 
                       ' ', 'O', ' '], 6),
                     (['X', ' ', 'X', 
                       ' ', 'O', 'O', 
                       ' ', ' ', ' '], 1),
                     ([' ', 'O', ' ', 
                       ' ', 'X', ' ', 
                       'O', ' ', 'X'], 0)
                 ])
    def test_x_win_next(self, board, expected_move):
        self.game.set_current_player("X")
        self.game.set_board(board)
        assert self.ai.move(self.game) == expected_move

    @parametrize("board, expected_move", 
                 [
                     (['O', ' ', 'X', 
                       ' ', ' ', 'X', 
                       'O', ' ', ' '], 3),
                     (['O', 'X', ' ', 
                       ' ', ' ', ' ', 
                       'X', ' ', 'O'], 4),
                     (['X', 'O', ' ', 
                       'X', 'X', 'O', 
                       ' ', 'X', 'O'], 2)
                 ])
    def test_o_win_next(self, board, expected_move):
        self.game.set_current_player("O")
        self.game.set_board(board)
        assert self.ai.move(self.game) == expected_move
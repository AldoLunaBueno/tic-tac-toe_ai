import pytest
#breakpoint()
# Classes to be evaluated
from ai_algorithms.ai import AI
from ai_algorithms.minimax import MinimaxAi
from ai_algorithms.alpha_beta_pruning import AlphaBetaPruning

# Local dependencies
# TODO: mock up these classes somehow, specially TicTacToe
from evaluator import TicTacToeStandardEvaluator
from tictactoe import TicTacToe

# Abbreviated decorators
parametrize = pytest.mark.parametrize

# Algorithms to be evaluated
algorithms = [MinimaxAi, AlphaBetaPruning]


@parametrize("Algorithm", algorithms)
class TestAiAlgorithmsUsingStandardEvaluator:
    
    @pytest.fixture(autouse = True)
    def setup(self, Algorithm):
        self.game = TicTacToe()
        evaluator = TicTacToeStandardEvaluator()
        self.ai: AI = Algorithm(evaluator)

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
        actual_move = self.ai.make_move(self.game)
        assert actual_move == expected_move

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
        actual_move = self.ai.make_move(self.game)
        assert actual_move == expected_move

    @parametrize("board, expected_move", 
                 [
                     ([' ', 'X', 'O',
                       ' ', 'X', 'O', 
                       ' ', ' ', ' '], 7),
                    # X can win moving to 6, but also to 0
                    #  ([' ', ' ', 'X', 
                    #    ' ', 'X', 'O', 
                    #    ' ', 'O', ' '], 6),
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
        actual_move = self.ai.make_move(self.game)
        assert actual_move == expected_move

    @parametrize("board, expected_move", 
                 [
                     (['O', ' ', 'X', 
                       ' ', ' ', 'X', 
                       'O', ' ', ' '], 3),
                    # O can win moving to 4, but also to 2
                    #  (['O', 'X', ' ', 
                    #    ' ', ' ', ' ', 
                    #    'X', ' ', 'O'], 4),
                     (['X', 'O', ' ', 
                       'X', 'X', 'O', 
                       ' ', 'X', 'O'], 2)
                 ])
    def test_o_win_next(self, board, expected_move):
        self.game.set_current_player("O")
        self.game.set_board(board)
        actual_move = self.ai.make_move(self.game)
        assert actual_move == expected_move

    @parametrize("board, expected_move", 
                 [
                     ([' ', ' ', ' ', 
                       ' ', ' ', ' ', 
                       ' ', ' ', ' '], 4)
                 ])
    def test_x_optimum_move(self, board, expected_move):
        self.game.set_current_player("X")
        self.game.set_board(board)
        actual_move = self.ai.make_move(self.game)
        assert actual_move == expected_move
    
    @parametrize("board, expected_move", 
                 [
                     (['X', ' ', ' ', 
                       ' ', ' ', ' ', 
                       ' ', ' ', ' '], 4)
                 ])
    def test_o_optimum_move(self, board, expected_move):
        self.game.set_current_player("O")
        self.game.set_board(board)
        actual_move = self.ai.make_move(self.game)
        assert actual_move == expected_move
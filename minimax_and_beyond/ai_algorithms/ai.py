from game import Game
from abc import ABC, abstractmethod
from tictactoe import TicTacToe
class AI(ABC):
    @abstractmethod
    def make_move(self, game: Game):
        pass
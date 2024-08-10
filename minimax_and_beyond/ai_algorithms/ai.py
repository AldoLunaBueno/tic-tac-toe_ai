from game import Game
from abc import ABC, abstractmethod
from tictactoe import TicTacToe
class AI(ABC):
    @abstractmethod
    def move(self, game: Game):
        pass
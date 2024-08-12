from ai_algorithms.ai import AI
from game import Game

class DumbAI(AI):
    def make_move(self, game: Game) -> int:
        position = game.available_moves()[0]
        return position
from ai_algorithms.ai import AI
from game import Game

class DumbAI(AI):
    def move(self, game: Game) -> int:
        position = game.available_positions()[0]
        return position
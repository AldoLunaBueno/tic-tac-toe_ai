from ai_algorithms.ai import AI
from game import Game
from evaluator import Evaluator

class MinimaxAi(AI):
    def __init__(self, evaluator: Evaluator) -> None:
        self.evaluator = evaluator
    def make_move(self, game: Game) -> int:
        position = self._minimax(game, game.get_current_player(), depth = 2)
        return position
        
    
    def _minimax(self, game: Game, max_player, depth = 4):
        best_score = float("-inf")
        position = None
        for i in game.available_moves():
            game.play(i, real = False)
            score = self._inner_minimax(game, max_player, depth = depth - 1)
            game.undo()
            if score < best_score:
                continue

            best_score = score
            position = i
            
        return position


    def _inner_minimax(self, game: Game, max_player: str, maximizing = False, depth = 2) -> int:

        winner = game.get_winner()
        if winner != None:
            return float("inf") if (winner == max_player) else float("-inf")
        elif game.is_full():
            return 0
        elif depth == 0:
            return self.evaluator.evaluate(game, max_player)
        
        if not maximizing:
            best_score = float("inf")
            for i in game.available_moves():
                game.play(i, real = False)
                score = self._inner_minimax(game, max_player, maximizing = True, depth = depth-1)
                game.undo()
                best_score = min(score, best_score)
            return best_score
        elif maximizing:
            best_score = float("-inf")
            for i in game.available_moves():
                game.play(i, real = False)
                score = self._inner_minimax(game, max_player, maximizing = False, depth = depth-1)
                game.undo()
                best_score = max(score, best_score)
            return best_score
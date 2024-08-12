from ai_algorithms.ai import AI
from game import Game

class MinimaxWithoutEvalFuncOrDepthAi(AI):
    def make_move(self, game: Game) -> int:
        position = self._minimax(game, game.get_current_player())
        return position
        
    
    def _minimax(self, game: Game, max_player):
        best_score = float("-inf")
        for i in game.available_moves():
            game.play(i, real = False)
            score = self._inner_minimax(game, max_player)
            game.undo()
            if score <= best_score:
                continue

            best_score = score
            position = i
            
        return position


    def _inner_minimax(self, game: Game, max_player: str, maximizing = False) -> int:
        winner = game.get_winner()
        if winner != None:
            return 10 if (winner == max_player) else -10
        elif game.is_full():
            return 0
        
        if not maximizing:
            best_score = float("inf")
            for i in game.available_moves():
                game.play(i, real = False)
                score = self._inner_minimax(game, max_player, maximizing = True)
                game.undo()
                best_score = min(score, best_score)
            return best_score
        elif maximizing:
            best_score = float("-inf")
            for i in game.available_moves():
                game.play(i, real = False)
                score = self._inner_minimax(game, max_player, maximizing = False)
                game.undo()
                best_score = max(score, best_score)
            return best_score
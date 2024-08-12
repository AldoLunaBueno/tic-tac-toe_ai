from ai_algorithms.ai import AI
from game import Game
from evaluator import Evaluator
from typing import Tuple

class AlphaBetaPruning(AI):
    def __init__(self, evaluator: Evaluator) -> None:
        self.evaluator = evaluator
    def make_move(self, game: Game):
        max_player = game.get_current_player()
        move, _ = self.__ab_pruning(game, max_player)
        return move

    def __ab_pruning(self, game: Game, max_player: str, 
                     alpha: int = float("-inf"), beta: int = float("inf"), 
                     depth: int = 3, maximizing = True) -> Tuple[int, int]:
        winner = game.get_winner()
        if winner != None:
            return None, float("inf") if (winner == max_player) else float("-inf")
        elif game.is_full():
            return None, 0
        elif depth == 0:
            return None, self.evaluator.evaluate(game, max_player)
        
        best_move = None
        if maximizing:          
            for move in game.available_moves():
                game.play(move, real = False) 
                _, score = self.__ab_pruning(game, max_player, alpha, beta, depth-1, maximizing = False)
                game.undo()
                if score < alpha:
                    continue
                alpha = score
                best_move = move
                if alpha >= beta: # main condition to PRUNING
                    break
                if alpha == float("inf"): # max_player win the game, so...
                    break
            return best_move, alpha
        else:
            for move in game.available_moves():
                game.play(move, real = False) 
                _, score = self.__ab_pruning(game, max_player, alpha, beta, depth-1, maximizing = True)
                game.undo()      
                if score > beta:
                    continue
                beta = score
                best_move = move
                if alpha >= beta: # main condition to PRUNING
                    break
                if beta == float("-inf"): # max_player lose the game, so...
                    break
            return best_move, beta

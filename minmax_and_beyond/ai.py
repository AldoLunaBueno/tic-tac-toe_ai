from tictactoe import TicTacToe

class DumbAi():
    def move(self, game: TicTacToe) -> int:
        position = game.available_positions()[0]
        return position
    
class MinimaxAi():
    def move(self, game: TicTacToe) -> int:
        position = self._minimax(game, game.current_player)
        return position
        
    
    def _minimax(self, game, max_player):
        best_score = float("-inf")
        for i in game.available_positions():
            game.play(i, real = False)
            score = self._inner_minimax(game, max_player)
            game.undo()
            if score <= best_score:
                continue

            best_score = score
            position = i
            
        return position


    def _inner_minimax(self, game: TicTacToe, max_player: str, maximizing = False) -> int:
        if game.there_is_winner():
            game.change_player() # Tricky af
            winner = game.current_player 
            game.change_player() # Tricky af
            return 10 if (winner == max_player) else -10
        elif game.is_full():
            return 0
        
        if not maximizing:
            best_score = float("inf")
            for i in game.available_positions():
                game.play(i, real = False)
                score = self._inner_minimax(game, max_player, maximizing = True)
                game.undo()
                best_score = min(score, best_score)
            return best_score
        elif maximizing:
            best_score = float("-inf")
            for i in game.available_positions():
                game.play(i, real = False)
                score = self._inner_minimax(game, max_player, maximizing = False)
                game.undo()
                best_score = max(score, best_score)
            return best_score
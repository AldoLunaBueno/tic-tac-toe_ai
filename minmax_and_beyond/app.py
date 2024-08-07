from tictactoe import TicTacToe
from ai import MinimaxAi

game = TicTacToe()
ai = MinimaxAi()
def main():
    while True:
        ai_position = ai.move(game)
        print(f"AI ({game.current_player}) moves to {ai_position}: ")               
        if game.play(ai_position):
            return
        while True:
            game.display()
            print("\n")
            human_position = int(input(f"Player {game.current_player} moves to [position]: "))
            result = game.play(human_position)
            game.display()
            print("\n")
            if result == None:
                continue
            elif result == False:
                break
            else:
                return
main()
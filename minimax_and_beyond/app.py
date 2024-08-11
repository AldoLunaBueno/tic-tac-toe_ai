from tictactoe import TicTacToe
from ai_algorithms.minimax import MinimaxAi
from evaluator import TicTacToeStandardEvaluator

game = TicTacToe()
evaluator = TicTacToeStandardEvaluator()
ai = MinimaxAi(evaluator)

# keyboard to position
kb2pos = {7:0, 8:1, 9:2,
          4:3, 5:4, 6:5,
          1:6, 2:7, 3:8}
# position to keyboard
pos2kb = {0:7, 1:8, 2:9,
          3:4, 4:5, 5:6,
          6:1, 7:2, 8:3}
def main():
    c = menu()
    game.display(kb_numbers = True)
    print("\n")
    if c == "X":
        while True:
            if human_turn() or ai_turn():
                return
    elif c == "O":
        while True:
            if ai_turn() or human_turn():
                return

def trans_kb2pos(in_numb: int):
    out_numb = kb2pos[in_numb]
    return out_numb
def trans_pos2kb(in_numb: int):
    out_numb = pos2kb[in_numb]
    return out_numb
        
def menu():
    return input("\nX moves first\nO moves next\nChoose your character (X/O): ")

def ai_turn():
    ai_position = ai.move(game)    
    print(f"AI ({game.get_current_player()}) moves to {trans_pos2kb(ai_position)}: ")               
    if game.play(ai_position):
        game.display()
        return True
    game.display()
    print(game.get_board())
    print("\n")
    return False

def human_turn():
    while True:
        player = game.get_current_player()
        human_position = int(input(f"Player {player} moves to [1-9]: "))
        result = game.play(trans_kb2pos(human_position))
        game.display()
        print("\n")
        if result == None:
            continue
        return result

main()
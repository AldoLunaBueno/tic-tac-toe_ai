from game import Game
from typing import List, Union

class TicTacToe(Game):
    def __init__(self):
        self.__board = [" " for i in range(9)]
        self.__current_player = "X"
        self.__position_stack = list()
        self.__winner_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
    def available_moves(self) -> List:
        positions = [i for i, c in enumerate(self.__board) if c == " "]
        return positions

    def next_turn(self):
        # Change turn
        if self.__current_player == "X":
            self.__current_player = "O"
        else:
            self.__current_player = "X"

    def display(self, kb_numbers = False):
        """
        Displays the board game.
        """
        if kb_numbers:
            rows = [[3*i+1, 3*i+2, 3*i+3] for i in range(2,-1,-1)]
            for row in rows:
                print("|" + "|".join(list(map(str, row))) + "|")
            return

        rows = [self.__board[3*i:3*(i+1)] for i in range(3)]
        for row in rows:
            print("|" + "|".join(row) + "|")

    def get_board(self):
        return self.__board
    
    def get_winner(self):        
        for win_line in self.__winner_lines:
            if self.__board[win_line[0]] == self.__board[win_line[1]] == self.__board[win_line[2]] != " ":                
                return self.__board[win_line[0]]
        return None
    
    def is_full(self):
        return " " not in self.__board
    
    def play(self, position, real = True) -> Union[bool,None]:
        if not real:
            self.__board[position] = self.__current_player
            self.__position_stack.append(position)
            self.next_turn()
            return None
            
        # Validation
        if self.__board[position] != " ":
            print("Occupied position. Select another position.")
            return None
        elif not (0 <= position < len(self.__board)):
            print("Invalid position.")
            return None
        
        # Actual move           
        self.__board[position] = self.__current_player
        # Memory for undo
        self.__position_stack.append(position)

        # Check end game
        if self.get_winner():
            print(f"Winner: {self.__current_player}")
            return True
        elif self.is_full():
            print("It's a draw.")
            return True   
        
        self.next_turn()
        return False
    
    def undo(self):
        if self.__position_stack == None:
            print("There is no move to undo.")
            return
        
        last_position = self.__position_stack.pop()
        self.__board[last_position] = " "
        self.next_turn()

    def get_winner_lines(self):
        return self.__winner_lines
    
    def get_current_player(self):
        return self.__current_player
    
    def set_board(self, board):
        self.__board = board

    def set_current_player(self, player: str):
        self.__current_player = player
from typing import List, Union

class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.current_player = "X"
        self.position_stack = list()
        
    def available_positions(self) -> List:
        positions = [i for i, c in enumerate(self.board) if c == " "]
        return positions

    def change_player(self):
        # Change turn
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def display(self):
        """
        Displays the board game.
        """
        rows = [self.board[3*i:3*(i+1)] for i in range(3)]
        for row in rows:
            print("|" + "|".join(row) + "|")
    
    def there_is_winner(self):
        winner_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for win_line in winner_lines:
            if self.board[win_line[0]] == self.board[win_line[1]] == self.board[win_line[2]] != " ":                
                return True
        return False
    
    def is_full(self):
        return " " not in self.board
    
    def play(self, position, real = True) -> Union[bool,None]:
        if not real:
            self.board[position] = self.current_player
            self.position_stack.append(position)
            self.change_player()
            return None
            
        # Validation
        if self.board[position] != " ":
            print("Occupied position. Select another position.")
            return None
        elif not (0 <= position < len(self.board)):
            print("Invalid position.")
            return None
        
        # Actual move           
        self.board[position] = self.current_player
        # Memory for undo
        self.position_stack.append(position)

        # Check end game
        if self.there_is_winner():
            self.display()
            print(f"Winner: {self.current_player}")
            return True
        elif self.is_full():
            self.display()
            print("It's a draw.")
            return True   
        
        self.change_player()
        return False
    
    def undo(self):
        if self.position_stack == None:
            print("There is no move to undo.")
            return
        
        last_position = self.position_stack.pop()
        self.board[last_position] = " "
        self.change_player()
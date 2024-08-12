from abc import ABC, abstractmethod

class Game(ABC):

    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def next_turn(self):
        pass

    @abstractmethod
    def play(self, move, real = True):
        pass
    
    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def get_board(self):
        pass

    @abstractmethod
    def get_winner(self):
        pass

    @abstractmethod
    def get_current_player(self):
        pass

    @abstractmethod
    def set_current_player(self):
        pass

    @abstractmethod
    def set_board(self):
        pass
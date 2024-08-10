from abc import ABC, abstractmethod

class Game(ABC):

    current_player: str

    @abstractmethod
    def available_positions(self):
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
    def play(self, position):
        pass
    
    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def winner(self):
        pass
from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def run(self):
        pass
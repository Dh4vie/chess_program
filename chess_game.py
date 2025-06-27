import pygame
import chess
from game import Game

class ChessGame(Game):
    def run(self):
        print("Chess Program Running..")

if __name__ == "__main__":
    game = ChessGame()
    game.run()
import pygame
import chess
from game import Game
from drawer import PieceDrawer, square_size
from piece_mover import PieceMover

class ChessGame(Game):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((8 * square_size, 8 * square_size))
        pygame.display.set_caption("Chess")
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = chess.Board()
        self.drawer = PieceDrawer(self.screen, self.board)
        self.mover = PieceMover(self.board)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mover.click_handler(pygame.mouse.get_pos())

            self.drawer.draw_board()
            self.drawer.load_pieces()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = ChessGame()
    game.run()
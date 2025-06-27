import pygame
import chess

square_size = 120

class PieceDrawer:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.images = self.load_images()

    def load_images(self):
        names = ['white_pawn', 'white_rook', 'white_horse', 'white_bishop','white_queen', 'white_king', 'black_pawn', 'black_rook', 'black_horse', 'black_bishop', 'black_queen', 'black_king']
        return {name: pygame.transform.scale(pygame.image.load(f"images/{name}.png"),(square_size, square_size)) for name in names}
    
    def draw_board(self):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(8):
            for column in range(8):
                color = colors[(row + column) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(column * square_size, row * square_size, square_size, square_size))

    def load_pieces(self):
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)     
            if piece:
                color = 'white' if piece.color == chess.WHITE else 'black'
                kind = {'p': 'pawn', 'r': 'rook', 'n': 'horse', 'b': 'bishop', 'q': 'queen', 'k': 'king'}[piece.symbol().lower()]
                name = f'{color}_{kind}'
                columns = square % 8
                rows = 7 - (square // 8)
                self.screen.blit(self.images[name], pygame.Rect(columns * square_size, rows * square_size, square_size, square_size))
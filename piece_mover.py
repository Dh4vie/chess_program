import pygame
import chess
from drawer import square_size

class PieceMover:
    def __init__(self, board):
        self.board = board
        self.selected_square = None

    def click_handler(self, position):
        columns = position[0] // square_size
        row = 7 - (position[1] // square_size)
        clicked_square = chess.square(columns, row)

        if self.selected_square is None:
            if self.board.piece_at(clicked_square) is not None and self.board.piece_at(clicked_square).color == self.board.turn:
                self.selected_square = clicked_square

            else:
                move = chess.Move(self.selected_square, clicked_square)
                if move in self.board.legal_moves:
                    self.board.push(move)
                self.selected_square = None
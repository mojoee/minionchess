import pygame as pg
from utils import load_image
from enum import Enum
from abc import ABC


class Pieces(Enum):
    PAWN = 1
    CASTLE = 2
    KNIGHT = 3
    BISHOP = 4
    KING = 5
    QUEEN = 6


class Side(pg.sprite.Group):
    def __init__(self, color, start_formation, Board) -> None:
        pg.sprite.Group.__init__(self)
        # each side should have 8 pawns, 2 castles, 2 knights, 2 bishops,
        # 1 queen, 1 king; they need to be fit to their positions
        self.start_formation = start_formation
        for p in Pieces:
            path = f"resources/{color}/{p.name}.png"
            positions = start_formation[p.name]
            for pos in positions:
                if p.name == "PAWN":
                    new_piece = Pawn(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                else:
                    new_piece = Piece(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                self.add(new_piece)
    
    def show_destinations(self):
        pass



class Piece(pg.sprite.Sprite, ABC):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__()
        self.image, self.rect = load_image(image_path, -1)
        self.type = Pieces(fig_type)
        self.rect.x = tile.rect.x
        self.rect.y = tile.rect.y
        self.tile = tile
        self.side = color
        self.factor = None

        self.set_side()


    def set_side(self):
        if self.side == "male":
            self.factor = -1
        else:
            self.factor = 1

    def move(self, x, y):
        pass

    def get_possible_moves(self):
        pass

    def remove(self):
        pass

    def can_throw(self):
        pass

class Pawn(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)
        self.moved = False

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.moved = True

    def get_possible_moves(self):
        possible_moves = []
        if not self.moved:
            possible_moves.append((self.tile.id_vertical + (2*self.factor), self.tile.id_horizontal))
        possible_moves.append((self.tile.id_vertical + (1*self.factor), self.tile.id_horizontal))
        return possible_moves

    def get_possible_throws(self):
        possible_throws = []
        possible_throws.append((self.tile.id_vertical + (1*self.factor), self.tile.id_horizontal-1))
        possible_throws.append((self.tile.id_vertical + (1*self.factor), self.tile.id_horizontal+1))
        return possible_throws



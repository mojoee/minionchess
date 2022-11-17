import pygame as pg
from utils import load_image
from enum import Enum


class Pieces(Enum):
    PAWN = 1
    CASTLE = 2
    KNIGHT = 3
    BISHOP = 4
    KING = 5
    QUEEN = 6


class Side(pg.sprite.Group):
    def __init__(self, color) -> None:
        pg.sprite.Group.__init__(self)
        # each side should have 8 pawns, 2 castles, 2 knights, 2 bishops,
        # 1 queen, 1 king; they need to be fit to their positions
        for p in Pieces:
            path = f"resources/{color}/{p.name}.jpg"
            new_piece = Piece(path, p)
            self.add(new_piece)


class Piece(pg.sprite.Sprite):
    def __init__(self, image_path, type) -> None:
        super().__init__()
        self.image, self.rect = load_image(image_path, -1)
        self.type = Pieces(type)

    def move(self):
        pass

    def remove(self):
        pass

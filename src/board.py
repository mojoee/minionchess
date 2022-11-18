import pygame as pg

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)


class Board(pg.sprite.Group):
    def __init__(self, width, pos_x, pos_y) -> None:
        pg.sprite.Group.__init__(self)
        self.width = width
        self.height = width
        self.edge_size = width/8
        self.tiles = []
        self.make_tiles(pos_x, pos_y)

    def make_tiles(self, offset_x, offset_y):
        for i in range(8):
            self.tiles.append([])
            for j in range(8):
                if (j+i) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                tile = Tile(color, self.edge_size,
                            offset_x + j * self.edge_size,
                            offset_y + i * self.edge_size)
                self.add(tile)
                self.tiles[i].append(tile)


class Tile(pg.sprite.Sprite):
    def __init__(self, color, edge_size, pos_x, pos_y) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([edge_size, edge_size])
        self.image.fill(color)
        self.color = color
        self.width = edge_size
        self.height = edge_size
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def change_color(self, color):
        self.color = color

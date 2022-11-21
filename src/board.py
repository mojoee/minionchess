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
                            offset_x, offset_y, j, i)
                self.add(tile)
                self.tiles[i].append(tile)

    def remove_highlights(self):
        for tile in self.sprites():
            tile.reset()


class Tile(pg.sprite.Sprite):
    def __init__(self, color, edge_size, offset_x, offset_y, horizontal, vertical) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([edge_size, edge_size])
        self.image.fill(color)
        self.color = color
        self.width = edge_size
        self.height = edge_size
        self.rect = self.image.get_rect()
        self.rect.x = offset_x + horizontal * edge_size
        self.rect.y = offset_y + vertical * edge_size
        self.id_vertical = vertical
        self.id_horizontal = horizontal
        self.selected = False
        self.choice = False

    def change_color(self, color):
        self.color = color

    def highlight(self):
        # self.color = (102, 255, 0)
        self.image.fill((102, 255, 0))
        self.selected = True

    def show_choice(self):
        # self.color = (102, 255, 0)
        self.image.fill((128,128,128))
        self.choice = True

    def reset(self):
        # self.color = (102, 255, 0)
        self.image.fill(self.color)
        self.selected = False
        self.choice = False

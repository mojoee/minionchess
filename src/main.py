import pygame as pg


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    pg.display.set_caption("Monkey Fever")
    pg.mouse.set_visible(False)
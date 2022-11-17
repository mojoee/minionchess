import pygame as pg
from board import Board

if __name__ == "__main__":
    screen_width, screen_height = 1280, 480
    board_size = 300
    pg.init()
    screen = pg.display.set_mode((screen_width, screen_height), pg.SCALED)
    pg.display.set_caption("Minion Chess")
    pg.mouse.set_visible(False)
    game_on = True
    while game_on:
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 0))
        board = Board(board_size, (screen_width-board_size)/2,
                      (screen_height-board_size)/2)
        board.draw(background)
        screen.blit(background, (0, 0))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_on = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pass
            elif event.type == pg.MOUSEBUTTONUP:
                pass


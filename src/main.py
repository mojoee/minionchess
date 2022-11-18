import pygame as pg
from board import Board
from pieces import Side

white_start_formation = {
    "PAWN": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    "CASTLE": [(0, 0), (0, 7)],
    "KNIGHT": [(0, 1), (0, 6)],
    "BISHOP": [(0, 2), (0, 5)],
    "KING": [(0, 3)],
    "QUEEN": [(0, 4)]
    }

black_start_formation = {
    "PAWN": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "CASTLE": [(7, 0), (7, 7)],
    "KNIGHT": [(7, 1), (7, 6)],
    "BISHOP": [(7, 2), (7, 5)],
    "KING": [(7, 3)],
    "QUEEN": [(7, 4)]
    }

if __name__ == "__main__":
    screen_width, screen_height = 1280, 480
    board_size = 300
    pg.init()
    screen = pg.display.set_mode((screen_width, screen_height), pg.SCALED)
    pg.display.set_caption("Minion Chess")
    pg.mouse.set_visible(False)
    clock = pg.time.Clock()
    game_on = True
    board = Board(board_size, (screen_width-board_size)/2, (screen_height - board_size)/2)
    white = Side("male", white_start_formation, board)
    black = Side("female", black_start_formation, board)

    while game_on:
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 0))

        board.draw(background)
        white.draw(background)
        black.draw(background)
        screen.blit(background, (0, 0))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_on = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pass
            elif event.type == pg.MOUSEBUTTONUP:
                pass

        pg.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)


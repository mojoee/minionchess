import pygame as pg
from config import Config
from pieces import Side
from board import Board



white_start_formation = {
    "PAWN": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "CASTLE": [(7, 0), (7, 7)],
    "KNIGHT": [(7, 1), (7, 6)],
    "BISHOP": [(7, 2), (7, 5)],
    "KING": [(7, 3)],
    "QUEEN": [(7, 4)]
    }

black_start_formation = {
    "PAWN": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    "CASTLE": [(0, 0), (0, 7)],
    "KNIGHT": [(0, 1), (0, 6)],
    "BISHOP": [(0, 2), (0, 5)],
    "KING": [(0, 3)],
    "QUEEN": [(0, 4)]
    }

moves = {
    "PAWN": [1, 2],
    "CASTLE": [],
    "KNIGHT": [],
    "BISHOP": [],
    "KING": [(7, 3)],
    "QUEEN": [(7, 4)]
    }


class Controller():
    def __init__(self) -> None:
        self.game_on = True
        self.turn = "white"
        self.clock = None
        self.screen = None
        self.board = None
        self.p1 = None  # white
        self.p2 = None  # black
        self.cfg = Config()


    def initialize_game(self):
        pg.init()
        self.screen = pg.display.set_mode((self.cfg.screen_width, self.cfg.screen_height), pg.SCALED)
        self.clock = pg.time.Clock()
        pg.display.set_caption(self.cfg.caption)
        pg.mouse.set_visible(True)
        self.board = Board(self.cfg.board_size, (self.cfg.screen_width-self.cfg.board_size)/2, (self.cfg.screen_height - self.cfg.board_size)/2)
        self.p1 = Side("male", white_start_formation, self.board)
        self.p2 = Side("female", black_start_formation, self.board)

    def show_moves(self):
        pass

    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def make_move(self):
        pass

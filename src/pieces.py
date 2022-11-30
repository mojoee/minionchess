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
                elif p.name == "CASTLE":
                    new_piece = Castle(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                elif p.name == "KNIGHT":
                    new_piece = Knight(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                elif p.name == "BISHOP":
                    new_piece = Bishop(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                elif p.name == "QUEEN":
                    new_piece = Queen(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                elif p.name == "KING":
                    new_piece = King(path, p, Board.tiles[pos[0]][pos[1]], color)
                    Board.tiles[pos[0]][pos[1]].set_occupied()
                    Board.tiles[pos[0]][pos[1]].figure = new_piece
                else:
                    print("Class does not exist!")
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
        self.possible_moves = []

        self.set_side()


    def set_side(self):
        if self.side == "male":
            self.factor = -1
        else:
            self.factor = 1

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_possible_moves(self, board):
        pass

    def get_possible_throws(self, board):
        return []

    def remove(self):
        pass

    def can_throw(self):
        pass

    def own_field(self, x, y):
        if self.tile.id_vertical == x and self.tile.id_horizontal == y:
            return True
        else:
            return False

    def clean_moves(self, moves):
        possible_moves_iterator = moves.copy()
        for move in possible_moves_iterator:
            if move[0] < 0 or move[0] > 7:
                moves.remove(move)
                continue
            if move[1] < 0 or move[1] > 7:
                moves.remove(move)

        self.possible_moves = moves


class Pawn(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)
        self.moved = False

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.moved = True

    def get_possible_moves(self, board):
        possible_moves = []
        if not self.moved:
            possible_moves.append((self.tile.id_vertical + (2*self.factor), self.tile.id_horizontal))
        possible_moves.append((self.tile.id_vertical + (1*self.factor), self.tile.id_horizontal))
        return possible_moves

    def get_possible_throws(self, board):
        possible_throws = []
        possible_throws.append((self.tile.id_vertical + (1*self.factor), self.tile.id_horizontal-1))
        possible_throws.append((self.tile.id_vertical + (1*self.factor), self.tile.id_horizontal+1))
        return possible_throws


class Castle(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)

    def get_possible_moves(self, board):
        possible_moves = []
        x = self.tile.id_vertical
        y = self.tile.id_horizontal

        for i in range(x+1, 8):
            if board.tiles[i][y].occupied:
                break
            possible_moves.append((i, y))
        for i in range(x-1, 0, -1):
            if board.tiles[i][y].occupied:
                break
            possible_moves.append((i, y))

        for i in range(y+1, 8):
            if board.tiles[x][i].occupied and board.tiles[x][i].figure.side != self.side:
                break
            possible_moves.append((x, i))
        for i in range(y-1, 0, -1):
            if board.tiles[x][i].occupied:
                break
            possible_moves.append((x, i))

        return possible_moves


    def get_possible_throws(self, board):
        # or should this be implemented by controller?
        possible_throws = []
        # possible_moves.append((self.tile.id_vertical + 1, self.tile.id_horizontal))
        x = self.tile.id_vertical
        y = self.tile.id_horizontal

        for i in range(x+1, 8):
            if board.tiles[i][y].is_opponent(self.side):
                possible_throws.append((i, y))
                break
            if board.tiles[i][y].occupied:
                break
        for i in range(x-1, 0, -1):
            if board.tiles[i][y].is_opponent(self.side):
                possible_throws.append((i, y))
                break
            if board.tiles[i][y].occupied:
                break
        for i in range(y+1, 8):
            if board.tiles[x][i].is_opponent(self.side):
                possible_throws.append((x, i))
                break
            if board.tiles[x][i].occupied:
                break           
        for i in range(y-1, 0, -1):
            if board.tiles[x][i].is_opponent(self.side):
                possible_throws.append((x, i))
                break
            if board.tiles[x][i].occupied:
                break

        return possible_throws

class Knight(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)

    def get_possible_moves(self, board):
        possible_moves = []
        x = self.tile.id_vertical
        y = self.tile.id_horizontal
        possible_moves.append((x+2, y+1))
        possible_moves.append((x+2, y-1))
        possible_moves.append((x-2, y+1))
        possible_moves.append((x-2, y-1))
        possible_moves.append((x+1, y+2))
        possible_moves.append((x+1, y-2))
        possible_moves.append((x-1, y+2))
        possible_moves.append((x-1, y-2))

        self.clean_moves(possible_moves)

        return self.possible_moves

    def get_possible_throws(self, board):
        possible_throws = []
        for move in self.possible_moves:
            if board.tiles[move[0]][move[1]].is_opponent(self.side):
                possible_throws.append(move)
        return possible_throws


class Bishop(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)

    def get_possible_moves(self, board):
        possible_moves = []
        x = self.tile.id_vertical
        y = self.tile.id_horizontal

        # 4 ways for the diagonals
        # ++, +-, -+, --
        for i in range(8-max(x, y)):
            field = (x+i, y+i)
            if self.own_field(field[0], field[1]):
                continue
            possible_moves.append(field)
            if board.tiles[field[0]][field[1]].occupied:
                break
        for i in range(min(y, 8-x)):
            field = (x+i, y-i)
            if self.own_field(field[0], field[1]):
                continue
            possible_moves.append(field)
            if board.tiles[field[0]][field[1]].occupied:
                break
        for i in range(min(x, 8-y)):
            field = (x-i, y+i)
            if self.own_field(field[0], field[1]):
                continue
            possible_moves.append(field)
            if board.tiles[field[0]][field[1]].occupied:
                break
        for i in range(min(x, y)+1):
            field = (x-i, y-i)
            if self.own_field(field[0], field[1]):
                continue
            possible_moves.append(field)
            if board.tiles[field[0]][field[1]].occupied:
                break

        self.possible_moves = possible_moves
        return possible_moves

    def get_possible_throws(self, board):
        possible_throws = []
        for move in self.possible_moves:
            if board.tiles[move[0]][move[1]].is_opponent(self.side):
                possible_throws.append(move)
        return possible_throws

class Queen(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)


class King(Piece):
    def __init__(self, image_path, fig_type, tile, color) -> None:
        super().__init__(image_path, fig_type, tile, color)

    def get_possible_moves(self, board):

        possible_moves = []
        x = self.tile.id_vertical
        y = self.tile.id_horizontal
        possible_moves.append((x+1, y+1))
        possible_moves.append((x+1, y))
        possible_moves.append((x+1, y-1))
        possible_moves.append((x, y+1))
        possible_moves.append((x, y))
        possible_moves.append((x, y-1))        
        possible_moves.append((x-1, y+1))
        possible_moves.append((x-1, y))
        possible_moves.append((x-1, y-1))
        self.clean_moves(possible_moves)
        return self.possible_moves

    def get_possible_throws(self, board):
        possible_throws = []
        for move in self.possible_moves:
            if board.tiles[move[0]][move[1]].is_opponent(self.side):
                possible_throws.append(move)
        return possible_throws

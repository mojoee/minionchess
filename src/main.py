import pygame as pg
from board import Board
from pieces import Side
from controller import Controller
from config import Config


if __name__ == "__main__":

    cntrl = Controller()
    cntrl.initialize_game()

    while cntrl.game_on:
        background = pg.Surface(cntrl.screen.get_size())
        background = background.convert()
        background.fill((255, 255, 0))
        cntrl.board.draw(background)
        cntrl.p1.draw(background)
        cntrl.p2.draw(background)
        cntrl.screen.blit(background, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                cntrl.game_on = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                cntrl.make_move()
                    # check if figures are selected
                for spr in cntrl.current_player.sprites():
                    if spr.rect.collidepoint(x, y) and spr.tile.selected:
                        cntrl.board.remove_highlights()
                    elif spr.rect.collidepoint(x, y):
                        spr.tile.highlight()
                        possible_moves = spr.get_possible_moves()
                        possible_throws = spr.get_possible_throws()
                        for tile in possible_moves:
                            tile = cntrl.board.tiles[tile[0]][tile[1]]
                            cntrl.selected_figure = spr
                            tile.show_choice()
                        for tile in possible_throws:
                            tile = cntrl.board.tiles[tile[0]][tile[1]]
                            # cntrl.selected_figure = spr
                            if tile.occupied:
                                tile.show_throw()
                for spr in cntrl.board.sprites():
                    if spr.rect.collidepoint(x, y) and spr.choice:

                        cntrl.selected_figure.move(spr.rect.x, spr.rect.y)
                        if spr.occupied:
                            cntrl.remove_figure(spr.figure)
                        spr.set_occupied()
                        cntrl.selected_figure.tile.set_unoccupied()
                        cntrl.selected_figure.tile = spr
                        spr.figure = cntrl.selected_figure
                        cntrl.board.remove_highlights()
                        cntrl.change_turn()

            elif event.type == pg.MOUSEBUTTONUP:
                pass

        pg.display.flip()  # Refresh on-screen display
        cntrl.clock.tick(60)         # wait until next frame (at 60 FPS)

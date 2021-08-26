"""tetris game"""

from figure import Figure
import sys
import pygame
from settings import *
from field import Field



def handle_game_event(field: Field, time) -> None:
    """ handling all game events like click some buttons"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # need to know boards of field to check collision
                field.figure.move_left()
            if event.key == pygame.K_RIGHT:
                field.figure.move_right()
            if event.key == pygame.K_SPACE:
                field.figure.turn()
    
    if time % 8 == 0:
        moving_down = field.figure.move_down()
        if not moving_down:
            coords = field.figure.get_cubes_coordinate()
            for coord in coords:
                x = coord[0]
                y = coord[1]

                field.fallen_cubes[y][x] = 1
                field.clear_full_row()
            field.figure = field.create_figure()
        time = 0
    time += 1
    return time


def update_screen(screen, field: Field) -> None:
    screen.fill(BLACK)
    field.draw()
    pygame.display.update()

def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SC, HEIGHT_SC))
    field = Field(screen, 250, 0)
    pygame.display.set_caption(TITLE)
    game = True
    time = 0
    while game:
        time = handle_game_event(field, time)
        update_screen(screen, field)
        clock.tick(FPS)


if __name__ == "__main__":
    main()

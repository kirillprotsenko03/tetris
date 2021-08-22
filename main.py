"""tetris game"""

import sys
from types import CellType
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
                field.figure.move_left((field.start_x, field.end_x))
            if event.key == pygame.K_RIGHT:
                field.figure.move_right((field.start_x, field.end_x))
    
    if time % 6 == 0:
        moving_down = field.figure.move_down()
        if not moving_down:
            for cube in field.figure.cubes:
                field.fallen_cubes.append(cube)
            field.figure = field.create_figure()
        time = 0
    time += 1
    print(time)
    return time


def update_screen(screen, field: Field) -> None:
    screen.fill(BLACK)
    field.draw()
    pygame.display.update()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SC, HEIGHT_SC))
    field = Field(screen)
    pygame.display.set_caption(TITLE)
    game = True
    time = 0
    while game:
        time = handle_game_event(field, time)
        update_screen(screen, field)
        clock.tick(FPS)


if __name__ == "__main__":
    main()

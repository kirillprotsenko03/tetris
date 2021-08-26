"""showing tetris field in screen, make a board to cube,
making map of fallen cubes"""


import random
import pygame
from settings import *
from figure import *



class Field:
    def __init__(self, screen, x: int, y: int) -> None:
        self.screen = screen
        self.screen_size = screen.get_size()

        self.start_x = x
        self.start_y = y
        self.end_x = x + CUBE_SIZE * 10
        self.end_y = y + CUBE_SIZE * 20

        self.fallen_cubes = [[0 for x in range(11)]
                             for y in range(21)]
        self.figure = self.create_figure()

    
    def create_figure(self) -> Figure:
        figures = [FirstFigure, SecondFigure, TherdFigure, FourthFigure, FiveFigure]
        figure = random.choice(figures)
        return figure(self.screen, self.fallen_cubes,
                      self.start_x, self.start_y)

    def clear_full_row(self) -> None:
        for y in range(21):
            x_count = 0
            for x in range(11):
                x_count += self.fallen_cubes[y][x]
            if x_count == 10:
                self._destroy_row(y)

    def _destroy_row(self, y: int) -> None:
        need_to_del = self.fallen_cubes[y]
        self.fallen_cubes.remove(need_to_del)
        new_row = [0 for x in range(11)]
        self.fallen_cubes = [new_row] + self.fallen_cubes


    def draw(self) -> None:
        # draw lines
        for y in range(21):
            pygame.draw.line(self.screen, WHITE,
                             (self.start_x, self.start_y + CUBE_SIZE * y),
                             (self.end_x, self.start_y + CUBE_SIZE * y))
        for x in range(11):
            pygame.draw.line(self.screen, WHITE,
                             (self.start_x + CUBE_SIZE * x, self.start_y),
                             (self.start_x + CUBE_SIZE * x, self.end_y))

        # draw figure
        coords = self.figure.get_cubes_coordinate()
        for coord in coords:
            x = coord[0] * CUBE_SIZE + self.start_x
            y = coord[1] * CUBE_SIZE + self.start_y
            pygame.draw.rect(self.screen, RED,
                             (x, y, CUBE_SIZE, CUBE_SIZE))
        
        # draw fallen figures
        for y in range(21):
            for x in range(11):
                if self.fallen_cubes[y][x]:
                        cube_x = self.start_x + x * CUBE_SIZE
                        cube_y = self.start_y + y * CUBE_SIZE
                        pygame.draw.rect(self.screen, RED,
                                         (cube_x, cube_y, 
                                         CUBE_SIZE, CUBE_SIZE))


            

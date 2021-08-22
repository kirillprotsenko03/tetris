"""showing tetris field in screen, make a board to cube,
making map of fallen cubes"""


import random
import pygame
from settings import *
from figure import *



class Field:
    def __init__(self, screen):
        self.screen = screen
        self.screen_size = screen.get_size()
        self.height_field = self.screen_size[1]
        self.width_field = self.height_field // 2

        self.start_x, self.end_x = self._get_x_board()
        self.start_y, self.end_y = self._get_y_board()

        self.fallen_cubes = []
        self.figure = self.create_figure()

    
    def create_figure(self) -> Figure:
        figures = (FirstFigure, SecondFigure)
        figure = random.choice(figures)
        return figure(self.screen, self.fallen_cubes)

    def _get_x_board(self) -> tuple:
        center_x = self.screen_size[0] // 2
        start_x = center_x - self.width_field // 2
        end_x = start_x + self.width_field
        return start_x, end_x

    def _get_y_board(self) -> tuple:
        start_y = 0
        end_y = self.height_field
        return start_y, end_y

    def draw(self) -> None:
        for i in range(11):
            x = self.start_x + i * CUBE_SIZE
            pygame.draw.line(self.screen, WHITE,
                            (x, self.start_y),
                            (x, self.end_y))

        for i in range(21):
            y = self.start_y + i * CUBE_SIZE
            pygame.draw.line(self.screen, WHITE,
                            (self.start_x, y),
                            (self.end_x, y))
        
        self.figure.draw()
        for cube in self.fallen_cubes:
            cube.draw(self.screen)

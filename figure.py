import random
from settings import *



class Figure:
    def __init__(self, screen, fallen_cubes: list,
                 field_start_x: int, field_start_y: int) -> None:
        self.screen = screen
        self.color = self._choose_color()
        self.fallen_cubes = fallen_cubes
        self.cubes = []
        self.field_start_x = field_start_x
        self.field_start_y = field_start_y
        self.x = 6
        self.y = -5
        self.width = 0
        self.height = 0

    def get_cubes_coordinate(self) -> list:
        coords = []
        for y in range(self.height):
            for x in range(self.width):
                if self.cubes[y][x]:
                    x_coord = (x + self.x)
                    y_coord = (y + self.y)
                    coords.append((x_coord, y_coord))
        return coords


    def move_down(self) -> bool:
        for y in range(self.height):
            for x in range(self.width):
                if self.cubes[y][x]:
                    x_coord = x + self.x
                    y_coord = y + self.y + 1
                    if self._is_collision(x_coord, y_coord):
                        return False
        if self.y + self.height >= 20:
            return False
        
        self.y += 1
        return True

    def move_left(self) -> bool:
        if self.x <= 0:
            return False
        for y in range(self.height):
            for x in range(self.width):
                if self.cubes[y][x]:
                    x_coord = x + self.x - 1
                    y_coord = y + self.y
                    if self._is_collision(x_coord, y_coord):
                        return False
        self.x -= 1

    def move_right(self) -> bool:
        if self.x + self.width >= 10:
            return False
        for y in range(self.height):
            for x in range(self.width):
                if self.cubes[y][x]:
                    x_coord = x + self.x + 1
                    y_coord = y + self.y
                    if self._is_collision(x_coord, y_coord):
                        return False
        self.x += 1

    def turn(self) -> bool:
        new_cubes = [[0 for y in range(self.height)]
                     for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                cube = self.cubes[y][x]
                new_y = x
                new_x = self.height - y - 1
                new_cubes[new_y][new_x] = cube
        self.cubes = new_cubes
        self.width, self.height = self.height, self.width
        

    def _is_collision(self, x: int, y: int) -> bool:
        if self.fallen_cubes[y][x] and x >= 0 and y >= 0:
            return True



    def _choose_color(self) -> tuple:
        colors = (RED, GREEN, BLUE)
        color = random.choice(colors)
        return color
    
    def _get_width(self) -> int:
        return len(self.cubes[0])

    def _get_height(self) -> int:
        return len(self.cubes)


class FirstFigure(Figure):
    def __init__(self, screen, fallen_cubes: list, 
                 field_start_x: int, field_start_y: int) -> None:
        super().__init__(screen, fallen_cubes, field_start_x, field_start_y)
        self.cubes = [[1],
                      [1],
                      [1],
                      [1]]
        self.width = self._get_width()
        self.height = self._get_height()
        

class SecondFigure(Figure):
    def __init__(self, screen, fallen_cubes: list, 
                 field_start_x: int, field_start_y: int) -> None:
        super().__init__(screen, fallen_cubes, field_start_x, field_start_y)
        self.cubes = [[1, 1],
                      [0, 1],
                      [0, 1],
                      [0, 1]]
        self.width = self._get_width()
        self.height = self._get_height()


class TherdFigure(Figure):
    def __init__(self, screen, fallen_cubes: list, 
                 field_start_x: int, field_start_y: int) -> None:
        super().__init__(screen, fallen_cubes, field_start_x, field_start_y)
        self.cubes = [[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]]
        self.width = self._get_width()
        self.height = self._get_height()


class FourthFigure(Figure):
    def __init__(self, screen, fallen_cubes: list, 
                 field_start_x: int, field_start_y: int) -> None:
        super().__init__(screen, fallen_cubes, field_start_x, field_start_y)
        self.cubes = [[0, 1],
                      [1, 1],
                      [0, 1]]
        self.width = self._get_width()
        self.height = self._get_height()

class FiveFigure(Figure):
    def __init__(self, screen, fallen_cubes: list,
                 field_start_x: int, field_start_y: int) -> None:
        super().__init__(screen, fallen_cubes, field_start_x, field_start_y)
        self.cubes = [[1, 1],
                      [1, 0],
                      [1, 0],
                      [1, 0]]
        self.width = self._get_width()
        self.height = self._get_height()

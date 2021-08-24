import random
from settings import *
from cube import Cube



class Figure:
    def __init__(self, screen, fallen_cubes) -> None:
        self.screen = screen
        self.color = self._choose_color()
        self.fallen_cubes = fallen_cubes
        self.cubes = []
        self.center_x = WIDTH_SC // 2

    def draw(self) -> None:
        for cube in self.cubes:
            cube.draw(self.screen)

    def move_down(self, board_x: tuple) -> bool:
        if not self._is_collision_down(board_x):
            for cube in self.cubes:
                x = cube.x
                y = cube.y + CUBE_SIZE
                cube.move(x, y)
            return True
        return False

    def move_left(self, board_x: tuple) -> None:
        if not self._is_collision_left(board_x):
            for cube in self.cubes:
                x = cube.x - CUBE_SIZE
                y = cube.y
                cube.move(x, y)

    def move_right(self, board_x: tuple) -> None:
        if not self._is_collision_right(board_x):
            for cube in self.cubes:
                x = cube.x + CUBE_SIZE
                y = cube.y
                cube.move(x, y)


    def _is_collision_down(self, board_x: tuple) -> bool:
        for cube in self.cubes:
            x = cube.x
            y = cube.y + CUBE_SIZE
            if cube.is_collision(x, y, self.fallen_cubes, board_x):
                return True
        return False

    def _is_collision_left(self, board_x: tuple) -> bool:
        for cube in self.cubes:
            x = cube.x - CUBE_SIZE
            y = cube.y
            if cube.is_collision(x, y, self.fallen_cubes, board_x):
                return True
        return False

    def _is_collision_right(self, board_x: tuple) -> bool:
        for cube in self.cubes:
            x = cube.x + CUBE_SIZE
            y = cube.y
            if cube.is_collision(x, y, self.fallen_cubes, board_x):
                return True
        return False


    def _choose_color(self) -> tuple:
        colors = (RED, GREEN, BLUE)
        color = random.choice(colors)
        return color


class FirstFigure(Figure):
    def __init__(self, screen, fallen_cubes) -> None:
        """this figure looks like this:
                    ###
                    ###
                    ###
        """
        super().__init__(screen, fallen_cubes)
        center_x = WIDTH_SC // 2
        self.cubes = [Cube(self.center_x + CUBE_SIZE * x, CUBE_SIZE * y, self.color)
                     for x in range(-1, 2)
                     for y in range(-3, 0)]
        

class SecondFigure(Figure):
    """this figure looks like this:

             #
             # 
             # 
             # 
             #  
    """
    def __init__(self, screen, fallen_cubes) -> None:
        super().__init__(screen, fallen_cubes)
        self.cubes = [Cube(self.center_x, -i * CUBE_SIZE, self.color)
                     for i in range(1, 6)]

class TherdFigure(Figure):
    """ this figure looks like this:
           ##
            # 
            # 
            # """
    def __init__(self, screen, fallen_cubes) -> None:
        super().__init__(screen, fallen_cubes)
        self.cubes = [Cube(self.center_x, -i * CUBE_SIZE, self.color)
                     for i in range(1, 5)]
        self.cubes.append(Cube(self.center_x - CUBE_SIZE, -CUBE_SIZE * 4, self.color))
    

class FourhtFigure(Figure):
    """this figure looks like this:
                #
               ## 
                # 
    """
    def __init__(self, screen, fallen_cubes) -> None:
        super().__init__(screen, fallen_cubes)
        self.cubes = [Cube(self.center_x, -i * CUBE_SIZE, self.color)
                     for i in range(1, 4)]
        self.cubes.append(Cube(self.center_x - CUBE_SIZE, -2 * CUBE_SIZE, self.color))
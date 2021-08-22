import pygame
from settings import CUBE_SIZE, HEIGHT_SC, WIDTH_SC


class Cube:
    def __init__(self, x: int, y: int,
                 color: tuple) -> None:
        self.x = x
        self.y = y
        self.color = color

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_collision(self, x: int, y: int, fallen_cubes: list,
                    x_board: tuple = (0,  WIDTH_SC)) -> bool:
        center_x = x + CUBE_SIZE // 2
        center_y = y + CUBE_SIZE // 2
        if center_y > HEIGHT_SC:
            return True
        if center_x < x_board[0] or center_x > x_board[1]:
            return True
        for cube in fallen_cubes:
            if cube.x < center_x < cube.x + CUBE_SIZE:
                if cube.y < center_y < cube.y + CUBE_SIZE:
                    return True
        return False

    def draw(self, screen) -> None:
        x = self.x
        y = self.y
        pygame.draw.rect(screen, self.color,
                        (x + 1, y + 1, CUBE_SIZE - 1, CUBE_SIZE - 1))
        
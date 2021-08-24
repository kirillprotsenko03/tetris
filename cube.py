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
                    x_board: tuple) -> bool:
        center_x = x + CUBE_SIZE // 2
        center_y = y + CUBE_SIZE // 2
        if center_y > HEIGHT_SC:
            return True
        if center_x < x_board[0] or center_x > x_board[1]:
            return True
        start_board_x = x_board[0]
        for y in range(21):
            for x in range(11):
                if fallen_cubes[y][x][0]:
                    cube_x = start_board_x + x * CUBE_SIZE
                    cube_y = y * CUBE_SIZE
                    if (cube_x < center_x and cube_x + CUBE_SIZE > center_x):
                        if (cube_y < center_y and cube_y + CUBE_SIZE > center_y):
                            return True
        return False

    def draw(self, screen) -> None:
        x = self.x
        y = self.y
        pygame.draw.rect(screen, self.color,
                        (x + 1, y + 1, CUBE_SIZE - 1, CUBE_SIZE - 1))

    @classmethod
    def draw_here(self, screen, x: int, y: int, color: tuple) -> None:
        pygame.draw.rect(screen, color,
                        (x + 1, y + 1, CUBE_SIZE - 1, CUBE_SIZE - 1))
        
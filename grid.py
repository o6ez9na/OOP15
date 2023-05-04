from random import randint
import pygame
from cell import Cell

CELL_SIZE = 40


class Grid:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.current_field = self.__make_base_map()
        self.next_field = self.__make_base_map()

    def __make_base_map(self):
        return [
            [Cell(width=CELL_SIZE, state=randint(0, 1),
                  cell_color=pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))) for j in
             range(self.__surface.get_height() // CELL_SIZE)] for i in
            range(self.__surface.get_width() // CELL_SIZE)]

    def __draw_new_map(self):
        for i, row in enumerate(self.current_field):
            for j, cell in enumerate(row):
                cell.topleft = (i * CELL_SIZE, j * CELL_SIZE)
                cell.draw(self.__surface)

    @staticmethod
    def make_new_map(source: list[list[Cell]], other: list[list[Cell]]):
        for i, row in enumerate(source):
            for j, cell in enumerate(row):
                source[i][j] = other[i][j]

    def find_collide_cell(self, position: tuple[int, int]):
        for i, row in enumerate(self.current_field):
            for j, cell in enumerate(row):
                if cell.collidepoint(position):
                    return cell, (i, j)

    def check_left(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x - 1][y].organism.is_alive

    def check_right(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x + 1][y].organism.is_alive

    def check_down(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x][y + 1].organism.is_alive

    def check_up(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x][y - 1].organism.is_alive

    def check_left_up(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x - 1][y - 1].organism.is_alive

    def check_left_down(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x - 1][y + 1].organism.is_alive

    def check_right_up(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x + 1][y - 1].organism.is_alive

    def check_right_down(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x + 1][y + 1].organism.is_alive

    def check_count_neighbors(self, position: tuple[int, int]):
        n, m = len(self.current_field) - 1, len(self.current_field[0]) - 1

        if position == (0, 0):
            count = self.check_right(position) + self.check_down(position) + self.check_right_down(position)
        elif position == (n, m):
            count = self.check_up(position) + self.check_left(position) + self.check_left_up(position)
        elif position == (0, m):
            count = self.check_up(position) + self.check_right(position) + self.check_right_up(position)
        elif position == (n, 0):
            count = self.check_left(position) + self.check_down(position) + self.check_left_down(position)
        else:
            if position[0] == 0:
                count = self.check_right(position) + self.check_up(position) + self.check_right_up(
                    position) + self.check_right_down(
                    position) + self.check_down(position)
            elif position[0] == n:
                count = self.check_up(position) + self.check_down(position) + self.check_left(
                    position) + self.check_left_down(
                    position) + self.check_left_up(position)
            elif position[1] == 0:
                count = self.check_left(position) + self.check_right(position) + self.check_down(
                    position) + self.check_left_down(
                    position) + self.check_right_down(position)
            elif position[1] == m:
                count = self.check_left(position) + self.check_right(position) + self.check_up(
                    position) + self.check_left_up(
                    position) + self.check_right_up(position)
            else:
                count = self.check_left(position) + self.check_right(position) + self.check_up(
                    position) + self.check_down(
                    position) + self.check_left_up(position) + self.check_left_down(position) + self.check_right_up(
                    position) + self.check_right_down(position)

        return count

    def update(self):
        self.make_new_map(self.current_field, self.next_field)

    def render(self):
        self.__draw_new_map()

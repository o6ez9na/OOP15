from grid import Grid
from rules import *


class Engine:
    def __init__(self, game_field: Grid):
        self.game_field = game_field

    def count_neighbors(self):
        for i, row in enumerate(self.game_field.current_field):
            for j, cell in enumerate(row):
                cell.organism.number_neighbors = self.game_field.check_count_neighbors((i, j))

    def run(self):
        self.count_neighbors()
        for row in self.game_field.current_field:
            for cell in row:
                Rule().run(cell)
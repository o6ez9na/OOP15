import pygame
from organism import *


class Cell(pygame.Rect):
    def __init__(self, width, state, x=0, y=0, cell_color: pygame.Color = pygame.Color(119, 221, 231),
                 border_color: pygame.Color = pygame.Color('forestgreen'),
                 border_width_alive: int = 0, border_width_dead: int = 1):
        super().__init__((x, y), (width, width))

        self.border_color = border_color
        self.cell_color = cell_color
        self.border_width_dead = border_width_dead
        self.border_width_alive = border_width_alive
        self.organism = Organism(state)

    def draw(self, surface: pygame.surface.Surface):
        color = self.cell_color if self.organism.is_alive else self.border_color
        border_width = self.border_width_alive if self.organism.is_alive else self.border_width_dead

        pygame.draw.rect(surface=surface, color=color, rect=self, width=border_width)

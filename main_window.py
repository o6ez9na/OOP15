import pygame
from grid import Grid

TITLE = "игра 'Жизнь'"


class MainWindow:
    def __init__(self, width: int, height: int, background_color: pygame.Color):
        pygame.init()
        self.surface = pygame.display.set_mode((width, height))
        self.__bg_color = background_color
        self.__game_field = Grid(self.surface)

        pygame.display.set_caption(TITLE)

    def render(self):
        self.surface.fill(self.__bg_color)
        self.__game_field.render()

    def update(self):
        self.__game_field.update()

    @property
    def background_color(self):
        return self.__bg_color

    @property
    def game_field(self):
        return self.__game_field

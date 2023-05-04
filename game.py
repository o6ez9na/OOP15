import pygame

from event import Event
from engine import Engine
from main_window import MainWindow


class Game:
    WIDTH = 3440
    HEIGHT = 1340

    def __init__(self):
        self.__main_window = MainWindow(Game.WIDTH, Game.HEIGHT, pygame.Color((168, 228, 160)))
        self.__game_engine = Engine(self.__main_window.game_field)

    def __update_event(self):
        Event().run()

    def __render(self):
        self.__main_window.render()

    def __update(self):
        self.__main_window.update()
        pygame.display.flip()
        pygame.time.Clock().tick(15)

    def run(self):
        while True:
            self.__update()
            self.__render()
            self.__update_event()
            self.__game_engine.run()

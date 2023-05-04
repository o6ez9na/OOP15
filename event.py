import pygame


class Event:
    @staticmethod
    def run():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


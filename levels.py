import pygame

class level1:
    def __init__(self , main) -> None:
        self.screen : pygame.surface.Surface = main.screen
        
    def run(self):
        self.screen.fill("white")
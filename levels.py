import pygame
import character
from constants import *

class level1:
    def __init__(self , main) -> None:
        self.screen : pygame.surface.Surface = main.screen
        self.character = pygame.sprite.Group()
        character.BaseCharacter(self.character , main)
        self.floor = pygame.surface.Surface((RES[0] , 100))

    def run(self , dt):
        key = pygame.key.get_pressed()
        self.screen.fill("white")
        self.character.draw(self.screen)
        self.screen.blit(self.floor , (0 , RES[1]-100))
        self.character.update(key , dt)

        #collisions

    
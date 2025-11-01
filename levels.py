import pygame
import character
from constants import *

class floor:
    def __init__(self):
        self.surface= pygame.surface.Surface((RES[0] , 100))
        self.rect= self.surface.get_rect(bottom=RES[1])

class level1:
    def __init__(self , main) -> None:
        self.screen : pygame.surface.Surface = main.screen
        self.character = character.BaseCharacter(self)
        self.floor = floor()

    def run(self , dt):
        key = pygame.key.get_pressed()
        self.screen.fill("white")
        self.character.draw(self.screen)
        self.screen.blit(self.floor.surface , self.floor.rect)
        #gravity
        if self.character.rect.bottom<self.floor.rect.top:
            self.character.falling=True
        else:
            self.character.velocity.y=0
            self.character.falling=False

        self.character.update(key , dt)
        #collisions


    
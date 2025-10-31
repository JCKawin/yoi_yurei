import pygame
import character

class level1:
    def __init__(self , main) -> None:
        self.screen : pygame.surface.Surface = main.screen
        self.character = pygame.sprite.Group()
        character.BaseCharacter(self.character , main)
        
    def run(self , dt):
        key = pygame.key.get_pressed()
        self.screen.fill("white")
        self.character.draw(self.screen)
        self.character.update(key , dt)

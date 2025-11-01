import pygame
from constants import *

class BaseCharacter(pygame.sprite.Sprite):
    def __init__(self , group , main):
        super().__init__(group)
        self.image = pygame.Surface((100 , 100))
        self.rect = self.image.get_frect()
        self.rect.center = main.screen.get_rect().center
        self.direction = pygame.Vector2(0,0)
        self.velocity = 1
        self.gravity = pygame.Vector2(0,-9.8)

    def update(self , key , dt):
        self.direction.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
        self.rect.x += ( self.direction.x * self.velocity) * dt #type: ignore
        if key[pygame.K_SPACE]:
            self.rect.y -= 20 * dt


        if self.rect.bottom > RES[1] - 100:
            self.rect.y -= 0
        else:
            self.rect.y += 0.9 * dt
            

        
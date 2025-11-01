import pygame
from constants import *

class BaseCharacter(pygame.sprite.Sprite):
    def __init__(self , main):
        self.image = pygame.Surface((100 , 100))
        self.rect = self.image.get_frect()
        self.rect.center = main.screen.get_rect().center
        # self.direction = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(1,0)
        self.falling=False
        self.gravity = pygame.Vector2(0,-9.8)

    def draw(self , screen):
        screen.blit(self.image , self.rect)


    def update(self , key , dt):
        self.velocity.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
        key_get = pygame.key.get_just_pressed()
        if self.falling:
            self.velocity.y+=GRAVITY*dt
        if key_get[pygame.K_SPACE]:
            print("space pressed",dt)
            self.velocity.y -= 20 * dt

        self.rect.center += self.velocity * dt

        
            

        
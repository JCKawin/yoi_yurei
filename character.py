from tkinter import W
import pygame
from constants import *

def get_sign(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    else:
        return 0


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

        #apply drag
        key_get = pygame.key.get_just_pressed()
        if not (key_get[pygame.K_a] or key_get[pygame.K_d]):
            self.velocity.x-= get_sign(self.velocity.x)*DRAG
        if abs(self.velocity.x)<0.09:
            self.velocity.x=0

        #run
        self.velocity.x += RUN*(int(key[pygame.K_d])-int(key[pygame.K_a]))
        if abs(self.velocity.x)>RUN_CAP:
            self.velocity.x=RUN_CAP*get_sign(self.velocity.x)

        #gravity
        if self.falling:
            self.velocity.y += GRAVITY #* (FPS/144)
        if key_get[pygame.K_SPACE] and not self.falling:
            # print("space pressed",dt)
            self.velocity.y =  -JUMP_HEIGHT #* (FPS/144)
            # print(self.velocity)

        self.rect.center += self.velocity #* (FPS/144)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>RES[0]:
            self.rect.right=RES[0]
        
            

        
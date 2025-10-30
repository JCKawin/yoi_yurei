import pygame

class BaseCharacter(pygame.sprite.Sprite):
    def __init__(self , group , main):
        super().__init__(group)
        self.image = pygame.Surface((100 , 100))
        self.rect.center = main.screen.get_rect().center
        self.direction = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)

    def update(self , key , dt):+
        self.direction.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
        self.direction.y = int(key[pygame.K_w]) - int(key[pygame.K_s])
        self.direction = self.direction.normalize if self.direction else self.direction
        self.rect += ( self.direction * self.velocity + self.gravity ) * dt
import pygame

class start_screen:
    def __init__(self , screen : pygame.surface.Surface , font : pygame.font.Font):
        self.screen = screen
        self.font = font

    def run(self):
        self.screen.fill("black")
        text = self.font.render("START" , True , "#ffdf00")
        text_rect = text.get_rect()
        text_rect.center = self.screen.get_rect().center
        self.screen.blit(text , text_rect)


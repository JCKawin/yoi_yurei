import pygame
from constants import *
import sys
from os.path import join

class Main():
    def __init__(self):
        pygame.init()
        try : pygame.mixer.init()
        except : print("NO Sound Device Detected")
        try : 
            pygame.display.init()
            self.screen = pygame.display.set_mode(RES)
            pygame.display.set_icon(pygame.image.load(join("img", "logo.png")).convert_alpha())
            pygame.display.set_caption("良い幽霊") 

        except: print("NO Display found")



        self._load()
        self.clock = pygame.time.Clock()
        self.running = True

    def _load(self):
        #images
        self.logo = pygame.image.load(join("img", "logo.png")).convert_alpha()

        #audio
        pygame.mixer.music.load(join("audio" ,"theme_music.ogg"),"ogg")

        #font
        
    

    def run(self):
        pygame.mixer.music.play(loops=-1)
        while self.running:
            pygame.mixer.music.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill(BG_COLOR)
            pygame.display.flip()

        else:
            self._gameover()
    
    def _gameover(self):
        pass

    def __del__(self):
        pygame.quit()

if __name__ == "__main__":
    Game : Main = Main()
    Game.run()

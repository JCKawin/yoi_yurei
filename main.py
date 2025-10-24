import pygame
from constants import *
import sys

class Main():
    def __init__(self):
        pygame.init()
        try : pygame.mixer.init()
        except : print("NO Sound Device Detected")
        try : 
            pygame.display.init()
            self.screen = pygame.display.set_mode(RES) 

        except: print("NO Display found")



        self._load()
        self.clock = pygame.time.Clock()
        self.running = True

    def _load(self):
        pass

    def run(self):
        while self.running:
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

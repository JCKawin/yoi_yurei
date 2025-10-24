import pygame

class Main():
    def __init__(self):
        pygame.init()
        self._load()
        self.running = True
    def _load(self):
        pass

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    break

        else:
            self._gameover()
    
    def _gameover(self):
        pass

    def __del__(self):
        pygame.quit()

if __name__ == "__main__":
    Game : Main = Main()
    Game.run()

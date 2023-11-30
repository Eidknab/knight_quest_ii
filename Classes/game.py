import pygame
from Classes.map_world import *
from config import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(GNAME)
        self.map_world = Map_world('background', (640, 480), 16, (1, 1), (38, 28), (19, 14), 16, 16, 16, 16)
        self.map_world.background_generate()
        self.map_world.map_world_default_generate()
        self.background = pygame.image.load('Assets/background.png')
        
    def gameloop(self):
        gamelooping = True
        while gamelooping:
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamelooping = False
        pygame.quit()
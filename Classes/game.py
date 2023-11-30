import pygame
from Classes.map_world import *
from Classes.characters import *
from config import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(GNAME)
        self.map_world = Map_world('background', (640, 480), 16, (1, 1), (38, 28), (19, 14), 16, 16, 16, 16)
        self.map_world.background_generate()
        self.map_world.map_world_default_generate()
        self.background = pygame.image.load('Assets/background.png')
        # 
        zombie_counter = 1
        wolf_counter = 1
        skeleton_counter = 1
        chest_counter = 1
        for i, row in enumerate(self.map_world.map_world_default.ascii_map):
            for j, char in enumerate(row):
                position = j*self.map_world.map_world_default.tile, i*self.map_world.map_world_default.tile
                if char == '@':
                    self.player = Character('player', 'eidknab', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                elif char == 'B':
                    self.boss = Character('boss', 'zebhrn', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                elif char == 'M':
                    self.merchant = Character('merchant', 'knabresuu', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                elif char == 'z':
                    zombie = Character('zombie', 'zombie', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    setattr(self, f"zombie{zombie_counter}", zombie)
                    zombie_counter += 1
                elif char == 'w':
                    wolf = Character('wolf', 'wolf', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    setattr(self, f"wolf{wolf_counter}", wolf)
                    wolf_counter += 1
                elif char == 's':
                    skeleton = Character('skeleton', 'skeleton', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    setattr(self, f"skeleton{skeleton_counter}", skeleton)
                    skeleton_counter += 1
                    
    def gameloop(self):
        gamelooping = True
        while gamelooping:
            # world map display refresh
            self.screen.blit(self.background, (0, 0))
            # player, boss, merchant
            self.screen.blit(self.player.image, self.player.position)
            self.screen.blit(self.boss.image, self.boss.position)
            self.screen.blit(self.merchant.image, self.merchant.position)
            # monsters
            for attr in dir(self):
                if 'zombie' in attr:
                    zombie = getattr(self, attr)
                    self.screen.blit(zombie.image, zombie.position)
                if 'wolf' in attr:
                    wolf = getattr(self, attr)
                    self.screen.blit(wolf.image, wolf.position)
                if 'skeleton' in attr:
                    skeleton = getattr(self, attr)
                    self.screen.blit(skeleton.image, skeleton.position)
            # Scenery
            for i, row in enumerate(self.map_world.map_world_default.ascii_map):
                for j, char in enumerate(row):
                    position = j*self.map_world.map_world_default.tile, i*self.map_world.map_world_default.tile
                    if char == ',':
                        herb = pygame.image.load('Assets/herb2.png')
                        self.screen.blit(herb, position)
                    elif char == '$':
                        chest = pygame.image.load('Assets/chest.png')
                        self.screen.blit(chest, position)
                    elif char == '-':
                        hwall = pygame.image.load('Assets/hwall.png')
                        self.screen.blit(hwall, position)
                    elif char == '|':
                        vwall = pygame.image.load('Assets/vwall.png')
                        self.screen.blit(vwall, position)
                    elif char == '┌':
                        corner1 = pygame.image.load('Assets/corner1.png')
                        self.screen.blit(corner1, position)
                    elif char == '┐':
                        corner2 = pygame.image.load('Assets/corner2.png')
                        self.screen.blit(corner2, position)
                    elif char == '┘':
                        corner3 = pygame.image.load('Assets/corner3.png')
                        self.screen.blit(corner3, position)
                    elif char == '└':
                        corner4 = pygame.image.load('Assets/corner4.png')
                        self.screen.blit(corner4, position)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamelooping = False
        pygame.quit()
        
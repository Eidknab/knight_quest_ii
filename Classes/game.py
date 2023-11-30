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
            # player, boss, merchant
            self.screen.blit(self.player.image, self.player.position)
            self.screen.blit(self.boss.image, self.boss.position)
            self.screen.blit(self.merchant.image, self.merchant.position)
            # move the player
            

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamelooping = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move(self.player, 'up')
                    if event.key == pygame.K_DOWN:
                        self.move(self.player, 'down')
                    if event.key == pygame.K_RIGHT:
                        self.move(self.player, 'right')
                    if event.key == pygame.K_LEFT:
                        self.move(self.player, 'left')
        pygame.quit()
    
    def move_up(self, character, direction):
        character.position = (character.position[0], character.position[1] - 16)
        for i, row in enumerate(self.map_world.map_world_default.ascii_map):
            for j, char in enumerate(row):
                position = j*self.map_world.map_world_default.tile, i*self.map_world.map_world_default.tile
                if character.position == position:
                    if char == '$':
                        character.gold += 10
                        self.map_world.map_world_default.ascii_map[i][j] = '.'
                        print(character.gold)
                    elif char == '-':
                        character.position = (character.position[0], character.position[1] +16)
                        print('wall coliision')
                    elif char == '|':
                        character.position = (character.position[0], character.position[1] +16)
                        print('wall coliision')

    def move(self, character, direction):
        if direction == 'up':
            y = -self.map_world.map_world_default.tile
            x = 0
        elif direction == 'down':
            y = self.map_world.map_world_default.tile
            x = 0
        elif direction == 'right':
            y = 0
            x = self.map_world.map_world_default.tile
        elif direction == 'left':
            y = 0
            x = -self.map_world.map_world_default.tile
        character.position = (character.position[0] + x, character.position[1] + y)
        map_width = len(self.map_world.map_world_default.ascii_map[0]) * self.map_world.map_world_default.tile
        map_height = len(self.map_world.map_world_default.ascii_map) * self.map_world.map_world_default.tile
        if character.position[0] < 0 or character.position[0] >= map_width or character.position[1] < 0 or character.position[1] >= map_height:
            character.position = (character.position[0] - x, character.position[1] - y)
            print('outside the disc world')
        for i, row in enumerate(self.map_world.map_world_default.ascii_map):
            for j, char in enumerate(row):
                position = j*self.map_world.map_world_default.tile, i*self.map_world.map_world_default.tile
                if character.position == position:
                    if char == '$':
                        character.gold += 10
                        self.map_world.map_world_default.ascii_map[i][j] = '.'
                        print(character.gold)
                    elif char in ('-', '|', '┌', '┐', '┘', '└'):
                        character.position = (character.position[0] - x, character.position[1] - y)
                        print('wall or corner')
                    elif char == '~':
                        character.position = (character.position[0] - x, character.position[1] - y)
                        print('water')
    
        
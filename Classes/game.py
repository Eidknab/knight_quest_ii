import pygame
from Classes.map_world import *
from Classes.characters import *
from config import *

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(GNAME)
        self.map_world = Map_world('background', (640, 480), 16, (1, 1), (38, 28), (19, 14), 16, 16, 16, 16)
        self.map_world.background_generate()
        self.map_world.map_world_default_generate()
        pygame.font.init()
        self.font1 = pygame.font.Font(None, 48)
        self.font2 = pygame.font.Font(None, 32)
        self.font3 = pygame.font.Font(None, 24)
        self.font4 = pygame.font.Font(None, 16)
        zombie_counter = 1
        wolf_counter = 1
        skeleton_counter = 1
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
                self.menu = True
                    
    def gameloop(self):
        gamelooping = True
        while gamelooping:
            # world map display refresh
            self.background = pygame.image.load('Assets/background.png')
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
            self.screen.blit(self.boss.image, self.boss.position)
            self.screen.blit(self.merchant.image, self.merchant.position)
            self.screen.blit(self.player.image, self.player.position)
            pygame.display.flip()
            self.display_menu()
            # Move
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
                    if event.key == pygame.K_ESCAPE:
                        self.menu = True
                        self.display_menu()
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
            print('outside the discworld')
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
                        print('wall')
                    elif char in ('.', ','):
                        print('grass')
                    elif char == '~':
                        character.position = (character.position[0] - x, character.position[1] - y)
                        print('water')
                    elif char == 'B':
                        print('boss')
                    elif char == 'M':
                        print('merchant')
                    elif char == 'z':
                        print('zombie')
                    elif char == 'w':
                        print('wolf')
                    elif char == 's':
                        print('skeleton')
    def display_menu(self):
        self.clock.tick(30)
        red1 = red2 = red3 = red4 = 255
        green1 = green2 = green3 = green4 = 255
        blue1 = blue2 = blue3 = blue4 = 255
        select = 2
        direction = -0.0625
        while self.menu == True:
            self.text = self.font1.render("- KNIGHT QUEST II -", True, (255, 255, 255, 255))
            self.screen.blit(self.text, (170, 32))
            self.text = self.font2.render("Start Game", True, (red2, green2, blue2, 255))
            self.screen.blit(self.text, (266, 92))
            self.text = self.font2.render("Load Game", True, (red3, green3, blue3, 255))
            self.screen.blit(self.text, (268, 132))
            self.text = self.font2.render("Quit", True, (red4, green4, blue4, 255))
            self.screen.blit(self.text, (296, 164))
            self.text = self.font4.render("PLAYER", True, (64, 192, 64))
            self.screen.blit(self.text, (6, 4))
            self.text = self.font4.render("BOSS", True, (192, 64, 64))
            self.screen.blit(self.text, (298, 212))
            self.text = self.font4.render("VENDOR", True, (192, 0, 192))
            self.screen.blit(self.text, (592, 438))
            
            red1 += direction
            green1 += direction
            blue1 += direction
            if select == 2:
                red2 += direction
                green2 += direction
                blue2 += direction
                red3 = green3 = blue3 = red4 = green4 = blue4 = 192
            if select == 3:
                red3 += direction
                green3 += direction
                blue3 += direction
                red2 = green2 = blue2 = red4 = green4 = blue4 = 192
            if select == 4:
                red4 += direction
                green4 += direction
                blue4 += direction
                red2 = green2 = blue2 = red3 = green3 = blue3 = 192
            if red1 == 192 or red1 == 255:
                direction *= -1
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu = False
                    if event.key == pygame.K_DOWN:
                        if select < 4:
                            select += 1
                    if event.key == pygame.K_UP:
                        if select > 1:
                            select -= 1
                    if event.key == pygame.K_RETURN:
                        if select == 2:
                            self.menu = False
                        if select == 3:
                            print('Load Game')
                        if select == 4:
                            self.menu = False
                            pygame.quit()
                

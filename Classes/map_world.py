import numpy as np
import pygame
from random import randint

class Map_world:
    def __init__(self, name, size, tile, player_position, merchant_position, boss_position,
                 howmany_chest, howmany_monster1, howmany_monster2, howmany_monster3, 
                 ):
        # Attributs
        self.ascii_map = None
        self.name = name
        self.size = size
        self.tile = tile
        self.player_position = player_position
        self.merchant_position = merchant_position
        self.boss_position = boss_position
        self.howmany_chest = howmany_chest
        self.howmany_monster1 = howmany_monster1
        self.howmany_monster2 = howmany_monster2
        self.howmany_monster3 = howmany_monster3
        self.ascii_herb1 = '.'
        self.ascii_herb2 = ','
        self.ascii_water = '~'
        self.ascii_bridge = 'b'
        self.ascii_chest = '$'
        self.ascii_hwall = '-'
        self.ascii_vwall = '|'
        self.ascii_corner1 = '┌'
        self.ascii_corner2 = '┐'
        self.ascii_corner3 = '┘'
        self.ascii_corner4 = '└'
        self.ascii_monster1 = 'z'
        self.ascii_monster2 = 's'
        self.ascii_monster3 = 'w'
        self.ascii_player = '@'
        self.ascii_boss = 'B'
        self.ascii_merchant = 'M'
        self.tile_herb1 = 'assets/herb1.png'
        self.tile_herb2 = 'assets/herb2.png'
        self.tile_water = 'assets/water.png'
        self.tile_bridge = 'assets/bridge.png'
        self.tile_chest = 'assets/chest.png'
        self.tile_hwall = 'assets/hwall.png'
        self.tile_vwall = 'assets/vwall.png'
        self.tile_corner1 = 'assets/corner1.png'
        self.tile_corner2 = 'assets/corner2.png'
        self.tile_corner3 = 'assets/corner3.png'
        self.tile_corner4 = 'assets/corner4.png'
        self.tile_player = 'assets/player.png'
        self.tile_monster1 = 'assets/zombie.png'
        self.tile_monster2 = 'assets/skeleton.png'
        self.tile_monster3 = 'assets/wolf.png'
        self.tile_boss = 'assets/boss.png'
        self.tile_merchant = 'assets/merchant.png'
        # ASCII Map pre-generation (herb1)
        self.ascii_map = [[self.ascii_herb1 for _ in range(self.size[0] // self.tile)] for _ in range(self.size[1] // self.tile)]
        
    def add_herb_variation(self,):
        howmany_herb1 = ((self.size[0] // self.tile) * (self.size[1] // self.tile) // 2) - (3 + self.howmany_chest + self.howmany_monster1 + self.howmany_monster2 + self.howmany_monster3)
        i = 0
        while i < howmany_herb1:
            x = np.random.randint(0, self.size[0] // self.tile)
            y = np.random.randint(0, self.size[1] // self.tile)
            if self.ascii_map[y][x] == self.ascii_herb1:
                self.ascii_map[y][x] = self.ascii_herb2
                i += 1
    
    def add_river(self):
        x, y = np.random.choice([0, self.size[0] // self.tile - 1]), np.random.randint(0, self.size[1] // self.tile)
        direction = 1 if x == 0 else -1
        while 0 <= x < self.size[0] // self.tile:
            self.ascii_map[y][x] = self.ascii_water
            y += np.random.choice([-1, 0, 1])
            y = max(min(y, self.size[1] // self.tile - 1), 0)
            x += direction
            
    def add_bridges(self):
        b = randint(1,3) # number of bridges
        i = 0
        while i < b:
            x = np.random.randint(0, self.size[0] // self.tile)
            y = np.random.randint(0, self.size[1] // self.tile)
            if self.ascii_map[y][x] == self.ascii_water:
                self.ascii_map[y][x] = self.ascii_bridge
                i += 1

    def add_uniques(self,):
        try: self.ascii_map[self.player_position[1]][self.player_position[0]] = self.ascii_player
        except: pass
        try: self.ascii_map[self.merchant_position[1]][self.merchant_position[0]] = self.ascii_merchant
        except: pass
        try: self.ascii_map[self.boss_position[1]][self.boss_position[0]] = self.ascii_boss
        except: pass

    def add_chests(self,):
        i = 0
        while i < self.howmany_chest:
            x = np.random.randint(0, self.size[0] // self.tile)
            y = np.random.randint(0, self.size[1] // self.tile)
            if (
                x-1 >= 0 and x+1 < (self.size[0] // self.tile) and
                y-1 >= 0 and y+1 < (self.size[1] // self.tile) and
                self.ascii_map[y][x] == self.ascii_herb1 and
                self.ascii_map[y-1][x] == self.ascii_herb1 and
                self.ascii_map[y][x-1] == self.ascii_herb1 and
                self.ascii_map[y][x+1] == self.ascii_herb1 and
                self.ascii_map[y-1][x-1] == self.ascii_herb1 and
                self.ascii_map[y-1][x+1] == self.ascii_herb1
                ):
                self.ascii_map[y][x] = self.ascii_chest
                self.ascii_map[y-1][x] = self.ascii_hwall
                self.ascii_map[y][x-1] = self.ascii_vwall
                self.ascii_map[y][x+1] = self.ascii_vwall
                self.ascii_map[y-1][x-1] = self.ascii_corner1
                self.ascii_map[y-1][x+1] = self.ascii_corner2
                i += 1

    def add_monsters(self,):
        i = 0
        while i < self.howmany_monster1:
            x = np.random.randint(0, self.size[0] // self.tile)
            y = np.random.randint(0, self.size[1] // self.tile)
            if self.ascii_map[y][x] == self.ascii_herb1:
                self.ascii_map[y][x] = self.ascii_monster1
                i += 1
        i = 0
        while i < self.howmany_monster2:
            x = np.random.randint(0, self.size[0] // self.tile)
            y = np.random.randint(0, self.size[1] // self.tile)
            if self.ascii_map[y][x] == self.ascii_herb1:
                self.ascii_map[y][x] = self.ascii_monster2
                i += 1
        i = 0
        while i < self.howmany_monster3:
            x = np.random.randint(0, self.size[0] // self.tile)
            y = np.random.randint(0, self.size[1] // self.tile)
            if self.ascii_map[y][x] == self.ascii_herb1:
                self.ascii_map[y][x] = self.ascii_monster3
                i += 1

    def ascii_map_display(self,):
        for y in range(self.size[1] // self.tile):
            for x in range(self.size[0] // self.tile):
                print(self.ascii_map[y][x], end='')
            print()
            
    def create_tiled_map(self):
        map_surface = pygame.Surface(self.size)
        for y in range(self.size[1] // self.tile):
            row = []
            for y in range(self.size[1] // self.tile):
                for x in range(self.size[0] // self.tile):
                    if self.ascii_map[y][x] == self.ascii_herb1:
                        tile = pygame.image.load(self.tile_herb1)
                    elif self.ascii_map[y][x] == self.ascii_herb2:
                        tile = pygame.image.load(self.tile_herb2)
                    elif self.ascii_map[y][x] == self.ascii_water:
                        tile = pygame.image.load(self.tile_water)
                    elif self.ascii_map[y][x] == self.ascii_bridge:
                        tile = pygame.image.load(self.tile_bridge)
                    elif self.ascii_map[y][x] == self.ascii_chest:
                        tile = pygame.image.load(self.tile_chest)
                    elif self.ascii_map[y][x] == self.ascii_hwall:
                        tile = pygame.image.load(self.tile_hwall)
                    elif self.ascii_map[y][x] == self.ascii_vwall:
                        tile = pygame.image.load(self.tile_vwall)
                    elif self.ascii_map[y][x] == self.ascii_corner1:
                        tile = pygame.image.load(self.tile_corner1)
                    elif self.ascii_map[y][x] == self.ascii_corner2:
                        tile = pygame.image.load(self.tile_corner2)
                    elif self.ascii_map[y][x] == self.ascii_player:
                        tile = pygame.image.load(self.tile_player)
                    elif self.ascii_map[y][x] == self.ascii_monster1:
                        tile = pygame.image.load(self.tile_monster1)
                    elif self.ascii_map[y][x] == self.ascii_monster2:
                        tile = pygame.image.load(self.tile_monster2)
                    elif self.ascii_map[y][x] == self.ascii_monster3:
                        tile = pygame.image.load(self.tile_monster3)
                    elif self.ascii_map[y][x] == self.ascii_boss:
                        tile = pygame.image.load(self.tile_boss)
                    elif self.ascii_map[y][x] == self.ascii_merchant:
                        tile = pygame.image.load(self.tile_merchant)
                    map_surface.blit(tile, (x * self.tile, y * self.tile))
            pygame.image.save(map_surface, 'Assets/' + self.name + '.png')

    def background_generate(self):
        self.background = Map_world('background', (640, 480), 16, (1, 1), (38, 28), (19, 14), 16, 16, 16, 16)
        self.background.add_river()
        self.background.add_bridges()
        self.background.ascii_map_display()
        self.background.create_tiled_map()
        print(f'{self.background.name}.png generated !')
        pass

    def map_world_default_generate(self):
        self.map_world_default = Map_world('map_world_default', (640, 480), 16, (1, 1), (38, 28), (19, 14), 16, 16, 16, 16)
        self.map_world_default.ascii_map = [row[:] for row in self.background.ascii_map]
        self.map_world_default.add_uniques()
        self.map_world_default.add_chests()
        self.map_world_default.add_monsters()
        self.map_world_default.add_herb_variation()
        self.map_world_default.ascii_map_display()
        self.map_world_default.create_tiled_map()
        print(f'{self.map_world_default.name}.png generated !')
        pass

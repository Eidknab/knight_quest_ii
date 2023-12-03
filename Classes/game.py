import pygame
from Classes.map_world import *
from Classes.characters import *
from random import randint
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
        self.characters_dict = {}
        for i, row in enumerate(self.map_world.map_world_default.ascii_map):
            for j, char in enumerate(row):
                position = j*self.map_world.map_world_default.tile, i*self.map_world.map_world_default.tile
                if char == '@':
                    self.player = Character('player', 'eidknab', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                elif char == 'B':
                    self.boss = Character('boss', 'zebhrn', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    self.characters_dict[self.boss.character_type] = self.boss.position
                elif char == 'M':
                    self.merchant = Character('merchant', 'knabresuu', position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    self.characters_dict[self.merchant.character_type] = self.merchant.position
                elif char == 'z':
                    namemonster = 'zombie' + str(zombie_counter)
                    zombie = Character('zombie', namemonster, position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    setattr(self, f"zombie{zombie_counter}", zombie)
                    self.characters_dict[f"zombie{zombie_counter}"] = zombie.position
                    zombie_counter += 1
                elif char == 'w':
                    namemonster = 'wolf' + str(wolf_counter)
                    wolf = Character('wolf', namemonster, position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    setattr(self, f"wolf{wolf_counter}", wolf)
                    self.characters_dict[f"wolf{wolf_counter}"] = wolf.position
                    wolf_counter += 1
                elif char == 's':
                    namemonster = 'skeleton' + str(skeleton_counter)
                    skeleton = Character('skeleton', namemonster, position, 50, 1, 100, 0, 100, 100, 40, 40, 20, 20, 10, 20, 5, 1, 100, [], [])
                    setattr(self, f"skeleton{skeleton_counter}", skeleton)
                    self.characters_dict[f"skeleton{skeleton_counter}"] = skeleton.position
                    skeleton_counter += 1
                self.menu = True
        # print characters_dict in console
        for i in self.characters_dict:
            print(i, self.characters_dict[i])
        global_counter = 3 + zombie_counter-1 + wolf_counter-1 + skeleton_counter-1
        print(f"{global_counter} characters generated !")
        
    def gameloop(self):
        gamelooping = True
        pygame.mixer.music.load('Assets/Sounds/music_world.ogg')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
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
            if self.isalive(self.boss) == True:
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
        
    def fight_colision(self, position):
        for key, value in self.characters_dict.items():
            if value == position:
                print(f"player: {position} {key}: {value}")
                return key
        pass
    
    def fight_start(self, monster_name):
        fight = True
        pygame.mixer.music.pause()
        while fight:
            self.background = pygame.image.load('Assets/fight_background.png')
            self.player_img = pygame.image.load('Assets/player.png')
            self.player_zoom = pygame.transform.scale(self.player_img, (48, 48))
            monster = getattr(self, monster_name)
            monster_type = monster.character_type
            self.monster_img = pygame.image.load('Assets/' + monster_type + '.png')
            # must be blited first
            self.screen.blit(self.background, (0, 0))
            # zoom and flip
            self.monster_flp = pygame.transform.flip(self.monster_img, True, False)
            if monster_type == 'boss':
                self.monster_zoom = pygame.transform.scale(self.monster_flp, (96, 96))
                self.screen.blit(self.monster_zoom, (460, 240))
            else:
                self.monster_zoom = pygame.transform.scale(self.monster_flp, (48, 48))
                self.screen.blit(self.monster_zoom, (500, 280))
            self.screen.blit(self.player_zoom, (120, 280))
            self.text = self.font1.render("FIGHT", True, (255, 255, 255, 255))
            self.screen.blit(self.text, (270, 32))
            self.text = self.font3.render(f"{self.player.hp} / {self.player.hp_max}", True, (255, 32, 32, 255))
            self.screen.blit(self.text, (10, 360))
            self.text = self.font3.render(f"{self.player.mp} / {self.player.mp_max}", True, (32, 32, 255, 255))
            self.screen.blit(self.text, (10, 384))
            self.text = self.font3.render(f"{monster.hp} / {monster.hp_max}", True, (255, 32, 32, 255))
            self.screen.blit(self.text, (560, 360))
            self.text = self.font3.render(f"{monster.mp} / {monster.mp_max}", True, (32, 32, 255, 255))
            self.screen.blit(self.text, (560, 384))
            self.text = self.font3.render(f"Press Escape", True, (255, 255, 255, 255))
            self.screen.blit(self.text, (10, 10))
            player_action = self.menu_creator(('attack', 'magic', 'special', 'item'), [120, 360],)
            if player_action == False:
                fight = False
            elif player_action == 'attack':
                damage = self.attack(self.player, monster)
                if self.isalive(monster) == False:
                    fight = False
                    x = monster.position[0]
                    y = monster.position[1]
                    self.map_world.map_world_default.ascii_map[y//16][x//16] = ','
                    del self.characters_dict[monster_name]
                    del monster
                    print(f"{monster_name} is dead !")
                    print(self.characters_dict)
                    self.map_world.map_world_default.ascii_map_display()
            elif player_action == 'magic':
                print("magic")
            elif player_action == 'special':
                print("special")
            elif player_action == 'item':
                print("item")
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("out of the fight")
                        pygame.mixer.music.rewind()
                        pygame.mixer.music.unpause()
                        fight = False
        pass

    def attack(self, attacker='player', defender='monster'):
        print(f"{attacker} is attacking {defender}")
        damage = attacker.strength
        damage -= defender.armor
        damage = randint(damage-5, damage+5)
        if randint(0, 100) <= (attacker.critical + (attacker.level-defender.level)*5):
            damage *= 1.5
            print("critical hit !")
        defender.hp -= damage
        print(f"{damage} damage")
        pass
    
    def isalive(self, character):
        if character.hp > 0:
            return True
        else:
            character.hp = 0
            return False
    
    def move(self, character, direction):
        grass_snd = pygame.mixer.Sound('Assets/Sounds/grass.wav')
        wall_snd = pygame.mixer.Sound('Assets/Sounds/wall.wav')
        water_snd = pygame.mixer.Sound('Assets/Sounds/water.wav')
        bridge_snd = pygame.mixer.Sound('Assets/Sounds/bridge.wav')
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
                        wall_snd.play()
                        print('wall')
                    elif char in ('.', ','):
                        grass_snd.play()
                        print('grass')
                    elif char == '~':
                        character.position = (character.position[0] - x, character.position[1] - y)
                        water_snd.play()
                        print('water')
                    elif char == 'b':
                        bridge_snd.play()
                        print('bridge')
                    elif char == 'M':
                        print('merchant')
                    elif char == 'z' or char == 'w' or char == 's' or char == 'B':
                        fight = self.fight_colision(position)
                        print (f"fight with {fight}")
                        self.fight_start(fight)
                        
    def display_menu(self):
        self.clock.tick(30)
        red1 = red2 = red3 = red4 = 255
        green1 = green2 = green3 = green4 = 255
        blue1 = blue2 = blue3 = blue4 = 255
        select = 2
        direction = -0.0625
        select_snd = pygame.mixer.Sound('Assets/Sounds/select.ogg')
        confirm_snd = pygame.mixer.Sound('Assets/Sounds/confirm.ogg')
        critical_snd = pygame.mixer.Sound('Assets/Sounds/critical.ogg')
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
            player_position = self.player.position[0]-16, self.player.position[1]-12
            self.screen.blit(self.text, (player_position))
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
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu = False
                    if event.key == pygame.K_DOWN:
                        if select < 4:
                            select += 1
                        select_snd.play()
                    if event.key == pygame.K_UP:
                        if select > 1:
                            select -= 1
                        select_snd.play()
                    if event.key == pygame.K_RETURN:
                        if select == 2:
                            self.menu = False
                            confirm_snd.play()
                        if select == 3:
                            print('Load Game')
                            critical_snd.play()
                        if select == 4:
                            self.menu = False
                            pygame.quit()

    def menu_creator(self, select=('1.',), position=[0, 0], action=(None)):
        self.clock.tick(30)
        menu_creator_loop = True
        highlight = 1
        direction = -0.0625
        red = green = blue = 255
        position_const = position.copy()
        select_snd = pygame.mixer.Sound('Assets/Sounds/select.ogg')
        confirm_snd = pygame.mixer.Sound('Assets/Sounds/confirm.ogg')
        critical_snd = pygame.mixer.Sound('Assets/Sounds/critical.ogg')
        i = 1
        for keytext in select:
            keytext = ''.join(keytext)
            keytext = keytext.capitalize()
            keytext = str(i) + '. ' + keytext
            keytext = self.font3.render(keytext, True, (red, green, blue, 255))
            self.screen.blit(keytext, position)
            position[1] += 20
            i += 1
        position = position_const.copy()
        while menu_creator_loop:
            keytext = select[highlight-1]
            keytext = keytext.capitalize()
            keytext = str(highlight) + '. ' + keytext
            keytext = self.font3.render(keytext, False, (red, green, blue, 255))
            self.screen.blit(keytext, position)
            red += direction; green += direction; blue += direction
            if red == 192 or red == 255:
                direction *= -1
            elif red < 192 or red > 255:
                red = green = blue = 255
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_creator_loop = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu_creator_loop = False
                        print("out of the fight")
                        pygame.mixer.music.rewind()
                        pygame.mixer.music.unpause()
                        return False
                    elif event.key == pygame.K_DOWN:
                        select_snd.play()
                        if highlight < len(select):
                            red = green = blue = 192
                            highlight += 1
                            position[1] += 20
                    elif event.key == pygame.K_UP:
                        select_snd.play()
                        if highlight > 1:
                            red = green = blue = 192
                            highlight -= 1
                            position[1] -= 20
                    elif event.key == pygame.K_RETURN:
                        confirm_snd.play()
                        textreturn = select[highlight-1]
                        print(f"return: {textreturn}")
                        menu_creator_loop = False
                        return textreturn

                            

from Classes.game import Game
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    game = Game()
    game.gameloop()
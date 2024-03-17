from scripts import eventhander
from scripts.menu import render
from scripts.menu import menu
from scripts.game import maingame
import pygame

class game():
    def __init__(self):
        pygame.font.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.BGCOLOUR = (0, 0, 0)       
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.update()
        pygame.display.set_caption("Snake Game")
    def main(self):
        main = menu.menu(self.WINDOW)
        main.menu_loop()
        if main.play_event():
            game = maingame.game(self.WINDOW)
            game.start_game()
        


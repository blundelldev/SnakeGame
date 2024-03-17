import pygame
from scripts.menu import render
from scripts import eventhander

class menu():
    def __init__(self, WINDOW):
        self.WINDOW = WINDOW
        self.RENDERER = render.render(self.WINDOW)
    def menu_loop(self):
        pygame.time.Clock().tick(20)

        eventhander.get_events()
        self.RENDERER = render.render(self.WINDOW)
        self.WINDOW.fill((0, 0, 0))
        
        if self.RENDERER.PlayButton(False).collidepoint(pygame.mouse.get_pos()):
            self.RENDERER.PlayButton(True)
        else:
            self.RENDERER.PlayButton(False)

        self.RENDERER.MenuTitle()
        
        pygame.display.update()
    def play_event(self):
        if self.RENDERER.PlayButton(False).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
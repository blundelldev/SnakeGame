import pygame

class render():
    def __init__(self, WINDOW=pygame.display.set_mode()):
        self.WINDOW = WINDOW
        if int(self.WINDOW.get_width() / 8) < int(self.WINDOW.get_height() / 6):
            self.TITLEFONT = pygame.font.Font('freesansbold.ttf', int(self.WINDOW.get_width() / 8))
        else:
            self.TITLEFONT = pygame.font.Font('freesansbold.ttf', int(self.WINDOW.get_height() / 6))
        if int(self.WINDOW.get_width() / 12) < int(self.WINDOW.get_height() / 9):
            self.BUTTONFONT = pygame.font.SysFont('freesansbold.ttf', int(self.WINDOW.get_width() / 12))
        else:
            self.BUTTONFONT = pygame.font.SysFont('freesansbold.ttf', int(self.WINDOW.get_height() / 9))
        self.TITLEFONT.set_underline(True)
        
    def MenuTitle(self):
        LoadingText = self.TITLEFONT.render('Snake Game', True, (255, 255, 255))
        textx = int((self.WINDOW.get_width() / 2) - (self.TITLEFONT.size('Snake Game')[0] / 2))
        texty = int((self.WINDOW.get_height() / 2) / 10)
        self.WINDOW.blit(LoadingText, (textx, texty))
    def PlayButton(self, queery):
        font = self.BUTTONFONT
        if queery:
            font.set_bold(True)
        else:
            font.set_bold(False)
        PlayText = font.render('Play', True, (255, 255, 255))
        textx = int((self.WINDOW.get_width() / 2) - (font.size('Play')[0] / 2))
        texty = int(((self.WINDOW.get_height() / 2) / 10) * 6)
        self.WINDOW.blit(PlayText, (textx, texty))
        return pygame.Rect(textx, texty, font.size('Play')[0], font.size('Play')[1])
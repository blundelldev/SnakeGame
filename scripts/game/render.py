import pygame

class render():
    def __init__(self, WINDOW=pygame.display.set_mode()):
        self.WINDOW = WINDOW
        if int(self.WINDOW.get_width() / 12) < int(self.WINDOW.get_height() / 9):
            self.MAINFONT = pygame.font.SysFont('freesansbold.ttf', int(self.WINDOW.get_width() / 12))
        else:
            self.MAINFONT = pygame.font.SysFont('freesansbold.ttf', int(self.WINDOW.get_height() / 9))
        if int(self.WINDOW.get_width() / 28) < int(self.WINDOW.get_height() / 21):
            self.CONFIGFONT = pygame.font.SysFont('freesansbold.ttf', int(self.WINDOW.get_width() / 28))
        else:
            self.CONFIGFONT = pygame.font.SysFont('freesansbold.ttf', int(self.WINDOW.get_height() / 21))    
        
        if self.WINDOW.get_width() > self.WINDOW.get_height():
            self.GAMEFRAME = pygame.Rect(((self.WINDOW.get_width() / 2) - (self.WINDOW.get_height() / 2)), 0, self.WINDOW.get_height(), self.WINDOW.get_height())
        else:
            self.GAMEFRAME = pygame.Rect(0, ((self.WINDOW.get_height() / 2) - (self.WINDOW.get_width())), self.WINDOW.get_width(), self.WINDOW.get_width())

        self.BOXSIZE = self.GAMEFRAME.width / 20
        self.VECTORSIZE = self.GAMEFRAME.width / 20

        
        
    def SpaceToStart(self):
        font = self.MAINFONT
        PlayText = font.render('Space To Start', True, (255, 255, 255))
        textx = int((self.WINDOW.get_width() / 2) - (font.size('Space To Start')[0] / 2))
        texty = int((self.WINDOW.get_height() - font.size('Space To Start')[1]) - 10)
        self.WINDOW.blit(PlayText, (textx, texty))
        return pygame.Rect(textx, texty, font.size('Space To Start')[0], font.size('Space To Start')[1])
    
    def Configurations(self, wallcollision, playercollision, speed):
        font = self.CONFIGFONT
        WallCollision = font.render('W Wall Collision?: ' + str(wallcollision), True, (255, 255, 255))
        PlayerCollision = font.render("P Player Collision?: " + str(playercollision), True, (255, 255, 255))
        Speed = font.render('S Speed- ' + str(speed), True, (255, 255, 255))
        textx = int((self.WINDOW.get_width() / 2) - (font.size('W Wall Collision?: ' + str(wallcollision))[0] / 2))
        texty = int(((self.WINDOW.get_height() / 20) * 5 - font.size('W Wall Collision?: ')[1]))
        self.WINDOW.blit(WallCollision, (textx, texty))
        textx = int((self.WINDOW.get_width() / 2) - (font.size('P Player Collision?: ' + str(playercollision))[0] / 2))
        texty = int(((self.WINDOW.get_height() / 20) * 6 - font.size('P Player Collision?: ')[1]))
        self.WINDOW.blit(PlayerCollision, (textx, texty))
        textx = int((self.WINDOW.get_width() / 2) - (font.size('S Speed- ' + str(speed))[0] / 2))
        texty = int(((self.WINDOW.get_height() / 20) * 7 - font.size('S Speed- ')[1]))
        self.WINDOW.blit(Speed, (textx, texty))
        

        
    
    def DrawBox(self, xvect ,yvect, head, angle=1):
        x = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20))
        y = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20))
        rect = pygame.Rect(x, y, self.BOXSIZE, self.BOXSIZE)
        pygame.draw.rect(self.WINDOW, (255, 255, 255), rect)
        if head:
            if angle == 1:
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10) 
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10)
                lrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10) * 7
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10)
                rrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
            if angle == 2:
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10) * 7
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10)
                lrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10) * 7
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10) * 7
                rrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
            if angle == 3:
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10) * 7
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10) * 7
                lrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10)
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10) * 7
                rrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
            if angle == 4:
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10) 
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10)
                lrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
                lx = self.GAMEFRAME.x + (self.VECTORSIZE * (xvect % 20)) + (self.VECTORSIZE / 10)
                ly = self.GAMEFRAME.y + (self.VECTORSIZE * (yvect % 20)) + (self.VECTORSIZE / 10) * 7
                rrect = pygame.Rect(lx, ly, self.VECTORSIZE / 10, self.VECTORSIZE / 10)
            pygame.draw.rect(self.WINDOW, (0, 0, 0), lrect)
            pygame.draw.rect(self.WINDOW, (0, 0, 0), rrect)
                
                
                

                                                    
        return rect
    
    def Frame(self):
        pygame.draw.rect(self.WINDOW, (255, 255, 255), self.GAMEFRAME, 4)
    
    def FoodItem(self, xvect, yvect):
        microvector = self.VECTORSIZE / 20
        x = self.GAMEFRAME.x + (self.VECTORSIZE * xvect)
        y = self.GAMEFRAME.y + (self.VECTORSIZE * yvect)
        rect1x = x + microvector * 4
        rect1y = y + microvector * 4
        rect1width = microvector * 12
        rect1height = microvector * 12
        rect2x, rect2y, rect2width, rect2height = x + microvector * 9, y + microvector * 2, microvector * 2, microvector * 5
        
        rect1 = pygame.Rect(rect1x, rect1y, rect1width, rect1height)
        rect2 = pygame.Rect(rect2x, rect2y, rect2width, rect2height)
        pygame.draw.rect(self.WINDOW, (255, 0, 0), rect1)
        pygame.draw.rect(self.WINDOW, (0, 255, 0), rect2)
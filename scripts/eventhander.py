import pygame
import sys


events = []
def get_events():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                events.append("left")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                events.append("right")
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                events.append("up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                events.append("down")
            if event.key == pygame.K_SPACE:
                events.append("space")
            if event.key == pygame.K_p:
                events.append("ppress")
            if event.key == pygame.K_ESCAPE:
                events.append("escape")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                events.remove("left")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                events.remove("right")
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                events.remove("up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                events.remove("down")
            if event.key == pygame.K_SPACE:
                events.remove("space")
            if event.key == pygame.K_p:
                events.remove("ppress")
            if event.key == pygame.K_ESCAPE:
                events.remove("escape")
        
            
    return events
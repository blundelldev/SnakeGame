import pygame
from scripts.game import render
from scripts import eventhander
from scripts.game import maths

class game():
    def __init__(self, WINDOW = pygame.display.set_mode()):
        self.WINDOW = WINDOW
        self.RENDERER = render.render(self.WINDOW)
        self.SCORE = 0
        self.PLAYERCOLLIDE = False
        self.WALLCOLLIDE = False
        self.SPEED = 1
        
    
    def start_game(self):
        cd = 0
        while True:
            self.WINDOW.fill((0, 0, 0))
            self.RENDERER = render.render(self.WINDOW)
            self.RENDERER.Configurations(self.WALLCOLLIDE, self.PLAYERCOLLIDE, self.SPEED)
            self.RENDERER.SpaceToStart()
            cd -= 1
            pygame.display.update()
            if 'ppress' in eventhander.get_events() and cd <= 0:
                cd = 10
                if self.PLAYERCOLLIDE == True:
                    self.PLAYERCOLLIDE = False
                else:
                    self.PLAYERCOLLIDE = True
            if 'up' in eventhander.get_events() and cd <= 0:
                cd = 10
                if self.WALLCOLLIDE == True:
                    self.WALLCOLLIDE = False
                else:
                    self.WALLCOLLIDE = True
            if 'down' in eventhander.get_events() and cd <= 0:
                cd = 10
                self.SPEED = self.SPEED + 1
                if self.SPEED >= 11:
                    self.SPEED = 1
            
            if 'escape' in eventhander.get_events():
                return
            


            if 'space' in eventhander.get_events():
                running = True
                body = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
                front = [1, 5]
                food = [15, 15]
                direction = 3
                renderwait = 0
                eating = False
                
                while running:
                    if 'escape' in eventhander.get_events():
                        return
                    pygame.time.Clock().tick(50)
                    if not self.WALLCOLLIDE:
                        front[0], front[1] = front[0] % 20, front[1] % 20
                    elif front[0] == -1 or front[0] == 20 or front[1] == -1 or front[1] == 20:
                        return

                    


                    if renderwait <= 0:
                        if direction == 3:
                            body.append([front[0], front[1] + 1])
                            front = [front[0], front[1] + 1]
                            if not front == food:
                                body = body[1:]
                            else:
                                food = maths.NextFoodPos(body)
                                eating = False
                            
                        if direction == 1:
                            body.append([front[0], front[1] - 1])
                            front = [front[0], front[1] - 1]
                            if not front == food:
                                body = body[1:]
                            else:
                                food = maths.NextFoodPos(body)
                                eating = False
                        if direction == 2:
                            body.append([front[0] + 1, front[1]])
                            front = [front[0] + 1, front[1]]
                            if not front == food:
                                body = body[1:]
                                self.SCORE += 1
                            else:
                                food = maths.NextFoodPos(body)
                                eating = False
                        if direction == 4:
                            body.append([front[0] - 1, front[1]])
                            front = [front[0] - 1, front[1]]
                            if not front == food:
                                body = body[1:]
                            else:
                                food = maths.NextFoodPos(body)
                                eating = False



                        
                        renderwait = 9 / self.SPEED
                    
                    renderwait -= 1

                    self.WINDOW.fill((0, 0, 0))
                    eventhander.get_events()


                    if 'up' in eventhander.get_events():
                        direction = 1
                    if 'right' in eventhander.get_events():
                        direction = 2
                    if 'down' in eventhander.get_events():
                        direction = 3
                    if 'left' in eventhander.get_events():
                        direction = 4
                    self.RENDERER.Frame()
                    
                    self.RENDERER = render.render(self.WINDOW)
                    abox = 0
                    for box in body:
                        boxx, boxy = box[0], box[1]
                        abox += 1
                        if abox == len(body):
                            
                            self.RENDERER.DrawBox(boxx, boxy, True, direction)
                        else:
                            self.RENDERER.DrawBox(boxx, boxy, False, direction)


                    if self.PLAYERCOLLIDE:
                        for box in body[:-1]:
                            if box == front:
                                return self.SCORE
                    


                    
                    self.RENDERER.FoodItem(food[0], food[1])

                    

                    pygame.display.update()
                    
            pygame.display.update()
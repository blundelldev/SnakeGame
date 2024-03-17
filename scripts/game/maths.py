import random

def NextFoodPos(playerbody=[[tuple, tuple, tuple]]):
    valid = False
    while not valid:
        xtry = random.randint(1, 19)
        ytry = random.randint(1, 19) 
        good = True  
        for part in playerbody:
            if [xtry, ytry] == part:
                good = False
        if good == True:
            valid = True
    return [xtry, ytry]
    


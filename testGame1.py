from pytholi import *

screen = start() 
sprite = Sprite() 

loop = Loop(screen, sprite)

def motion():
    x, y = sprite.getPos()
    if keys()[pygame.K_UP]: y = y-1
    elif keys()[pygame.K_DOWN]: y = y+1
    elif keys()[pygame.K_LEFT]: x = x-1
    elif keys()[pygame.K_RIGHT]: x = x+1
    sprite.move(x, y)
    sleep(0.1)

loop.add_func(motion)
loop.run()
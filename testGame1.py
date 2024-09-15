from pytholi import *

screen = start() 
sprite = Sprite() 
loop = Loop(screen, sprite)

def motion():
    x, y = sprite.getPos()
    if pressed('up'): y = y-1
    elif pressed('down'): y = y+1
    elif pressed('left'): x = x-1
    elif pressed('right'): x = x+1
    sprite.move(x, y)
    sleep(0.1)

loop.add_func(motion)
loop.run()
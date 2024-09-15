from pytholi import *

# Muovi lo sprite lungo la prima riga in alto ogni secondo

screen = start(10, 4) 
sprite = Sprite(0, 0) 

x = 0
for n in range(10):
    screen.fill('white')
    grill(screen)
    picture(screen, sprite)
    flip()
    sleep(1)
    sprite.move(x, 0)
    x += 1


from pytholi import *

# Stampa uno sprite e fai in modo che dopo un secondo si sposta

screen = start(4, 4) # nuova schermata (4x4)
sprite = Sprite(0, 0) # nuovo player a posizione 2 3 rosso

screen.fill('white') # riempi schermo di bianco
grill(screen) # stampa la griglia sullo schermo
picture(screen, sprite) # stampa sprite1 alla sua posizione

flip()
sleep(1)
sprite.move(1, 0) # muovi lo sprite a posizione 2 2

screen.fill('white') # riempi schermo di bianco
grill(screen) # stampa la griglia sullo schermo
picture(screen, sprite) # stampa sprite1 alla sua posizione

flip()
sleep(2)
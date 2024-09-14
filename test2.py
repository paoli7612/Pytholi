from pytholi import *

# Creazione di due sprite distanti in una schermata 4x4

screen = start(4, 4) # nuova schermata (4x4)
sprite1 = Sprite(0, 0, 'red') # nuovo player a posizione 2 3 rosso
sprite2 = Sprite(2, 2) # nuovo player a posizione 2 3

screen.fill('white') # riempi schermo di bianco
grill(screen) # stampa la griglia sullo schermo
picture(screen, sprite1) # stampa sprite1 alla sua posizione
picture(screen, sprite2) # stampa sprite2 alla sua posizione

flip() # mostra le modifiche sullo schermo
sleep(2) # aspetta 2 secondi
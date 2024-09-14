from pytholi import *

# Creazione di un giocatore e stampa sullo schermo in una scacchiera impostando la posizione

screen = start() # nuova schermata
sprite = Sprite(2, 3) # nuovo player a posizione 2 3

screen.fill('purple') # riempi schermo di bianco
grill(screen) # stampa la griglia sullo schermo
picture(screen, sprite) # stampa il player alla sua posizione

flip() # mostra le modifiche sullo schermo
sleep(2) # aspetta 2 secondi
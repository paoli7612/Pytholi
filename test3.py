from pytholi import *

# Reimposta le dimensioni di ogni cella a 32x32 e stampa una griglia vuota 4x4

set_tile(32)
screen = start() # nuova schermata
screen.fill('blue') # riempi schermo di bianco
grill(screen) # stampa la griglia sullo schermo

flip() # mostra le modifiche sullo schermo
sleep(3) # aspetta 2 secondi
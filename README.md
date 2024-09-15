<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

# Pytholi

Semplificazione del modulo di pygame per semplificare lo studio della programmazione in Python attraverso un modulo grafico.

## Comandi

Per semplificare la procedura viene stabilito un metodo iniziale che ritorna l'oggetto che rappresenta la schermata

## Funzionalità

Semplificando il modulo viene deciso di rispettare il rendering di un tile-game 2D. Viene stabilito un numero TILE (inizialmente impostato a 64)
- `TILE_X` rappresenta la quantità di celle in orizzontale
- `TILE_Y` rappresenta la quantità di celle in verticale
- `SIZE` è la tupla `(TILE_X, TILE_Y)`

### Cambio dei parametri iniziali
Il cambio della grandezza `TILE` è raccomandata solo tramite il metodo `set_tile(tile)`

## Istruzioni

### Template
```python
    from pytholi import *
    screen = start() # nuova schermata
    screen.fill('white') # colora di bianco
    grill(screen) # stampa la griglia
    flip() # mostra le modifiche allo screen
    sleep(1) # aspetta 1 secondo
```

- Avvio
  - Avvio standard `screen = start()`
  - Impostando le dimensioni `screen = start(12, 9)`
- Stampa
  - Flip and wait
```python
    flip()
    sleep(3)
```

<img src="img/Screenshot from 2024-09-14 22-18-03.png">
# avoid first print____________________
import sys, os                      # |
from time import sleep              # |
sys.stdout = open(os.devnull, 'w')  # |
import pygame                       # | 
sys.stdout.close()                  # |
sys.stdout = sys.__stdout__         # |
#______________________________________
from .settings import Settings
from .sprite import Sprite

def start(tileX=None, tileY=None):
    if tileX and tileY:
        Settings.setSize(tileX, tileY)
    return pygame.display.set_mode(Settings.SIZE)

def grill(screen, color='black', thickness=3):
    for x in range(Settings.TILE_X):
        pygame.draw.line(screen, color, (x*Settings.TILE, 0), (x*Settings.TILE, Settings.HEIGHT), thickness)
    for y in range(Settings.TILE_Y):
        pygame.draw.line(screen, color, (0, y*Settings.TILE), (Settings.WIDTH, y*Settings.TILE), thickness)

def picture(screen, sprite):
    screen.blit(sprite.image, sprite.rect)

def flip():
    pygame.display.flip()

def set_tile(tile):
    Settings.setTile(tile)



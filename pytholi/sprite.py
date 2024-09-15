import pygame
from .settings import Settings

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, color='black', name=''):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(Settings.RECT)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.move(x, y)

    def move(self, x, y):
        self.rect.topleft = Settings.posToPixel(x, y)

    def getPos(self):
        xp, yp = self.rect.topleft
        return xp/Settings.TILE, yp/Settings.TILE


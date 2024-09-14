class Settings:
    TILE = 64
    TILE_X = 9
    TILE_Y = 6
    SIZE = (WIDTH, HEIGHT) = TILE * TILE_X, TILE * TILE_Y
    RECT = (TILE, TILE)

    def posToPixel(x, y):
        return Settings.TILE*x, Settings.TILE*y


class Settings:
    TILE = 64
    TILE_X = 9
    TILE_Y = 6
    SIZE = (WIDTH, HEIGHT) = TILE * TILE_X, TILE * TILE_Y
    RECT = (TILE, TILE)

    def posToPixel(x, y):
        return Settings.TILE*x, Settings.TILE*y

    def setSize(tile_x, tile_y):
        Settings.TILE_X = tile_x
        Settings.TILE_Y = tile_y
        Settings.SIZE = (Settings.WIDTH, Settings.HEIGHT) = Settings.TILE * Settings.TILE_X, Settings.TILE * Settings.TILE_Y



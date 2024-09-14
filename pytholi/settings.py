class Settings:
    TILE = 64
    TILE_X, TILE_Y = 9, 6

    def init():
        Settings.SIZE = (Settings.WIDTH, Settings.HEIGHT) = Settings.TILE * Settings.TILE_X, Settings.TILE * Settings.TILE_Y
        Settings.RECT = (Settings.TILE, Settings.TILE)

    def posToPixel(x, y):
        return Settings.TILE*x, Settings.TILE*y

    def setTile(tile):
        Settings.TILE = tile
        Settings.init()

    def setSize(tile_x, tile_y):
        Settings.TILE_X = tile_x
        Settings.TILE_Y = tile_y
        Settings.SIZE = (Settings.WIDTH, Settings.HEIGHT) = Settings.TILE * Settings.TILE_X, Settings.TILE * Settings.TILE_Y

Settings.init()
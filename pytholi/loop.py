import pygame

class Loop:
    def __init__(self, screen, *sprites):
        self.screen = screen
        self.sprites = pygame.sprite.Group(sprites)
        self.functions = list()

    def add_func(self, func):
        self.functions.append(func)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.sprites.update()
        for func in self.functions:
            func()

    def draw(self):
        self.screen.fill('white')
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.event()
            self.update()
            self.draw()
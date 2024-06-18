import pygame
import os

class AssetManager:
    def __init__(self, biome):
        self.images = {}
        self.fonts = {}
        self.biome = biome

        self.load_image('background.jpg', (400, 700))
        self.load_image('knife.png', (30, 120))
        self.load_image('small_knife.png', (20, 80))

        self.load_font('IndieFlower-Regular.ttf', 36)

        self.load_fonts()

    def load_fonts(self):
        if self.biome == 'desert':
            self.load_font('Algerian.ttf', 24)
        elif self.biome == 'green':
            self.load_font('VinerHandITC.ttf', 24)
        elif self.biome == 'ice':
            self.load_font('HarlowSolidItalic.ttf', 24)
        elif self.biome == 'urban':
            self.load_font('Impact.ttf', 24)
        else:
            self.load_font('IndieFlower-Regular.ttf', 24)

    def load_image(self, name, size=None):
        fullname = os.path.join('images', self.biome, name)
        try:
            image = pygame.image.load(fullname).convert_alpha()
            if size:
                image = pygame.transform.scale(image, size)
            self.images[name] = image
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)

    def get_image(self, name):
        return self.images.get(name)

    def load_font(self, name, size):
        fullname = os.path.join('fonts', name)
        try:
            font = pygame.font.Font(fullname, size)
            self.fonts[name] = font
        except pygame.error as message:
            print('Cannot load font:', name)
            raise SystemExit(message)

    def get_font(self, name):
        return self.fonts.get(name)

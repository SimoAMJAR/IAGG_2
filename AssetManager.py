import pygame
import os

class AssetManager:
    def __init__(self, biome):
        self.images = {}
        self.fonts = {}
        self.biome = biome

        # Load images based on biome
        self.load_image('background.jpg', (400, 700))
        self.load_image('knife.png', (30, 120))
        self.load_image('small_knife.png', (20, 80))

        # Load font
        self.load_font('IndieFlower-Regular.ttf', 36)

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

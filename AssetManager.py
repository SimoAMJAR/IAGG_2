import pygame
import os

class AssetManager:
    def __init__(self):
        self.images = {}
        self.fonts = {}

    def load_image(self, name, size=None):
        fullname = os.path.join('images', name)
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

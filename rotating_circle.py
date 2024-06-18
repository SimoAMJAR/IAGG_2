import pygame
import os

WIDTH, HEIGHT = 400, 700

class RotatingCircle(pygame.sprite.Sprite):
    def __init__(self, rotation_speed, biome, direction="right"):
        super().__init__()
        self.biome = biome
        self.rotation_speed = rotation_speed
        self.direction = direction
        self.load_image()

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
        self.angle = 0

    def load_image(self):
        filename = 'wheel.png'
        fullname = os.path.join('images', self.biome, filename)
        try:
            self.original_image = pygame.image.load(fullname).convert_alpha()
            self.original_image = pygame.transform.scale(self.original_image, (200, 200))
            self.image = self.original_image.copy()
        except pygame.error as e:
            print(f"Cannot load image: {fullname}")
            raise SystemExit(e)

    def update(self):
        if self.direction == "right":
            self.angle += self.rotation_speed
        else:
            self.angle -= self.rotation_speed
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_rotation_direction(self):
        return self.direction

# rotating_circle.py

import pygame

WIDTH, HEIGHT = 400, 700

class RotatingCircle(pygame.sprite.Sprite):
    def __init__(self, rotation_speed, direction="right"):
        super().__init__()
        self.original_image = pygame.image.load('wheel.png').convert_alpha()  # Load the image
        self.original_image = pygame.transform.scale(self.original_image, (200, 200))  # Adjust size if necessary
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
        self.angle = 0
        self.rotation_speed = rotation_speed
        self.direction = direction

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

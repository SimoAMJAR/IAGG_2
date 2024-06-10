# rotating_circle.py

import pygame

RED = (255, 0, 0)
WIDTH, HEIGHT = 400, 700

class RotatingCircle(pygame.sprite.Sprite):
    def __init__(self, rotation_speed):
        super().__init__()
        self.original_image = pygame.Surface((160, 160), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, RED, (80, 80), 80)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
        self.angle = 0
        self.rotation_speed = rotation_speed

    def update(self):
        self.angle += self.rotation_speed
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

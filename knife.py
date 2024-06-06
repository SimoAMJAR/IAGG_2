import pygame
import math

BLACK = (0, 0, 0)

class Knife(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        # Load and resize the knife image
        self.original_image = pygame.image.load('knife.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (80, 80))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
        self.speed = 10
        self.stuck = False
        self.rotation_speed = 1
        self.target = target
        self.angle = 0
        self.stick_angle = 0

    def update(self):
        if not self.stuck:
            self.rect.y -= self.speed
        else:
            radius = self.target.rect.width / 2
            self.angle += self.rotation_speed
            self.angle %= 360
            self.rect.centerx = self.target.rect.centerx + radius * math.cos(math.radians(self.stick_angle + self.angle))
            self.rect.centery = self.target.rect.centery + radius * math.sin(math.radians(self.stick_angle + self.angle))

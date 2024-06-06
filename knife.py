import pygame
import math

BLACK = (0, 0, 0)

class Knife(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        # Load and resize the knife image
        self.original_image = pygame.image.load('knife.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (50, 150))  # Adjust size if necessary
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
        self.speed = 10
        self.stuck = False
        self.rotation_speed = 1
        self.target = target
        self.angle = 0
        self.stick_angle = 0
        self.stick_distance = 100  # Distance from the center of the circle

    def update(self):
        if not self.stuck:
            self.rect.y -= self.speed
        else:
            radius = self.target.rect.width / 2
            self.angle += self.rotation_speed
            self.angle %= 360

            # Calculate knife position to ensure it stays fixed relative to the circle's center
            self.rect.centerx = self.target.rect.centerx + self.stick_distance * math.cos(math.radians(self.stick_angle + self.angle))
            self.rect.centery = self.target.rect.centery + self.stick_distance * math.sin(math.radians(self.stick_angle + self.angle))

            # Rotate the knife to always point towards the center of the circle
            rotation_angle = self.stick_angle + self.angle - 90
            self.image = pygame.transform.rotate(self.original_image, -rotation_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

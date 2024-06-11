# knife.py

import pygame
import math

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 400, 700

class Knife(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.original_image = pygame.image.load('knife.png').convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 550)
        self.speed = 10
        self.stuck = False
        self.target = target
        self.angle = 0
        self.stick_angle = 0
        self.stick_distance = 90  # Distance from the center of the circle
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not self.stuck:
            self.rect.y -= self.speed
            self.speed += 2  # Adjust this value as needed
        else:
            if self.target.direction == "right":
                self.angle -= self.target.rotation_speed
            else:
                self.angle += self.target.rotation_speed
            self.angle %= 360

            # Calculate the new position of the knife on the wheel
            self.rect.centerx = self.target.rect.centerx + self.stick_distance * math.cos(math.radians(self.stick_angle + self.angle))
            self.rect.centery = self.target.rect.centery + self.stick_distance * math.sin(math.radians(self.stick_angle + self.angle))

            # Rotate the knife to always point towards the center of the circle
            rotation_angle = self.stick_angle + self.angle - 90
            self.image = pygame.transform.rotate(self.original_image, -rotation_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

            # Update the mask after rotation
            self.mask = pygame.mask.from_surface(self.image)

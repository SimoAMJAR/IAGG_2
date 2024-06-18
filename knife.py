import pygame
import math
import os

class Knife(pygame.sprite.Sprite):
    def __init__(self, target, biome):
        super().__init__()
        self.biome = biome
        self.original_image = pygame.image.load(os.path.join('images', self.biome, 'knife.png')).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (30, 120))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (400 // 2, 550)
        self.speed = 10
        self.stuck = False
        self.target = target
        self.angle = 0
        self.stick_angle = 0
        self.stick_distance = 90
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not self.stuck:
            self.rect.y -= self.speed
            self.speed += 2
        else:
            rotation_direction = self.target.get_rotation_direction()
            if rotation_direction == "right":
                self.angle -= self.target.rotation_speed
            else:
                self.angle += self.target.rotation_speed
            self.angle %= 360

            self.rect.centerx = self.target.rect.centerx + self.stick_distance * math.cos(math.radians(self.stick_angle + self.angle))
            self.rect.centery = self.target.rect.centery + self.stick_distance * math.sin(math.radians(self.stick_angle + self.angle))

            rotation_angle = self.stick_angle + self.angle - 90
            self.image = pygame.transform.rotate(self.original_image, -rotation_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

            self.mask = pygame.mask.from_surface(self.image)

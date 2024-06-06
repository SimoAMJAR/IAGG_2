import pygame
import math

BLACK = (0, 0, 0)

class Knife(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.original_image = pygame.Surface((20, 40))
        self.original_image.fill(BLACK)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
        self.speed = 10
        self.stuck = False
        self.rotation_speed = 1  # Adjust rotation speed of the knife to match circle
        self.target = target
        self.angle = 0
        self.stick_angle = 0  # Angle at which the knife sticks to the circle

    def update(self):
        if not self.stuck:
            self.rect.y -= self.speed
        else:
            # Stick to the circumference of the circle
            radius = self.target.rect.width / 2
            self.angle += self.rotation_speed
            self.angle %= 360
            self.rect.centerx = self.target.rect.centerx + radius * math.cos(math.radians(self.stick_angle + self.angle))
            self.rect.centery = self.target.rect.centery + radius * math.sin(math.radians(self.stick_angle + self.angle))
            # Resize the image to maintain the original size
            self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))

    def set_stick_angle(self, angle):
        self.stick_angle = angle

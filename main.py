import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knife Hit Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define classes
class Knife(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 10
        self.hit_target = False  # New attribute to track if the knife has hit the target

    def update(self):
        if not self.hit_target:
            self.rect.y -= self.speed

    def draw(self, surface):
        if not self.hit_target:
            surface.blit(self.image, self.rect)

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, RED, (50, 50), 50)
        self.image = self.original_image.copy()  # Make a copy to avoid modifying the original
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.angle = 0  # Initial rotation angle
        self.rotation_speed = 2  # Rotation speed in degrees per frame

    def update(self):
        self.angle += self.rotation_speed
        self.angle %= 360  # Keep angle within 0-359 range
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create sprites
knife = Knife()
target = Target()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(knife)

targets = pygame.sprite.Group()
targets.add(target)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                new_knife = Knife()
                all_sprites.add(new_knife)

    # Update sprites
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.groupcollide(targets, all_sprites, False, True)
    for target, knives in hits.items():
        for knife in knives:
            knife.hit_target = True
            knife.rect.center = target.rect.center

    # Draw sprites
    for entity in all_sprites:
        entity.draw(screen)

    for entity in targets:
        entity.draw(screen)

    for target in targets:
        target.update()

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

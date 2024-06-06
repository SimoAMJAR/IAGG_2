import pygame
import sys
import random
import math

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
    def __init__(self, target):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 10
        self.stuck = False
        self.rotation_speed = 5
        self.target = target
        self.angle = 0

    def update(self):
        if not self.stuck:
            self.rect.y -= self.speed
        else:
            # Stick to the circumference of the circle
            radius = self.target.rect.width / 2
            self.angle += self.rotation_speed
            self.rect.centerx = self.target.rect.centerx + radius * math.cos(math.radians(self.angle))
            self.rect.centery = self.target.rect.centery + radius * math.sin(math.radians(self.angle))

    def draw(self, surface):
        if not self.stuck:
            surface.blit(self.image, self.rect)
        else:
            rotated_image = pygame.transform.rotate(self.image, -self.angle)
            rotated_rect = rotated_image.get_rect(center=self.rect.center)
            surface.blit(rotated_image, rotated_rect)

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, RED, (50, 50), 50)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.angle = 0
        self.rotation_speed = 2

    def update(self):
        self.angle += self.rotation_speed
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create sprites
target = Target()

# Create sprite groups
all_sprites = pygame.sprite.Group()

targets = pygame.sprite.Group()
targets.add(target)

# Main game loop
running = True
score = 0

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_knife = Knife(target)  # Pass the target instance
                all_sprites.add(new_knife)

    hits = pygame.sprite.groupcollide(targets, all_sprites, False, False)
    for target, knives in hits.items():
        for knife in knives:
            if not knife.stuck:
                knife.stuck = True
                score += 1

    all_sprites.update()

    for target in targets:
        target.update()

    for entity in all_sprites:
        entity.draw(screen)

    for entity in targets:
        entity.draw(screen)

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

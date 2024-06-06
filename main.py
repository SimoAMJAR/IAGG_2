#main.py
import pygame
import sys
import math
from knife import Knife
from target import Target

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knife Hit Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create sprite groups
all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()

# Create target sprite
target = Target()
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
                new_knife = Knife(target)
                all_sprites.add(new_knife)

    hits = pygame.sprite.groupcollide(targets, all_sprites, False, False)
    for target, knives in hits.items():
        for knife in knives:
            if not knife.stuck:
                dx = knife.rect.centerx - target.rect.centerx
                dy = knife.rect.centery - target.rect.centery
                angle = math.degrees(math.atan2(dy, dx))
                knife.set_stick_angle(angle)
                knife.stuck = True
                score += 1

    all_sprites.update()  # Update all sprites, including knives
    targets.update()

    all_sprites.draw(screen)
    targets.draw(screen)

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

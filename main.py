import pygame
import sys
import math
from knife import Knife
from rotating_circle import RotatingCircle
from game_over_screen import GameOverScreen
from start_screen import StartScreen
from levels import Levels

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 700  # Changed dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knife Hit Game")

# Colors
WHITE = (255, 255, 255)

def preplace_knives(rotating_circle, knife_count):
    knives = pygame.sprite.Group()
    for i in range(knife_count):
        angle = i * (360 // knife_count)
        knife = Knife(rotating_circle)
        knife.stuck = True
        knife.stick_angle = angle
        knife.rect.centerx = rotating_circle.rect.centerx + knife.stick_distance * math.cos(math.radians(angle))
        knife.rect.centery = rotating_circle.rect.centery + knife.stick_distance * math.sin(math.radians(angle))
        knives.add(knife)
    return knives

def initialize_level(levels):
    current_level = levels.get_current_level()
    all_sprites = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    rotating_circle = RotatingCircle(current_level.rotation_speed, current_level.direction)  # Pass direction here
    targets.add(rotating_circle)
    preplaced_knives = preplace_knives(rotating_circle, current_level.preplaced_knives)
    all_sprites.add(preplaced_knives)
    return all_sprites, targets, current_level.knife_count, rotating_circle


def main():
    # Initialize levels
    levels = Levels()
    
    # Initialize the first level
    all_sprites, targets, knife_count, rotating_circle = initialize_level(levels)

    # Load knife image
    knife_image = pygame.image.load('knife.png').convert_alpha()
    knife_image = pygame.transform.scale(knife_image, (40, 40))  # Adjust size if necessary

    # Main game loop
    running = True
    score = 0
    game_over = False
    game_over_timer = None

    # Display the start screen
    start_screen = StartScreen(screen)
    while start_screen.running:
        start_screen.display()
        start_screen.handle_events()

    while running:
        screen.fill(WHITE)

        if game_over:
            if game_over_timer is None:
                game_over_timer = pygame.time.get_ticks()  # Start the timer
            elif pygame.time.get_ticks() - game_over_timer >= 500:  # Check if 2 seconds have passed
                game_over_screen = GameOverScreen(screen, score)
                while game_over_screen.running:
                    game_over_screen.display()
                    game_over_screen.handle_events()
                # Reset game state if restarted
                if not game_over_screen.running:
                    levels.reset()
                    all_sprites, targets, knife_count, rotating_circle = initialize_level(levels)
                    score = 0
                    game_over = False
                    game_over_timer = None
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and knife_count > 0:
                        new_knife = Knife(rotating_circle)
                        all_sprites.add(new_knife)
                        knife_count -= 1

            for knife in all_sprites:
                if not knife.stuck:
                    # Check for collision with other knives
                    hit_knives = pygame.sprite.spritecollide(knife, all_sprites, False, pygame.sprite.collide_mask)
                    for hit_knife in hit_knives:
                        if hit_knife != knife and hit_knife.stuck:
                            game_over = True
                            break

            hits = pygame.sprite.groupcollide(targets, all_sprites, False, False, pygame.sprite.collide_mask)
            for target, knives in hits.items():
                for knife in knives:
                    if not knife.stuck:
                        dx = knife.rect.centerx - target.rect.centerx
                        dy = knife.rect.centery - target.rect.centery
                        angle = math.degrees(math.atan2(dy, dx))
                        knife.stick_angle = angle
                        knife.stuck = True
                        score += 1

            all_sprites.update()  # Update all sprites, including knives
            targets.update()

            if knife_count == 0 and all(knife.stuck for knife in all_sprites):
                if levels.advance_level():
                    all_sprites, targets, knife_count, rotating_circle = initialize_level(levels)
                else:
                    game_over = True

        all_sprites.draw(screen)
        targets.draw(screen)

        # Display score and knife count
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))
        text = font.render(f"Level: {levels.current_level}", True, (0, 0, 0))
        screen.blit(text, (10, 50))

        # Display remaining knives as small images
        knife_spacing = 45  # Spacing between each knife image
        for i in range(knife_count):
            screen.blit(knife_image, (10, HEIGHT - 50 - i * knife_spacing))     

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

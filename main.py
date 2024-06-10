import pygame
import sys
import math
from knife import Knife
from rotating_circle import RotatingCircle
from game_over_screen import GameOverScreen
from start_screen import StartScreen 

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knife Hit Game")

# Colors
WHITE = (255, 255, 255)

def main():
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    targets = pygame.sprite.Group()

    # Create rotating circle sprite
    rotating_circle = RotatingCircle()
    targets.add(rotating_circle)

    # Main game loop
    running = True
    score = 0
    game_over = False

    # Display the start screen
    start_screen = StartScreen(screen)
    while start_screen.running:
        start_screen.display()
        start_screen.handle_events()

    while running:
        screen.fill(WHITE)

        if game_over:
            game_over_screen = GameOverScreen(screen, score)
            while game_over_screen.running:
                game_over_screen.display()
                game_over_screen.handle_events()
            # Reset game state if restarted
            if not game_over_screen.running:
                running = True
                game_over = False
                score = 0
                all_sprites.empty()
                targets.empty()
                rotating_circle = RotatingCircle()
                targets.add(rotating_circle)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        new_knife = Knife(rotating_circle)
                        all_sprites.add(new_knife)

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

        all_sprites.draw(screen)
        targets.draw(screen)

        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

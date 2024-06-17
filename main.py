import pygame
import sys
import math
import os
from AssetManager import AssetManager
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
pygame.display.set_caption("Knife Hit")

# Initialize AssetManager
asset_manager = None  # Will be initialized in main

# Font for the game (retrieved from AssetManager)
font = None  # Will be initialized in main

# Define the path to the high score file
HIGH_SCORE_FILE = "high_score.txt"

# Colors
WHITE = (255, 255, 255)

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    else:
        return 0

# Add a function to save the high score to the file
def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))

def preplace_knives(rotating_circle, biome, knife_count):
    knives = pygame.sprite.Group()
    for i in range(knife_count):
        angle = i * (360 // knife_count)
        knife = Knife(rotating_circle, biome)  # Provide biome argument here
        knife.stuck = True
        knife.stick_angle = angle
        knife.rect.centerx = rotating_circle.rect.centerx + knife.stick_distance * math.cos(math.radians(angle))
        knife.rect.centery = rotating_circle.rect.centery + knife.stick_distance * math.sin(math.radians(angle))
        knives.add(knife)
    return knives

def initialize_level(levels, biome):
    current_level = levels.get_current_level()
    all_sprites = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    rotating_circle = RotatingCircle(current_level.rotation_speed, biome, current_level.direction)  # Pass biome here
    targets.add(rotating_circle)
    preplaced_knives = preplace_knives(rotating_circle, biome, current_level.preplaced_knives)
    all_sprites.add(preplaced_knives)
    return all_sprites, targets, current_level.knife_count, rotating_circle

def main(biome):
    # Initialize levels
    levels = Levels()

    # Load the high score
    high_score = load_high_score()
    
    # Initialize the first level
    all_sprites, targets, knife_count, rotating_circle = initialize_level(levels, biome)

    # Initialize AssetManager with selected biome
    asset_manager = AssetManager(biome)

    # Retrieve font from AssetManager
    font = asset_manager.get_font('IndieFlower-Regular.ttf')

    # Retrieve specific fonts based on biome
    if biome == 'desert':
        font = asset_manager.get_font('Algerian.ttf')
    elif biome == 'green':
        font = asset_manager.get_font('VinerHandITC.ttf')
    elif biome == 'ice':
        font = asset_manager.get_font('HarlowSolidItalic.ttf')
    elif biome == 'urban':
        font = asset_manager.get_font('Impact.ttf')

    # Retrieve images from AssetManager
    background_image = asset_manager.get_image('background.jpg')
    knife_image = asset_manager.get_image('knife.png')
    small_knife_image = asset_manager.get_image('small_knife.png')

    # Rect for the knife to be displayed at the bottom center
    knife_rect = knife_image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))

    # Main game loop
    running = True
    score = 0
    game_over = False
    game_over_timer = None
    knife_in_motion = False
    current_knife = None

    background = pygame.image.load('images/background.png').convert()

    # Load sound effect
    throw_sound = pygame.mixer.Sound('music/knife_throw.mp3')
    hit_sound = pygame.mixer.Sound('music/knife_hit.mp3')
    throw_sound.set_volume(0.5)
    hit_sound.set_volume(0.5)

    pygame.mixer.music.load('music/intro.mp3')

    level_up_timer = None
    display_level_up = False
    vibrate_offset = 0  

    while running:
        screen.fill(WHITE)

        # Draw the background image
        screen.blit(background_image, (0, 0))

        if game_over:
            pygame.mixer.music.play(-1)
            if game_over_timer is None:
                game_over_timer = pygame.time.get_ticks()  # Start the timer
            elif pygame.time.get_ticks() - game_over_timer >= 500:  # Check if 2 seconds have passed
                # Check if the current score is higher than the high score
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)  # Save the new high score
                game_over_screen = GameOverScreen(screen, background ,score, high_score)
                while game_over_screen.running:
                    game_over_screen.display()
                    game_over_screen.handle_events()
                # Reset game state if restarted
                if game_over_screen.restart_game:
                    pygame.mixer.music.stop()
                    return  # Return to main loop to restart the game
                else:
                    pygame.quit()
                    sys.exit()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and knife_count > 0 and not knife_in_motion:
                        knife_in_motion = True
                        current_knife = Knife(rotating_circle, biome)
                        all_sprites.add(current_knife)
                        knife_count -= 1
                        # Play the sound effect
                        throw_sound.play()

            if knife_in_motion and current_knife is not None:
                current_knife.update()
                if current_knife.rect.top < 0 or current_knife.stuck:
                    knife_in_motion = False
                    if current_knife.stuck:
                        score += 1
                    else:
                        game_over = True

            for knife in all_sprites:
                if not knife.stuck:
                    hit_knives = pygame.sprite.spritecollide(knife, all_sprites, False, pygame.sprite.collide_mask)
                    for hit_knife in hit_knives:
                        if hit_knife != knife and hit_knife.stuck:
                            game_over = True
                            hit_sound.play()
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

            all_sprites.update()  # Update all sprites, including knives
            targets.update()

            if knife_count == 0 and all(knife.stuck for knife in all_sprites):
                if levels.advance_level():
                    display_level_up = True
                    level_up_timer = pygame.time.get_ticks()  # Start the timer
                    vibrate_offset = 0  # Reset vibration offset
                    all_sprites, targets, knife_count, rotating_circle = initialize_level(levels, biome)
                else:
                    game_over = True

        all_sprites.draw(screen)
        targets.draw(screen)

        # Draw the knife at the bottom center if it's not in motion
        if not knife_in_motion and knife_count > 0:
            screen.blit(knife_image, knife_rect)

        if display_level_up:
            # Calculate vibration effect
            vibrate_amplitude = 5  # Amplitude of vibration
            vibrate_offset = vibrate_amplitude * math.sin(pygame.time.get_ticks() / 50)  # Adjust speed of vibration

            # Render level number with vibration effect
            level_text = font.render(f"Level: {levels.current_level}", True, (0, 0, 0))
            text_rect = level_text.get_rect(center=(WIDTH // 2 + vibrate_offset, HEIGHT // 2))
            screen.blit(level_text, text_rect)

            # Check if 3 seconds have passed
            if pygame.time.get_ticks() - level_up_timer >= 500:
                display_level_up = False

        # Display score and knife count
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        # Display remaining knives as small images
        knife_spacing = 80  # Spacing between each knife image
        for i in range(knife_count):
            screen.blit(small_knife_image, (5, HEIGHT - 90 - i * knife_spacing))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    while True:
        # Display the start screen and get the selected biome
        start_screen = StartScreen(screen)
        while start_screen.running:
            start_screen.display()
            start_screen.handle_events()

        selected_biome = start_screen.selected_biome
        if selected_biome:
            main(selected_biome)

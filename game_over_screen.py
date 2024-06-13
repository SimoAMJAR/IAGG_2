import sys
import pygame

class GameOverScreen:
    def __init__(self, screen, background, score, high_score):
        self.screen = screen
        self.background = background
        self.score = score
        self.high_score = high_score
        self.font_large = pygame.font.Font('SCRUBLAND.ttf', 50)
        self.font_small = pygame.font.Font('SCRUBLAND.ttf', 36)
        self.running = True
        self.restart_game = False

    def display(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))

        game_over_text = self.font_large.render("Game Over", True, (0, 0, 0))
        score_text = self.font_small.render(f"Score: {self.score}", True, (0, 0, 0))
        high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        restart_text = self.font_small.render("Restart [R]", True, (0, 0, 0))
        quit_text = self.font_small.render("Quit [Q]", True, (0, 0, 0))

        # Position texts
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(score_text, (self.screen.get_width() // 2 - score_text.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(high_score_text, (self.screen.get_width() // 2 - high_score_text.get_width() // 2, self.screen.get_height() // 2 + 30))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, self.screen.get_height() // 2 + 140))
        self.screen.blit(quit_text, (self.screen.get_width() // 2 - quit_text.get_width() // 2, self.screen.get_height() // 2 + 180))

        pygame.display.flip()  # Update the display

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.running = False
                    self.restart_game = True  # Indicate a restart
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

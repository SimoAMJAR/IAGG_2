import sys
import pygame

class GameOverScreen:
    def __init__(self, screen, score, high_score):
        self.screen = screen
        self.score = score
        self.high_score = high_score
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.running = True

    def display(self):
        self.screen.fill((255, 255, 255))
        game_over_text = self.font_large.render("Game Over", True, (255, 0, 0))
        score_text = self.font_small.render(f"Score: {self.score}", True, (0, 0, 0))
        high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, (0, 0, 0))  # Display high score
        restart_text = self.font_small.render("Press R to Restart or Q to Quit", True, (0, 0, 0))

        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(score_text, (self.screen.get_width() // 2 - score_text.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(high_score_text, (self.screen.get_width() // 2 - high_score_text.get_width() // 2, self.screen.get_height() // 2 + 30))  # Adjust position
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, self.screen.get_height() // 2 + 80))  # Adjust position

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.running = False  # Will be used to restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

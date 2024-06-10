import sys
import pygame

class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.running = True

    def display(self):
        self.screen.fill((255, 255, 255))
        game_over_text = self.font_large.render("Game Over", True, (255, 0, 0))
        score_text = self.font_small.render(f"Score: {self.score}", True, (0, 0, 0))
        restart_text = self.font_small.render("Press R to Restart or Q to Quit", True, (0, 0, 0))

        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(score_text, (self.screen.get_width() // 2 - score_text.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, self.screen.get_height() // 2 + 50))

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

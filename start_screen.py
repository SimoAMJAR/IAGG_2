import sys
import pygame

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.running = True

    def display(self):
        self.screen.fill((255, 255, 255))
        title_text = self.font_large.render("Knife Hit Game", True, (0, 0, 255))
        start_text = self.font_small.render("Click to Start", True, (0, 0, 0))

        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(start_text, (self.screen.get_width() // 2 - start_text.get_width() // 2, self.screen.get_height() // 2))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.running = False  # Will be used to start the game

import sys
import pygame

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.running = True
        self.selected_biome = None

        # Define button properties
        self.button_width = 150
        self.button_height = 50
        self.button_color = (0, 255, 0)  # Green
        self.button_hover_color = (0, 200, 0)  # Darker green

        # Define positions
        self.ice_button_rect = pygame.Rect((self.screen.get_width() // 4 - self.button_width // 2,
                                            self.screen.get_height() // 2), (self.button_width, self.button_height))
        self.green_button_rect = pygame.Rect((3 * self.screen.get_width() // 4 - self.button_width // 2,
                                              self.screen.get_height() // 2), (self.button_width, self.button_height))

    def display(self):
        self.screen.fill((255, 255, 255))
        title_text = self.font_large.render("Knife Hit Game", True, (0, 0, 255))
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, self.screen.get_height() // 3))

        # Draw buttons
        self.draw_button(self.ice_button_rect, "Ice")
        self.draw_button(self.green_button_rect, "Green")

        pygame.display.flip()

    def draw_button(self, rect, text):
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):
            color = self.button_hover_color
        else:
            color = self.button_color
        pygame.draw.rect(self.screen, color, rect)
        button_text = self.font_small.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (rect.x + rect.width // 2 - button_text.get_width() // 2,
                                       rect.y + rect.height // 2 - button_text.get_height() // 2))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.ice_button_rect.collidepoint(event.pos):
                        self.selected_biome = "ice"
                        self.running = False
                    elif self.green_button_rect.collidepoint(event.pos):
                        self.selected_biome = "green"
                        self.running = False

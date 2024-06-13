import sys
import pygame

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font('SCRUBLAND.ttf', 50)
        self.font_small = pygame.font.Font('SCRUBLAND.ttf', 36)
        self.running = True
        self.selected_biome = None
        
        # Load background image
        self.background = pygame.image.load('images/background.png').convert()

        # Define button properties
        self.button_width = 150
        self.button_height = 50
        self.button_color = (139, 69, 19)  # Brown color
        self.button_hover_color = (160, 82, 45)  # Darker brown color
        self.button_radius = 10  # Radius for rounded corners

        # Define positions
        button_y = screen.get_height() // 2
        self.buttons = {
            "Ice": pygame.Rect((screen.get_width() // 4 - self.button_width // 2, button_y), (self.button_width, self.button_height)),
            "Green": pygame.Rect((3 * screen.get_width() // 4 - self.button_width // 2, button_y), (self.button_width, self.button_height)),
            "Desert": pygame.Rect((screen.get_width() // 4 - self.button_width // 2, button_y + 100), (self.button_width, self.button_height)),
            "Urban": pygame.Rect((3 * screen.get_width() // 4 - self.button_width // 2, button_y + 100), (self.button_width, self.button_height))
        }

    def display(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))
        
        # Render title text in black color
        title_text = self.font_large.render("Knife Hit Game", True, pygame.Color(0, 0, 0))  # Black color
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, self.screen.get_height() // 3))

        mouse_pos = pygame.mouse.get_pos()
        for text, rect in self.buttons.items():
            if rect.collidepoint(mouse_pos):
                color = self.button_hover_color
            else:
                color = self.button_color
            self.draw_rounded_rect(self.screen, color, rect, self.button_radius)
            button_text = self.font_small.render(text, True, (0, 0, 0))
            self.screen.blit(button_text, (rect.centerx - button_text.get_width() // 2, rect.centery - button_text.get_height() // 2))

        pygame.display.flip()

    def draw_rounded_rect(self, surface, color, rect, radius):
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for biome, rect in self.buttons.items():
                    if rect.collidepoint(event.pos):
                        self.selected_biome = biome.lower()
                        self.running = False

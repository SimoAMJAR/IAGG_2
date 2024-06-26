import pygame

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font('SCRUBLAND.ttf', 50)
        self.font_small = pygame.font.Font('SCRUBLAND.ttf', 36)
        self.running = True
        self.selected_biome = None
        
        self.background = pygame.image.load('images/background.png').convert()

        self.button_width = 150
        self.button_height = 50
        self.button_color = (255, 228, 181)
        self.button_hover_color = (193, 154, 107)
        self.button_radius = 10

        button_y = screen.get_height() // 2
        self.buttons = {
            "Ice": pygame.Rect((screen.get_width() // 4 - self.button_width // 2, button_y), (self.button_width, self.button_height)),
            "Green": pygame.Rect((3 * screen.get_width() // 4 - self.button_width // 2, button_y), (self.button_width, self.button_height)),
            "Desert": pygame.Rect((screen.get_width() // 4 - self.button_width // 2, button_y + 100), (self.button_width, self.button_height)),
            "Urban": pygame.Rect((3 * screen.get_width() // 4 - self.button_width // 2, button_y + 100), (self.button_width, self.button_height))
        }

        pygame.mixer.music.load('music/intro.mp3')
        pygame.mixer.music.play(-1) 
        pygame.mixer.music.set_volume(0.5)  

    def display(self):
        self.screen.blit(self.background, (0, 0))
        
        title_text = self.font_large.render("KNIFE TARGET", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 4))
        self.screen.blit(title_text, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        for biome, rect in self.buttons.items():
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, self.button_hover_color, rect, border_radius=self.button_radius)
            else:
                pygame.draw.rect(self.screen, self.button_color, rect, border_radius=self.button_radius)
            text = self.font_small.render(biome, True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for biome, rect in self.buttons.items():
                        if rect.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            self.selected_biome = biome.lower()
                            self.running = False

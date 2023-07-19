import pygame

from game.utils.constants import FONT_STYLE,WHITE,BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER, BG

class Menu:
    def __init__(self,message,screen):
        screen.fill(WHITE)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()
            elif game.death_count == 0 and event.type == pygame.K_INSERT:
                
                break

    def reset_screen_color(self,screen):
        screen.fill(WHITE)
    
    def update_message(self,screen, game):
        messages = ['Game Over, Press any key to restart',
                    f'Your Score: {game.score}', 
                    f'Highest Score: {game.high_score}',
                    f'Total Deaths {game.death_count}']
        Y = 300
        for message in messages:
            self.text = self.font.render(message, True, BLACK)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (SCREEN_WIDTH // 2, Y)
            screen.blit(self.text,self.text_rect)
            Y += 40

    def game_over(self, screen, game):
        game.draw_background()
        self.image = pygame.transform.scale(GAME_OVER,(200, 200))
        self.rect = self.image.get_rect()
        self.rect = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(self.image,self.rect)
        
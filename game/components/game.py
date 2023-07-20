import pygame
import sys
pygame.font.init()
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, WHITE,FONT_STYLE, HEART,MUTE, Y_SOUND, X_SOUND,MAX_SOUND,MIN_SOUND,SOUND, PAUSED,X_HEART,Y_HEART,X_P_HEART,Y_P_HEART, HEART_SPACE
from game.components.spaceship import SpaceShip
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.bursts.burst import Burst
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = SpaceShip()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu('Welcome crew member, Press Enter key to start...', self.screen)
        self.score = 0
        self.high_score = 0
        self.death_count = 5
        self.power_up_manager = PowerUpManager()
        self.list_sound = [MUTE,MAX_SOUND,MIN_SOUND,SOUND]


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self, self.screen)
        self.enemy_manager.update(self, user_input)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.draw_deaths(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.control_sounds()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.background(self.screen)

        if self.death_count == 5:
            self.menu.draw(self.screen)
        elif self.death_count == 0:
            self.menu.game_over(self.screen, self)
        else:
            self.menu.update_message(self.screen, self)
        
        icon = self.image = pygame.transform.scale(ICON, (80,120))
        self.screen.blit(icon, ((SCREEN_WIDTH //2) - 40, (60)))

        self.menu.update(self)

    def reset(self):
        self.score = 0
        self.explosion = []
        self.player.reset()
        self.power_up_manager.reset()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_deaths(self, screen):
        for death in range(self.death_count):
            heart_x = X_P_HEART + death * HEART_SPACE
            self.image = pygame.transform.scale(HEART, (X_HEART,Y_HEART))
            screen.blit(self.image, (heart_x, Y_P_HEART))

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/ 1000,2)

            if time_to_show >= 0:
                return ('hola')
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

    def draw_sounds(self,screen,image):
            self.image = pygame.transform.scale(image,(X_SOUND, Y_SOUND))
            self.rect = self.image.get_rect() 
            self.rect.x = (SCREEN_WIDTH // 2)
            self.rect.y = 20
            screen.blit(self.image, self.rect)

    def control_sounds(self):
        self.mute_sound()
        self.max_sound()
        self.up_sound()
        self.down_sound()

    def mute_sound(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
            self.draw_sounds(self.screen,self.list_sound[0])
        
    def max_sound(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_x]:
            pygame.mixer.music.set_volume(1.0)
            self.draw_sounds(self.screen,self.list_sound[3])

    def up_sound(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
            self.draw_sounds(self.screen,self.list_sound[1])
        elif key[pygame.K_w] and pygame.mixer.music.get_volume() == 1.0:
            self.draw_sounds(self.screen,self.list_sound[3])

    def down_sound(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_s] and pygame.mixer.music.get_volume() > 0.0 :
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
            self.draw_sounds(self.screen,self.list_sound[2])
        elif key[pygame.K_s] and pygame.mixer.music.get_volume() == 0.0:
            self.draw_sounds(self.screen,self.list_sound[0])

    
    def pause_game(self, screen):
        self.pause = True
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.display.quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.pause = False


                if event.type == pygame.K_q:
                    pygame.quit()
                    pygame.display.quit()
                    sys.exit()

        if not self.pause:
            screen.blit(HEART, (2000,200))
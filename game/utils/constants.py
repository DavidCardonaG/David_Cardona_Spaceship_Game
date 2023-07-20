import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SHIP_WIDTH = 40
SHIP_HEIGHT = 60
SHIP_WIDTH_TWO = 60
SHIP_HEIGHT_TWO = 80
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
WHITE = (255,255,255)
BLACK = (0,0,0)
SCORE = 0
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/game_over.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
MUTE = pygame.image.load(os.path.join(IMG_DIR,'Sounds/mute.png'))
MAX_SOUND = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/max.png'))
MIN_SOUND = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/min.png'))
SOUND = pygame.image.load(os.path.join(IMG_DIR, 'Sounds/sound.png'))
PAUSED = pygame.image.load(os.path.join(IMG_DIR,'Other/pausa.jpg'))
ALIEN = pygame.image.load(os.path.join(IMG_DIR,'Other/fondo_alien.jpg'))

MUSIC_FOND = pygame.mixer.Sound(os.path.join('game/assets/Sounds/music.ogg'))
LASER = pygame.mixer.Sound(os.path.join('game/assets/Sounds/laser.ogg'))
X_SOUND = 60
Y_SOUND = 60
X_HEART = 40
Y_HEART = 40
FONT_STYLE = 'freesansbold.ttf'

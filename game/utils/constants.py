import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/Explocion.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GAME_OVER.png"))
INICIO = pygame.image.load(os.path.join(IMG_DIR, 'Other/Galaxy.png'))
POWER_UP_STOP = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reloj.png'))

#sounds
BACKGROUND_MUSIC_PATH = os.path.join(IMG_DIR, 'sounds/starwras-guerra-de-las-galaxias-peliculas-.mp3')
DISPARO_MUSIC = os.path.join(IMG_DIR, 'sounds/scifi002.mp3')
GAME_OVER_MUSIC = os.path.join(IMG_DIR, 'sounds/game-over-1-gameover.mp3')
POWER_UP_MUSIC = os.path.join(IMG_DIR, 'sounds/01-power-up.mp3')



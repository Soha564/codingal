import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 400
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50 # random vertical range where enemies appear.
ENEMY_START_Y_MAX = 150 # random vertical range where enemiea appear
ENEMY_SPEED_X = 4 # how fast enemiea move down after touching side
ENEMY_SPEED_Y = 40 # how much enemies move after touching side
BULLET_SPEED_Y = 10 # how fast bullets move upward
COLLISION_DISTANCE = 27

# Initialising Pygame
pygame.init()
# Initialising music for pygame
pygame.mixer.init()


# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Music
pygame.mixer.music.load('retro-arcade-game-music-396890.mp3')  # Replace with your actual file name
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6 

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X) # Horizontal speed
    enemyY_change.append(ENEMY_SPEED_Y) #  Vertical speed

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font  =pygame.font.Font('freesansbold.ttf' , 32)
textX = 10
textY = 10

#Game Over Text
over_font  = pygame.font.Font('freesansbold.ttf', 64)

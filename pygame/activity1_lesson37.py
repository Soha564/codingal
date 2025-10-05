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

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

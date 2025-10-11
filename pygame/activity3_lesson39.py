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
font  = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#Game Over Text
over_font  = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    #Display the current score on the screen.
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))

    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text.
    over_text = over_font.render("GAME_OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire" # This means the bullet is now in motion (not ready anymore).
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)#This uses the distance formula to calculate how far the enemy is from the bullet.
    return distance < COLLISION_DISTANCE

#Game loop
running = True # Starts the infinite game loop
while running:
    screen.fill((0, 0, 0))#black color
    screen.blit(background, (0, 0))#background image on top

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:#press any key
          if event.key == pygame.K_LEFT:
              playerX_change = -5
          if event.key == pygame.K_RIGHT:
              playerX_change = 5
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:#release the key
          playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player it keeps the player inside the screen:

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000#enemy disappear
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]#moves the enemy horizontally.
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1#reverse the direction
            enemyY[i] += enemyY_change[i]#move one step downward

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y#reset the bullet
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)#enemy new position
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)#Calls the function enemy() to draw each enemy at its current location.

    # Bullet Movement
    if bulletY <= 0:#If the bullet goes off the top of the screen (
        bulletY = PLAYER_START_Y#reset bullet
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change#move bullet upward

    player(playerX, playerY)#Draws the player spaceship in the new position.
    show_score(textX, textY)
    pygame.display.update()                                                                                                                                                                                   
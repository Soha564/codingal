import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Movement Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite dimensions
SPRITE_WIDTH, SPRITE_HEIGHT = 50, 50

# Sprite positions
player_x, player_y = 100, 100
static_x, static_y = 400, 300

# Movement speed
speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # Draw sprites
    player_rect = pygame.Rect(player_x, player_y, SPRITE_WIDTH, SPRITE_HEIGHT)
    static_rect = pygame.Rect(static_x, static_y, SPRITE_WIDTH, SPRITE_HEIGHT)

    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, BLUE, static_rect)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

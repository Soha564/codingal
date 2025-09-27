import pygame
import sys
import random
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 800, 600

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Sprite & Custom events Example.")

# Clock (controls FPS)
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colour=RED):
        super().__init__() # Inherits Sprite class
        self.image = pygame.Surface((50, 50)) # Create square
        self.image.fill(colour) # Fill with given colour
        self.rect = self.image.get_rect() # Get rect for position
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed() # Check pressed keys
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.x -= 5
        if keys[pygame.K_DOWN]:
            self.rect.x += 5

# create sprite and group
all_sprites = pygame.sprite.Group()
player = Player(100, 100)
all_sprites.add(player)

# Custom event: change player colour

CHANGE_COLOUR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOUR, 2000)

# Main Loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == CHANGE_COLOUR:
            player.image.fill(BLUE)

    # Update
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

#FPS
clock.tick(60)
pygame.quit()
sys.exit
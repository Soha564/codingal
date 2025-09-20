# Write a program to create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My First Pygame Window")
player = pygame.image.load("Screenshot_20-9-2025_12529_www.bing.com.jpeg")
player = pygame.transform.scale(player, (200, 200))

running = True
while running:
    screen.fill((255, 255, 255))

    screen.blit(player, (150, 150))

# red ractangle
#    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 150, 100))
# blue circle
#    pygame.draw.circle(screen, (0, 0, 255), (300, 200), 50)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

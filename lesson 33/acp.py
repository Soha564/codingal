import pygame

pygame.init()

# Display
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

# Background color
background_color = (58, 58, 58)

# Image and size
image = pygame.image.load("Screenshot_20-9-2025_12529_www.bing.com.jpeg") 
image = pygame.transform.scale(image, (300, 300))

# Position image at the center
image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

running = True
while running:
    screen.fill((background_color))

    screen.blit(image, image_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

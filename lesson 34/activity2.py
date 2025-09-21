# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame Circle Example")
green = (0, 255, 0)
circle1 = pygame.circle(50, 60, 100, 80)

running = True
while running:
    screen.fill((255, 255, 255))

    # circle
    pygame.draw.circle(screen, (0, 0, 255), circle1)


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
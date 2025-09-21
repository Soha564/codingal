# Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame Rect Example")

rectangle1 = pygame.Rect(50, 60, 100, 80)

running = True
while running:
    screen.fill((0, 0, 0))

    #red rectangle
    pygame.draw.rect(screen, (0, 125, 255), rectangle1)


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
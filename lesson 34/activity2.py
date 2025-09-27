# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame Circle Example")
green = (0, 255, 0)
circle1 = pygame.circle(50, 60, 100, 80)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running - False

# Fill background
screen.fill(WHITE)

# Draw solid circle (filled)
pygame.draw.circle(screen, green, (200, 300), 80, 0)
# (surface, color, center(x,y), radius, width=0 + filled)

# Draw hollow circle (border width 3)
pygame.draw.circle(screen, green, (500, 300), 100, 3)
# width-3 + only border with thickness 3

# Update display
pygame.display.flip()

pygame.quit()

import pygame
pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

rectangle1 = pygame.Rect(50, 60, 100, 80)
rectangle1.center = (window_size[0] // 2, window_size[1] // 2)

font = pygame.font.Font(None, 36)
text = font.render("Hello, This Is A Rectangle: ", True, (255, 255, 255))

running = True
while running:
    screen.fill((0, 0, 0))

    #red rectangle
    pygame.draw.rect(screen, (0, 125, 255), rectangle1)

    screen.blit(text, (150, 20))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
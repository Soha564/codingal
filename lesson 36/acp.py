import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sprite Color Changer")

CHANGE_COLOR = pygame.USEREVENT + 1


class Box(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

    def change_color(self):
        new_color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.image.fill(new_color)

sprite1 = Box((100, 150), (255, 0, 0))  # Red
sprite2 = Box((300, 150), (0, 255, 0))  # Green

group = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR))
        elif e.type == CHANGE_COLOR:
            for s in group:
                s.change_color()

    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.flip()

pygame.quit()

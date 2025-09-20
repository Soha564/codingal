# Write a Python program to create an empty Pygame window.
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My First Pygame Window")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
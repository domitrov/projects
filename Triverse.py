import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

running = True

while running:
    screen.fill((128,128,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
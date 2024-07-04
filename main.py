import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        # pygame.QUIT means if the user clicks X, window closes
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
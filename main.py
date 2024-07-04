import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set window title and icon
pygame.display.set_caption("Project Game")
cowboy_icon = pygame.image.load("icons\cowboy_icon.png")
pygame.display.set_icon(cowboy_icon)

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(40, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        # pygame.QUIT means if the user clicks X, window closes
        if event.type == pygame.QUIT:
            running = False

    screen.fill((192,192,192))

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -=300 * dt
    if keys[pygame.K_s]:
        player_pos.y +=300 * dt
    # if keys[pygame.K_a]:
        # while player_pos.x != 0:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
        # while player_pos.x != screen.get_width():
        # player_pos.x += 300 * dt
        
    pygame.display.flip()
    dt = clock.tick(120) / 1000

pygame.quit()
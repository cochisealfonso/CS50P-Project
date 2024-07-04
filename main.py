import pygame

# Initialize Pygame and display
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set window title and icon
pygame.display.set_caption("Project Game")
cowboy_icon = pygame.image.load("icons\cowboy_icon.png")
pygame.display.set_icon(cowboy_icon)

# Variables
clock = pygame.time.Clock()
running = True
dt = 0

# Define player position
cowboyImage = pygame.image.load("icons\cowboy_player.png")
playerXPos = 30
playerYPos = screen.get_height() / 2

# Display player function
def player():
    screen.blit(cowboyImage, (playerXPos, playerYPos))

while running:
    screen.fill((255,204,153))
    for event in pygame.event.get():
        # pygame.QUIT means if the user clicks X, window closes
        if event.type == pygame.QUIT:
            running = False

    # Display player on screen
    player()

    # Directional controls for the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerYPos -=300 * dt
    if keys[pygame.K_s]:
        playerYPos +=300 * dt
    if keys[pygame.K_a]:
        playerXPos -= 300 * dt
    if keys[pygame.K_d]:
        playerXPos += 300 * dt
    

    pygame.display.flip()
    dt = clock.tick(120) / 1000

pygame.quit()
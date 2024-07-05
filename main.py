import pygame
from player import Player

# Initialize Pygame and display
pygame.init()
screen = pygame.display.set_mode((800, 600))
player = Player(playerType=1)


# Set window title and icon
pygame.display.set_caption("Project Game")
cowboy_icon = pygame.image.load("icons\cowboy_icon.png")
pygame.display.set_icon(cowboy_icon)

# Variables
clock = pygame.time.Clock()
running = True
dt = 0

# Define player position
cowboyImage = pygame.image.load("icons\cowboy_player1.png")
playerXPos = 30
playerYPos = screen.get_height() / 2

# Display player function
def player():
    screen.blit(cowboyImage, (playerXPos, playerYPos))

while running:
    for event in pygame.event.get():
        # pygame.QUIT means if the user clicks X, window closes
        if event.type == pygame.QUIT:
            running = False
    
    # Display player on screen
    screen.fill((255,204,153))
    player()

    # Directional controls for the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if playerYPos > (0): 
            playerYPos -= 300 * dt
        else:
            playerYPos += 350 * dt
    if keys[pygame.K_s]:
        if playerYPos < (screen.get_height() - 60):
            playerYPos += 300 * dt
        else:
            playerYPos -= 350 * dt
    if keys[pygame.K_a]:
        if playerXPos > (0): 
            playerXPos -= 300 * dt
        else:
            playerXPos += 350 * dt
    if keys[pygame.K_d]:
        if playerXPos < (screen.get_width() / 8):
            playerXPos += 300 * dt
        else:
            playerXPos -= 350 * dt
    
    pygame.display.flip()
    dt = clock.tick(120) / 1000

pygame.quit()
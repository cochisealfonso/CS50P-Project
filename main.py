import pygame
from player import Player

def main():
    # Initialize Pygame and display
    pygame.init()

    # Initialize window size, caption, and icon
    screen = set_window(800,600)

    # Initialize player
    """TO DO: Make the player choose player type"""
    player = Player(playerType=1, screen=screen)

    # Variables
    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            # Window closes if the user clicks X
            if event.type == pygame.QUIT:
                running = False
        
        # Display player on screen
        screen.fill((255,204,153))
        player.move(dt)
        
        pygame.display.flip()
        dt = clock.tick(120) / 1000

    pygame.quit()


def set_window(w, h):
    pygame.display.set_caption("The Last Cowboy")
    pygame.display.set_icon(pygame.image.load("icons\cowboy_icon.png"))
    return pygame.display.set_mode((w, h))


if __name__ == "__main__":
    main()
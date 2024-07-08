import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet

"""
TO DO:
    
    x Tidy up code for bullet mechanics
    x Fix enemy spawn functionality
    x Make player choose player type
    x Tidy up variables
    x ETC

"""

def main():
    # Initialize Pygame and display
    pygame.init()

    # Initialize window size, caption, icon, background
    screen, background = set_window(800,600)
    bullet_image = pygame.image.load("icons\\bullet.png")

    # Initialize player
    """TO DO: Make the player choose player type"""
    player = Player(playerType=1, screen=screen)

    """TO DO: Setup enemies"""
    enemy = Enemy(enemyType=1, screen=screen)
    enemy2 = Enemy(enemyType=1, screen=screen)

    # Variables
    clock = pygame.time.Clock()
    running = True
    dt = 0
    time_dt = 0
    do = "N"
    loaded = False
    bullet = player.load_gun(bullet_image)

    while running:
        for event in pygame.event.get():
            # Window closes if the user clicks X
            if event.type == pygame.QUIT:
                running = False
        
        # Display player on screen
        screen.fill((255,204,153))
        screen.blit(background, (0,0))
        player.move(dt)

        keys = pygame.key.get_pressed()
        
        if not loaded:
            if keys[pygame.K_SPACE]:
                loaded = True
                bullet = player.load_gun(bullet_image)
        
        loaded = bullet.fire(bullet_image, loaded, dt)
                    
        if time_dt >= 1:
            do = "Y"
            time_dt = 0
            
        enemy.spawn(dt,do)
        enemy2.spawn(dt,do)

        pygame.display.flip()
        dt = clock.tick(120) / 1000
        time_dt += dt
        
    pygame.quit()


def set_window(w, h):
    pygame.display.set_caption("The Last Cowboy")
    pygame.display.set_icon(pygame.image.load("icons\cowboy_icon.png"))
    background = pygame.image.load("icons\cowboy_bg.jpg")
    return pygame.display.set_mode((w, h)), background


if __name__ == "__main__":
    main()
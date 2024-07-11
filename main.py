import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet

"""
TO DO:
    
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
    player = Player(playerType=1, screen=screen)
    bullet = Bullet(bullet_image=bullet_image, screen=screen, XPos=player.XPos, YPos=player.YPos)

    # Initialize Enemies
    enemy = Enemy(enemyType=1, screen=screen)
    enemy2 = Enemy(enemyType=2, screen=screen)
    enemy3 = Enemy(enemyType=3, screen=screen)

    # Variables
    clock = pygame.time.Clock()
    running = True
    dt = 0
    time_dt = 0
    shoot = False
    
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

        # Bullet Mechanics
        if not shoot:
            if keys[pygame.K_SPACE]:
                bullet = Bullet(bullet_image=bullet_image, screen=screen, XPos=player.XPos, YPos=player.YPos)
                shoot = True

        shoot = bullet.fire(shoot, dt)

        # Spawn enemies:        
        enemy.spawn(dt,time_dt >= 1)
        enemy2.spawn(dt,time_dt >= 2)
        enemy3.spawn(dt,time_dt >= 3)

        # print(time_dt)
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
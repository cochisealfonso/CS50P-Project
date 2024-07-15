import pygame
import math
import random
from player import Player
from enemy import Enemy
from bullet import Bullet

"""
TO DO:
    

    x Tidy up start and end game code
    x Tidy up variables
    x ETC

"""

def main():
    # Initialize Pygame and display
    pygame.init()
    pygame.font.init()

    # Initialize window size, caption, icon, background, images
    screen, background = set_window(800,600)
    bullet_image = pygame.image.load("icons\\bullet.png")
    intro_image = pygame.image.load("icons\WASD.png")

    # Initialize player and bullet
    player = Player(playerType=1, screen=screen)
    bullet = Bullet(bullet_image=bullet_image, screen=screen, XPos=player.XPos, YPos=player.YPos)

    # Initialize Enemies
    enemy = Enemy(enemyType=1, screen=screen)
    enemy2 = Enemy(enemyType=2, screen=screen)
    enemy3 = Enemy(enemyType=3, screen=screen)
    enemy4 = Enemy(enemyType=4, screen=screen)

    # Variables
    clock = pygame.time.Clock()
    running = True
    dt = 0
    time_dt = 0
    shoot = False
    hit = False
    hit2 = False
    hit3 = False
    hit4 = False
    score = 0
    scoreX = 10
    scoreY = 10

    # Intro
    while running:
        for event in pygame.event.get():
            # Window closes if the user clicks X
            if event.type == pygame.QUIT:
                running = False

        # Press ENTER to start the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            break
        
        # Display background and instructions
        screen.fill((255,204,153))
        screen.blit(background, (0,0))
        screen.blit(intro_image, (250,50))
        font = pygame.font.Font('RangerEastwood.ttf',64)
        display_intro =  font.render("Press ENTER to Start", True, (255,255,255))
        screen.blit(display_intro, (200, 400))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    font = pygame.font.Font('RangerEastwood.ttf',32)


    # Main game
    while running:
        for event in pygame.event.get():
            # Window closes if the user clicks X
            if event.type == pygame.QUIT:
                running = False

        # Display player on screen
        screen.fill((255,204,153))
        screen.blit(background, (0,0))
        player.move(dt)

        # Bullet Mechanics
        keys = pygame.key.get_pressed()        
        if not shoot:
            if keys[pygame.K_SPACE]:
                bullet = Bullet(bullet_image=bullet_image, screen=screen, XPos=player.XPos, YPos=player.YPos)
                shoot = True

        shoot = bullet.fire(shoot, dt)

        # Spawn enemies:        
        enemy.spawn(dt,time_dt >= 1)
        enemy2.spawn(dt,time_dt >= 2)
        enemy3.spawn(dt,time_dt >= 3)
        enemy4.spawn(dt,time_dt >= 4)


        # Bullet-Enemy collision
        hit = collision(enemy.XPos, enemy.YPos, bullet.XPos, bullet.YPos)
        hit2 = collision(enemy2.XPos, enemy2.YPos, bullet.XPos, bullet.YPos)
        hit3 = collision(enemy3.XPos, enemy3.YPos, bullet.XPos, bullet.YPos)
        hit4 = collision(enemy4.XPos, enemy4.YPos, bullet.XPos, bullet.YPos)

        if hit:
            enemy.XPos = 800
            enemy.YPos = random.randint(30,570)
            shoot = False
            bullet.XPos = 0
            score += 1
        if hit2:
            enemy2.XPos = 800
            enemy2.YPos = random.randint(30,570)
            score += 1
            shoot = False
            bullet.XPos = 0
        if hit3:
            enemy3.XPos = 800
            enemy3.YPos = random.randint(30,570)
            shoot = False
            bullet.XPos = 0
            score += 1
        if hit4:
            enemy4.XPos = 800
            enemy4.YPos = random.randint(30,570)
            shoot = False
            bullet.XPos = 0
            score += 1

        if enemy.XPos < 160 or enemy2.XPos < 160 or enemy3.XPos < 160 or enemy4.XPos < 160:
            break

        show_score(font, score, scoreX, scoreY, screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        time_dt += dt

    # END GAME
    while running:
        for event in pygame.event.get():
            # Window closes if the user clicks X
            if event.type == pygame.QUIT:
                running = False

        # Display background
        screen.fill((255,204,153))
        screen.blit(background, (0,0))

        # Display score
        show_score(font=pygame.font.Font('RangerEastwood.ttf',128), score=score, scoreX = 200, scoreY = 200, screen=screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    pygame.quit()


def set_window(w, h):
    pygame.display.set_caption("The Last Cowboy")
    pygame.display.set_icon(pygame.image.load("icons\cowboy_icon.png"))
    background = pygame.image.load("icons\cowboy_bg.jpg")
    return pygame.display.set_mode((w, h)), background


def collision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    if distance <= 20:
        return True
    else:
        return False


def show_score(font, score, scoreX, scoreY, screen):
    display_score =  font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(display_score, (scoreX, scoreY))
    

if __name__ == "__main__":
    main()
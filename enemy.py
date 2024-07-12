import pygame
import random

class Enemy:
    def __init__(self, enemyType, screen, XPos=700, YPos=random.randint(30,570)):
        self.playertype = pygame.image.load(f"icons\enemy{enemyType}.png")
        self.screen = screen
        self.XPos = XPos
        self.YPos = random.randint(30,570)

    # Directional controls for the player
    def spawn(self, dt, bool):
        if bool:
            self.screen.blit(self.playertype, (self.XPos, self.YPos))
            self.XPos -= 100 * dt
            if self.XPos < 150:
                self.XPos = 800 
                self.YPos = random.randint(30, 570)
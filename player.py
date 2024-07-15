import pygame
from bullet import Bullet

class Player:
    def __init__(self, playerType, screen, XPos=30, YPos=300):
        self.playertype = pygame.image.load(f"icons\cowboy_player{playerType}.png")
        self.screen = screen
        self.XPos = XPos
        self.YPos = YPos

    # Directional controls for the player
    def move(self, dt):
        self.screen.blit(self.playertype, (self.XPos, self.YPos))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.YPos > (0): 
                self.YPos -= 300 * dt
            else:
                self.YPos += 350 * dt
        if keys[pygame.K_s]:
            if self.YPos < (self.screen.get_height() - 60):
                self.YPos += 300 * dt
            else:
                self.YPos -= 350 * dt
        if keys[pygame.K_a]:
            if self.XPos > (0): 
                self.XPos -= 300 * dt
            else:
                self.XPos += 350 * dt
        if keys[pygame.K_d]:
            if self.XPos < (self.screen.get_width() / 8):
                self.XPos += 300 * dt
            else:
                self.XPos -= 350 * dt
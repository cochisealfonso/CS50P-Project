import pygame

class Bullet:
    def __init__(self, bullet, screen, XPos, YPos):
        self.bullet = bullet
        self.screen = screen
        self.XPos = XPos
        self.YPos = YPos

    # Directional controls for the player
    def fire(self, bullet_image, loaded, dt):
        if self.XPos >= 750:
            self.XPos = 800
            return False
        elif loaded:
            self.screen.blit(bullet_image, (self.XPos, self.YPos))
            self.XPos += 350 * dt
            return True

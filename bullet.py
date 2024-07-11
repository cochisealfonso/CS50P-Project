import pygame

class Bullet:
    def __init__(self, bullet_image, screen, XPos, YPos):
        self.bullet_image = bullet_image
        self.screen = screen
        self.XPos = XPos + 45
        self.YPos = YPos + 35

    # Bullet fire 
    def fire(self, shoot, dt):
        if shoot:
            if self.XPos >= 750:
                self.screen.blit(self.bullet_image, (self.XPos, self.YPos))
                self.XPos = 850
                return False
            else:
                self.screen.blit(self.bullet_image, (self.XPos, self.YPos))
                self.XPos += 350 * dt
                return True
        else:
            self.XPos = 0
            
    

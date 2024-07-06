import pygame

class Player:
    def __init__(self, playerType, XPos=30, YPos=300):
        self.playertype = pygame.image.load(f"icons\cowboy_player{playerType}.png")
        self.XPos = XPos
        self.YPos = YPos

    # Directional controls for the player
    def move(self):
        screen = pygame.display.set_mode((800, 600))
        screen.blit(self.playertype, (self.XPos, self.YPos))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            playerYPos -=300 * dt
        if keys[pygame.K_s]:
            playerYPos +=300 * dt
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
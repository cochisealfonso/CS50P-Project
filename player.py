import pygame

class Player:
    def __init__(self, playerType):
        self.type = playerType

    # def load(self, screen):
        # clock = pygame.time.Clock()
        # dt = 0

        # cowboyImage = pygame.image.load(f"icons\cowboy_player{self.type}.png")
        # playerXPos = 30
        # playerYPos = 300

        # screen.blit(cowboyImage, (playerXPos, playerYPos))
        # return playerXPos, playerYPos

    # Directional controls for the player
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     playerYPos -=300 * dt
        # if keys[pygame.K_s]:
        #     playerYPos +=300 * dt
        # if keys[pygame.K_a]:
        #     if playerXPos > (0): 
        #         playerXPos -= 300 * dt
        #     else:
        #         playerXPos += 350 * dt
        # if keys[pygame.K_d]:
        #     if playerXPos < (screen.get_width() / 8):
        #         playerXPos += 300 * dt
        #     else:
        #         playerXPos -= 350 * dt

        # pygame.display.flip()
        # dt = clock.tick(120) / 1000
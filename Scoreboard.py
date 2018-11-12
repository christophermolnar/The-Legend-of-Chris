import pygame
import sys
from os import path
from GameSetting import *

# heart Images
HEART_IMG = pygame.image.load(PICTURE_PATH + "heart.png")
HEART_INVINCIBLE_IMG = pygame.image.load(PICTURE_PATH + "heartInvincible.png")


# Scoreboard
# The scoreboard at the top of the screen
class Scoreboard():

    # __init__
    # Create a Item object
    # Parameters: Game object, top x-position, top y-position, bottom x-position, bottom y-position
    def __init__(self, game, tx = 0, ty = 0, bx = WIDTH, by = SCORE_BOARD_TILES * TILE_SIZE):
        self.game = game
        #self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        #self.image.fill(BLACK)
        #self.rect = self.image.get_rect()
        self.tx = tx
        self.ty = ty
        self.bx = bx
        self.by = by
        self.font = pygame.font.SysFont(FONT_NAME, 25)


    def update(self, points, lives):

        pass


    def draw(self, currentTime, currentPointTotal, numberOfLivesLeft):

        # Background
        pygame.draw.rect(self.game.screen, BLACK, (self.tx, self.ty, self.bx, self.by))
        #scoreboardTextSpace = (WIDTH/TILE_SIZE -2) == 33 (Have items at 1, 12, 23)
        # Score
        textSurface = self.font.render("TIME: " + str(currentTime), True, WHITE)
        self.game.screen.blit(textSurface, (TILE_SIZE, TILE_SIZE))
        # Points
        textSurface = self.font.render("POINTS: " + str(currentPointTotal), True, WHITE)
        self.game.screen.blit(textSurface, (12 * TILE_SIZE, TILE_SIZE))
        # Life
        textSurface = self.font.render("LIFE: ", True, WHITE)
        self.game.screen.blit(textSurface, (23 * TILE_SIZE, TILE_SIZE))
        heartPicture = HEART_IMG
        if (self.game.player.isPlayerInvincible()):
            heartPicture = HEART_INVINCIBLE_IMG
        for hearts in range(0, numberOfLivesLeft):
            self.game.screen.blit(heartPicture, ((27 + hearts) * TILE_SIZE, 1.5 * TILE_SIZE))

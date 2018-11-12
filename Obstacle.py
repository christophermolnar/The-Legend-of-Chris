import pygame
from os import path
from GameSetting import *

# Obstacle Images
BUSH_IMG = pygame.image.load(PICTURE_PATH + "bush.png")

# Resources (Super Class)
# Different Map resources (Ex: Bushes)
class Obstacle(pygame.sprite.Sprite):

    # __init__
    # Creates a resource object
    # Parameters: Game object, x position for the Resource and y position for the Resource
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

# Bush (Sub Class)
# A bush
class Bush(Obstacle):

    # __init__
    # Create a bush using the Resource Super Class
    # Parameters: Game object, x position for the Bush and y position for the Bush
    def __init__(self, game, x, y):
        Obstacle.__init__(self, game, x, y)
        self.groups = game.all_sprites, game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = BUSH_IMG

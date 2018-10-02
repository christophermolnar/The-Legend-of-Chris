import pygame
from os import path
from GameSetting import *

# Item Images
RupeeImg = pygame.image.load(pictures_path + "rupee.png")

# Item (Super Class)
# Different items for the player to collect (Ex: Rupee)
class Item(pygame.sprite.Sprite):

    # __init__
    # Create a Item object
      # Parameters: Game object, x position for the Item and y position for the Item
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


# Rupee (Sub Class)
class Rupee(Item):

    # __init__
    # Create a Rupee object using the Item Super Class
    # Parameters: Game object, x position for the Rupee and y position for the Rupee
    def __init__(self, game, x, y):
        Item.__init__(self, game, x, y)
        self.image = RupeeImg
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)

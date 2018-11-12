import pygame
from os import path
from GameSetting import *
from Enemies import *

# Item Images
RUPEE_IMG = pygame.image.load(PICTURE_PATH + "rupee.png")
SWORD_UP_IMG = pygame.image.load(PICTURE_PATH + "swordUp.png")
SWORD_DOWN_IMG = pygame.image.load(PICTURE_PATH + "swordDown.png")
SWORD_LEFT_IMG = pygame.image.load(PICTURE_PATH + "swordLeft.png")
SWORD_RIGHT_IMG = pygame.image.load(PICTURE_PATH + "swordRight.png")

# Sword Dictionary
SWORD_IMG_DICTIONARY = {'U': SWORD_UP_IMG, 'D' : SWORD_DOWN_IMG, 'L' : SWORD_LEFT_IMG, 'R' : SWORD_RIGHT_IMG}

# Sword Offset
SWORD_IMG_OFFSET = {'U': [2, -12], 'D' : [5, 16], 'L' : [-12, 6], 'R' : [15, 6]}

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
# Currency for the player to collect, that will increase the players points
class Rupee(Item):

    # __init__
    # Create a Rupee object using the Item Super Class
    # Parameters: Game object, x position for the Rupee and y position for the Rupee
    def __init__(self, game, x, y):
        Item.__init__(self, game, x, y)
        self.image = RUPEE_IMG
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)


# Sword (Sub Class)
# Weapon for the player to attack with
class Sword(Item):

    # __init__
    # Create a Sword object using the Item Super Class
    # Parameters: Game object, x position for the Rupee and y position for the Rupee
    def __init__(self, game, x, y, direction):
        x = x + SWORD_IMG_OFFSET[direction][0]
        y = y + SWORD_IMG_OFFSET[direction][1]
        self.game = game
        self.image = SWORD_IMG_DICTIONARY[direction]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.groups = game.all_sprites, game.playerItems
        pygame.sprite.Sprite.__init__(self, self.groups)


    # Update method for the sword
    def update(self):
        if (self.game.player.state != "attack"): # Destroy the sword object after attacking
            self.kill()
        collide = pygame.sprite.spritecollideany(self, self.game.enemies)
        if (collide): # Defeat enemy when hit with sword
                collide.kill()
                self.game.points += 20

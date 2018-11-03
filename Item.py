import pygame
from os import path
from GameSetting import *
from Enemies import *

# Item Images
RupeeImg = pygame.image.load(pictures_path + "rupee.png")
swordUpImg = pygame.image.load(pictures_path + "swordUp.png")
swordDownImg = pygame.image.load(pictures_path + "swordDown.png")
swordLeftImg = pygame.image.load(pictures_path + "swordLeft.png")
swordRightImg = pygame.image.load(pictures_path + "swordRight.png")

# Sword Dictionary
swordImgDictionary = {'U': swordUpImg, 'D' : swordDownImg, 'L' : swordLeftImg, 'R' : swordRightImg}

# Sword Offset
swordImgOffset = {'U': [2, -12], 'D' : [5, 16], 'L' : [-12, 6], 'R' : [15, 6]}

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
            
        
# Sword (Sub Class)
class Sword(Item):

    # __init__
    # Create a Sword object using the Item Super Class
    # Parameters: Game object, x position for the Rupee and y position for the Rupee
    def __init__(self, game, x, y, direction):
        x = x + swordImgOffset[direction][0]
        y = y + swordImgOffset[direction][1]
        self.game = game
        self.image = swordImgDictionary[direction]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y        
        self.groups = game.all_sprites, game.playerItems
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        
    
    def update(self): 
        if (self.game.player.state != "attack"): # Destroy the sword object after attacking
            self.kill() 
        collide = pygame.sprite.spritecollideany(self, self.game.enemies)
        if (collide): # Defeat enemy when hit with sword
                collide.kill()
                self.game.points += 20        
        
        

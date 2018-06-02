import pygame
from GameSetting import *

#Enemies Images
OctoF1Img= pygame.image.load(pictures_path + "octo forward 1.png")

# Enemies (Super Class)
class Enemies(pygame.sprite.Sprite):

    # __init__ 
    # Creates a Enemy
    # Parameters: game object, x position of the enemy and y position of the enemy
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.state = 'walk' 
        #self.image_list = self.animation_list[self.state][self.direction]
        #self.image_index = 0
        #self.image = self.image_list[self.image_index]
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.pos = pygame.math.Vector2(x * TILE_SIZE, y * TILE_SIZE)
        self.vel = 0
        
# OrangeOcto (Sub Class)
class OrangeOcto(Enemies):
    
    # __init__ 
    # Creates a OrangeOcto with the Enemies Super Class
    # Parameters: game object, x position of the OrangeOcto and y position of the OrangeOcto
    def __init__(self, game, x, y):
        Enemies.__init__(self, game, x, y)
        self.image = OctoF1Img
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
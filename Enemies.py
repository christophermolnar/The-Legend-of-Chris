import pygame
from GameSetting import *

#Enemies
OctoF1Img= pygame.image.load(pictures_path + "octo forward 1.png")

class Enemies(pygame.sprite.Sprite):

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
        

class OrangeOcto(Enemies):
    
    def __init__(self, game, x, y):
        Enemies.__init__(self, game, x, y)
        self.image = OctoF1Img
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
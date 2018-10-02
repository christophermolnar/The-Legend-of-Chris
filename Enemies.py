import pygame
import math
from GameSetting import *

#Enemies Images
OctoF1Img= pygame.image.load(pictures_path + "octo forward 1.png")

# Enemies (Super Class)
class Enemies(pygame.sprite.Sprite):

    # __init__ 
    # Creates a Enemy
    # Parameters: game object, x position of the enemy and y position of the enemy
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
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
        self.start_pos = pygame.math.Vector2(x * TILE_SIZE, y * TILE_SIZE)
        self.pos = pygame.math.Vector2(x * TILE_SIZE, y * TILE_SIZE)
        self.vel = 0
        self.spotting_distance = 10 * TILE_SIZE
        self.attacking_distance = 5 * TILE_SIZE
        self.speed = 10
     
     
    def move_x(self, destination):
        if (self.pos.x - destination.x > 0):
            self.pos.x -= self.speed * self.game.dt
        else:
            self.pos.x += self.speed * self.game.dt         
    
      
    def move_y(self, destination):  
        if (self.pos.y - destination.y > 0):
            self.pos.y -= self.speed * self.game.dt
        else:
            self.pos.y += self.speed * self.game.dt           
     
        
    def calculate_move(self, destination):

        difference_in_x = math.fabs(self.pos.x - destination.x)
        difference_in_y = math.fabs(self.pos.y - destination.y)

        if (difference_in_x < difference_in_y and (difference_in_x > TILE_SIZE/2)):
            self.move_x(destination)
        elif (difference_in_x > difference_in_y and (difference_in_y > TILE_SIZE/2)):
            self.move_y(destination)  
        elif (difference_in_x < difference_in_y and (difference_in_x < TILE_SIZE/2)):
            self.move_y(destination) 
        elif (difference_in_x > difference_in_y and (difference_in_y < TILE_SIZE/2)):
            self.move_x(destination)         

        self.rect.topleft = (self.pos.x, self.pos.y)  
        print("ENEMY x:" + str(self.pos.x))
        print("ENEMY y:" + str(self.pos.y))


    def update(self):

        player_position = self.game.player.pos

        #print("player position: " + self.game.player.pos)
        #print("enemy position: " + self.pos)
        #
        distance_to_player =  self.pos.distance_to(player_position)
        
        x_target = math.fabs(self.pos.x - player_position.x)
        y_target = math.fabs(self.pos.y - player_position.y)

        #if (distance_to_player <= self.attacking_distance and (x_target < TILE_SIZE/2 or y_target < TILE_SIZE/2)):
            ##attack
            #print("Can Attack")
        #if (distance_to_player <= self.spotting_distance):
            ##move towards player
            #self.calculate_move(player_position)
            #print("Can Move Towards")    
        ## Random patrol in a pattern
        
        ## Return to gaurd post
        #else:
            #print("original position = " + str(self.start_pos))
            #self.calculate_move(self.start_pos)
        ##Retreat
        
        
# OrangeOcto (Sub Class)
class OrangeOcto(Enemies):
    
    #const.ORANGE_OCTO_SPEED = 75
    
    # __init__ 
    # Creates a OrangeOcto with the Enemies Super Class
    # Parameters: game object, x position of the OrangeOcto and y position of the OrangeOcto
    def __init__(self, game, x, y):
        Enemies.__init__(self, game, x, y)
        self.image = OctoF1Img
        self.speed = 75
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
      
 
        
        
        

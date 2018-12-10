import pygame
import math
from GameSetting import *

# Moving Pictures
# Octo Images
OCTO_UP_1_IMG = pygame.image.load(PICTURE_PATH + "octoUp1.png")
OCTO_UP_2_IMG = pygame.image.load(PICTURE_PATH + "octoUp2.png")
OCTO_DOWN_1_IMG= pygame.image.load(PICTURE_PATH + "octoDown1.png")
OCTO_DOWN_2_IMG = pygame.image.load(PICTURE_PATH + "octoDown2.png")
OCTO_LEFT_1_IMG = pygame.image.load(PICTURE_PATH + "octoLeft1.png")
OCTO_LEFT_2_IMG = pygame.image.load(PICTURE_PATH + "octoLeft2.png")
OCTO_RIGHT_1_IMG = pygame.image.load(PICTURE_PATH + "octoRight1.png")
OCTO_RIGHT_2_IMG = pygame.image.load(PICTURE_PATH + "octoRight2.png")
# Dog Images
#Moving Pictures
DOG_UP_1_IMG = pygame.image.load(PICTURE_PATH + "dogUp1.png")
DOG_UP_2_IMG = pygame.image.load(PICTURE_PATH + "dogUp2.png")
DOG_DOWN_1_IMG= pygame.image.load(PICTURE_PATH + "dogDown1.png")
DOG_DOWN_2_IMG = pygame.image.load(PICTURE_PATH + "dogDown2.png")
DOG_LEFT_1_IMG = pygame.image.load(PICTURE_PATH + "dogLeft1.png")
DOG_LEFT_2_IMG = pygame.image.load(PICTURE_PATH + "dogLeft2.png")
DOG_RIGHT_1_IMG = pygame.image.load(PICTURE_PATH + "dogRight1.png")
DOG_RIGHT_2_IMG = pygame.image.load(PICTURE_PATH + "dogRight2.png")

# A Dicionary for the octo sprites. This is a Dictionay of directions (key) and sprites (values)
OCTO_ANIMATION_DICTIONARY = {'U': [OCTO_UP_1_IMG, OCTO_UP_2_IMG], 'D': [OCTO_DOWN_1_IMG, OCTO_DOWN_2_IMG], 'L': [OCTO_LEFT_1_IMG, OCTO_LEFT_2_IMG], 'R': [OCTO_RIGHT_1_IMG, OCTO_RIGHT_2_IMG]}
# A Dicionary for the dog sprites. This is a Dictionay of directions (key) and sprites (values)
DOG_ANIMATION_DICTIONARY = {'U': [DOG_UP_1_IMG, DOG_UP_2_IMG], 'D': [DOG_DOWN_1_IMG, DOG_DOWN_2_IMG], 'L': [DOG_LEFT_1_IMG, DOG_LEFT_2_IMG], 'R': [DOG_RIGHT_1_IMG, DOG_RIGHT_2_IMG]}


# Enemies (Super Class)
class Enemies(pygame.sprite.Sprite):

    # __init__
    # Creates a Enemy
    # Parameters: game object, x position of the enemy and y position of the enemy
    def __init__(self, game, x, y, enemyAnimationDictionary, direction, xSpeed, ySpeed):
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.state = 'walk'
        self.direction = direction
        self.changeDirectionFlag = False
        self.animationDictionary = enemyAnimationDictionary
        self.imageList = self.animationDictionary[self.direction]
        self.image_index = 0
        self.image = self.imageList[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.startPosition = pygame.math.Vector2(x * TILE_SIZE, y * TILE_SIZE)
        self.pos = pygame.math.Vector2(x * TILE_SIZE, y * TILE_SIZE)
        self.vel = pygame.math.Vector2(xSpeed, ySpeed)
        self.spotting_distance = 10 * TILE_SIZE
        self.attacking_distance = 5 * TILE_SIZE
        self.speed = 10


    # straightLineMove
    # Moving the enemy in a horizontal or vertical direction
    def straightLineMove(self, xMovement, yMovement, speed):

        self.pos.x += self.vel[0] * self.game.dt
        self.pos.y += self.vel[1] * self.game.dt
        self.rect.topleft = (self.pos.x, self.pos.y)
        self.chamgeDirectionFlag = False

        if pygame.sprite.spritecollideany(self, self.game.obstacles):
            self.pos.x -= self.vel[0] * self.game.dt
            self.pos.y -= self.vel[1] * self.game.dt
            self.rect.topleft = (self.pos.x, self.pos.y)
            self.vel[0] = - self.vel[0]
            self.vel[1] = - self.vel[1]
            self.changeDirectionFlag = True


    # getDirections
    # Get the direction that the enemy is moving in
    def getDirection(self):
        if (self.vel[0] > 0 ):
            return 'R'
        elif (self.vel[0] < 0 ):
            return 'L'
        if (self.vel[1] < 0 ):
            return 'U'
        elif (self.vel[1] > 0 ):
            return 'D'        
     
        
    # animation
    # Alternates the sprites
    # Returns: The enemy sprite to display
    def animation(self):
        if self.image_index < (len(self.image_list) - 1):
            self.image_index += 1
        else:
            self.image_index = 0

        return self.image_list[self.image_index]    

    
    # Not Used
    def move_x(self, destination):
        if (self.pos.x - destination.x > 0):
            self.pos.x -= self.speed * self.game.dt
        else:
            self.pos.x += self.speed * self.game.dt


    # Not Used
    def move_y(self, destination):
        if (self.pos.y - destination.y > 0):
            self.pos.y -= self.speed * self.game.dt
        else:
            self.pos.y += self.speed * self.game.dt


    # Not Used
    def calculate_move(self, destination):

        differenceInXPosition = math.fabs(self.pos.x - destination.x)
        differenceInYPosition = math.fabs(self.pos.y - destination.y)

        if (differenceInXPosition < differenceInYPosition and (differenceInXPosition > TILE_SIZE/2)):
            self.move_x(destination)
        elif (differenceInXPosition > differenceInYPosition and (differenceInYPosition > TILE_SIZE/2)):
            self.move_y(destination)
        elif (differenceInXPosition < differenceInYPosition and (differenceInXPosition < TILE_SIZE/2)):
            self.move_y(destination)
        elif (differenceInXPosition > differenceInYPosition and (differenceInYPosition < TILE_SIZE/2)):
            self.move_x(destination)

        self.rect.topleft = (self.pos.x, self.pos.y)
        print("ENEMY x:" + str(self.pos.x))
        print("ENEMY y:" + str(self.pos.y))

    
    # update    
    # Update the enemy 
    def update(self):

        self.straightLineMove(0, 0, 0)
        
        if ((self.game.counter % 15 == 0) or self.changeDirectionFlag): # alternate every 10 frames or if the direction changes
            self.direction = self.getDirection()
            self.image_list = self.animationDictionary[self.direction]
            self.image = self.animation()    
            self.changeDirectionFlag = False

        
        # *** Not Used Code ***
        #playerPosition = self.game.player.pos

        #print("player position: " + self.game.player.pos)
        #print("enemy position: " + self.pos)
        #
        #distanceToPlayer =  self.pos.distance_to(playerPosition)

        #xTarget = math.fabs(self.pos.x - playerPosition.x)
        #yTarget = math.fabs(self.pos.y - playerPosition.y)

        #if (distanceToPlayer <= self.attacking_distance and (xTarget < TILE_SIZE/2 or yTarget < TILE_SIZE/2)):
            ##attack
            #print("Can Attack")
        #if (distanceToPlayer <= self.spotting_distance):
            ##move towards player
            #self.calculate_move(playerPosition)
            #print("Can Move Towards")
        ## Random patrol in a pattern

        ## Return to gaurd post
        #else:
            #print("original position = " + str(self.startPosition))
            #self.calculate_move(self.startPosition)
        ##Retreat
        # *** Not Used Code ***


# OrangeOcto (Sub Class)
class OrangeOcto(Enemies):

    # __init__
    # Creates a OrangeOcto with the Enemies Super Class
    # Parameters: game object, x position of the OrangeOcto and y position of the OrangeOcto
    def __init__(self, game, x, y, startingDirection, xSpeed, ySpeed):
        Enemies.__init__(self, game, x, y, OCTO_ANIMATION_DICTIONARY, startingDirection, xSpeed, ySpeed)
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        
# DogGuard (Sub Class)
class DogGuard(Enemies):

    # __init__
    # Creates a dog guard with the Enemies Super Class
    # Parameters: game object, x position of the dog guard and y position of the dog guard
    def __init__(self, game, x, y, startingDirection, xSpeed, ySpeed):
        Enemies.__init__(self, game, x, y, DOG_ANIMATION_DICTIONARY, startingDirection, xSpeed, ySpeed)
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

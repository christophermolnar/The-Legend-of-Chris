import pygame
from os import path
from GameSetting import *
from Enemies import *

#Moving Pictures
ChrisF1Img= pygame.image.load(pictures_path + "chris forward 1.png")
ChrisF2Img= pygame.image.load(pictures_path + "chris forward 2.png")
ChrisB1Img= pygame.image.load(pictures_path + "chris backwards 1.png")
ChrisB2Img= pygame.image.load(pictures_path + "chris backwards 2.png")
ChrisL1Img= pygame.image.load(pictures_path + "chris left 1.png")
ChrisL2Img= pygame.image.load(pictures_path + "chris left 2.png")
ChrisR1Img= pygame.image.load(pictures_path + "chris right 1.png")
ChrisR2Img= pygame.image.load(pictures_path + "chris right 2.png")
#Attack Pictures
ChrisAFImg= pygame.image.load(pictures_path + "chris attack forward.png")
ChrisABImg= pygame.image.load(pictures_path + "chris attack back.png")
ChrisALImg= pygame.image.load(pictures_path + "chris attack left.png")
ChrisARImg= pygame.image.load(pictures_path + "chris attack right.png")


# Player
# The player controlled by the user
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.direction = 'U'
        self.state = 'walk'
        self.alive = True
        self.animation_list = self.create_animation_dict()
        self.image_list = self.animation_list[self.state][self.direction]
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (15 * TILE_SIZE, 15 * TILE_SIZE)
        self.timer = 0.0
        self.pos = pygame.math.Vector2(15 * TILE_SIZE, 15 * TILE_SIZE)
        self.vel = pygame.math.Vector2(0, 0)
        #self.acc = pygame.math.Vector2(0, 0)


    # create_animation_dict
    # Creates a dictionary with the players sprites
    # The Dictionaries keys are walk, and attack: the corresponding values are dictionaries with a list of sprites inside
    # Returns: A dictionary with the player sprites
    def create_animation_dict(self):

        # ***Will Resize Later***
        size = (32,32)
        # *** ***

        walkU1 = ChrisB1Img
        walkU2 = ChrisB2Img
        walkD1 = ChrisF1Img
        walkD2 = ChrisF2Img
        walkL1 = ChrisL1Img
        walkL2 = ChrisL2Img
        walkR1 = ChrisR1Img
        walkR2 = ChrisR2Img
        attackU = ChrisABImg
        attackD = ChrisAFImg
        attackL = ChrisALImg
        attackR = ChrisARImg

        # Animation Dictionary Dictionary (A Dictionay of actions with a Dictionary of directions to give the proper animation list)
        animation_dict = {'walk': {'U': [walkU1, walkU2], 'D': [walkD1, walkD2], 'L': [walkL1, walkL2], 'R': [walkR1, walkR2]},
                      'attack': {'U': [attackU], 'D': [attackD], 'L': [attackL], 'R': [attackR]}}

        return animation_dict


    # animation
    # Alternates the sprites
    # Returns: The players sprite to display
    def animation(self):
        if self.image_index < (len(self.image_list) - 1):
            self.image_index += 1
        else:
            self.image_index = 0

        return self.image_list[self.image_index]


    # get_keys
    # Gets the keys pressed by the user and converts them into the players state, direction and velocity
    def get_keys(self):
        self.vel = (0, 0)
        keys =pygame.key.get_pressed()
        self.state = "rest"
        if (keys[pygame.K_SPACE]):
            self.state = "attack"
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.vel = (-PLAYER_SPEED, 0)
            self.state = "walk"
            self.direction = 'L'
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.vel = (PLAYER_SPEED, 0)
            self.state = "walk"
            self.direction = 'R'
        elif (keys[pygame.K_UP] or keys[pygame.K_w]):
            self.vel = (0, -PLAYER_SPEED)
            self.state = "walk"
            self.direction = 'U'
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.vel = (0, PLAYER_SPEED)
            self.state = "walk"
            self.direction = 'D'


    # update
    # Updates the player: moves the player
    def update(self):
        previous_direction = self.direction
        previous_state = self.state
        self.get_keys()
        if (self.state != 'rest'): #if the player moved
            self.pos.x += self.vel[0] * self.game.dt
            self.pos.y += self.vel[1] * self.game.dt
            self.rect.topleft = (self.pos.x, self.pos.y)
            if ((self.game.counter % 10 == 0) or (previous_direction != self.direction) or (self.state != previous_state)): # alternate every 10 frames or if the direction or state changes
                self.image_list = self.animation_list[self.state][self.direction]
                self.image = self.animation()
            if pygame.sprite.spritecollideany(self, self.game.obstacles):
                self.pos.x -= self.vel[0] * self.game.dt
                self.pos.y -= self.vel[1] * self.game.dt
                self.rect.topleft = (self.pos.x, self.pos.y)

            collide = pygame.sprite.spritecollideany(self, self.game.enemies)

            if (collide != None):
                if (self.state == "attack"): # Defeat the enemy
                    collide.kill()
                    #defeat_monster =  pygame.sprite.spritecollide(self, self.game.enemies, True) # Collect Rupee
                else: # Enemy Attacks you
                    self.alive = False
                    self.kill()
                    self.game.player.kill()
                    return
                    #Player takes a damage
                    #Check health
                    #Lose points
            collects_rupee =  pygame.sprite.spritecollide(self, self.game.items, True) # Collect Rupee
            if (collects_rupee):
                pass
        elif (previous_state == "attack"): # After attacking switch back to a standard image
            self.image_list = self.animation_list["walk"][self.direction]
            self.image = self.animation()

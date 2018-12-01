import pygame
from os import path
from GameSetting import *
from Enemies import *
from Item import *

#Moving Pictures
PLAYER_UP_1_IMG = pygame.image.load(PICTURE_PATH + "chrisUp1.png")
PLAYER_UP_2_IMG = pygame.image.load(PICTURE_PATH + "chrisUp2.png")
PLAYER_DOWN_1_IMG= pygame.image.load(PICTURE_PATH + "chrisDown1.png")
PLAYER_DOWN_2_IMG = pygame.image.load(PICTURE_PATH + "chrisDown2.png")
PLAYER_LEFT_1_IMG = pygame.image.load(PICTURE_PATH + "chrisLeft1.png")
PLAYER_LEFT_2_IMG = pygame.image.load(PICTURE_PATH + "chrisLeft2.png")
PLAYER_RIGHT_1_IMG = pygame.image.load(PICTURE_PATH + "chrisRight1.png")
PLAYER_RIGHT_2_IMG = pygame.image.load(PICTURE_PATH + "chrisRight2.png")
#Attack Pictures
PLAYER_ATTACK_UP_IMG = pygame.image.load(PICTURE_PATH + "chrisAttackUp.png")
PLAYER_ATTACK_DOWN_IMG = pygame.image.load(PICTURE_PATH + "chrisAttackDown.png")
PLAYER_ATTACK_LEFT_IMG = pygame.image.load(PICTURE_PATH + "chrisAttackLeft.png")
PLAYER_ATTACK_RIGHT_IMG = pygame.image.load(PICTURE_PATH + "chrisAttackRight.png")

# A Dicionary for the player sprites. This is a Dictionay of actions with a Dictionary of directions with a list of sprites
# The Dictionaries keys are walk, and attack: the corresponding values are dictionaries with a list of sprites inside
PLAYER_ANIMATION_DICTIONARY = {'walk': {'U': [PLAYER_UP_1_IMG, PLAYER_UP_2_IMG], 'D': [PLAYER_DOWN_1_IMG, PLAYER_DOWN_2_IMG], 'L': [PLAYER_LEFT_1_IMG, PLAYER_LEFT_2_IMG], 'R': [PLAYER_RIGHT_1_IMG, PLAYER_RIGHT_2_IMG]},
                    'attack': {'U': [PLAYER_ATTACK_UP_IMG], 'D': [PLAYER_ATTACK_DOWN_IMG], 'L': [PLAYER_ATTACK_LEFT_IMG], 'R': [PLAYER_ATTACK_RIGHT_IMG]}}

# Player
# The player controlled by the user
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.direction = 'U'
        self.state = 'walk'
        self.alive = True
        self.lives = 3
        self.invincibleTime = 0
        self.animation_list = PLAYER_ANIMATION_DICTIONARY
        self.image_list = self.animation_list[self.state][self.direction]
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (15 * TILE_SIZE, 15 * TILE_SIZE)
        self.timer = 0.0
        self.pos = pygame.math.Vector2(15 * TILE_SIZE, 15 * TILE_SIZE)
        self.vel = pygame.math.Vector2(0, 0)


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
        if (keys[pygame.K_SPACE]):
            if (self.state != "attack"): # Only create 1 sword at a time
                Sword(self.game, self.pos.x, self.pos.y, self.direction)
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
        else:
            self.state = "rest" 

        if (self.isPlayerInvincible()):
            # *TO DO: Add a different Colour sprite for invincibility
            pass

    # checkPlayerCollisions
    # Check what the player is colliding with
    def checkPlayerCollisions(self):
    
        enemyCollision = pygame.sprite.spritecollideany(self, self.game.enemies)

        if (enemyCollision != None):
            if (not self.isPlayerInvincible()):
                self.lives -= 1
                if (self.lives <= 0):
                    self.alive = False
                    self.kill()
                    self.game.player.kill()
                    return
                self.invincibleTime = self.game.currentTime + PLAYER_INVINCIBILITY_SECONDS  
                
        if (pygame.sprite.spritecollide(self, self.game.items, True)): # Collect Rupee when you collide with it
            self.game.points += RUPEE_VALUE        


    # update
    # Updates the player: moves the player
    def update(self):
        previousDirection = self.direction
        previousState = self.state
        self.get_keys()
        self.checkPlayerCollisions()
        if (self.state != 'rest'): #if the player moved
            self.pos.x += self.vel[0] * self.game.dt
            self.pos.y += self.vel[1] * self.game.dt
            self.rect.topleft = (self.pos.x, self.pos.y)
            if ((self.game.counter % 10 == 0) or (previousDirection != self.direction) or (self.state != previousState)): # alternate every 10 frames or if the direction or state changes
                self.image_list = self.animation_list[self.state][self.direction]
                self.image = self.animation()
            if pygame.sprite.spritecollideany(self, self.game.obstacles):
                self.pos.x -= self.vel[0] * self.game.dt
                self.pos.y -= self.vel[1] * self.game.dt
                self.rect.topleft = (self.pos.x, self.pos.y)

        elif (previousState == "attack"): # After attacking switch back to a standard image
            self.image_list = self.animation_list["walk"][self.direction]
            self.image = self.animation()    

    # isPlayerInvincible
    # Check to see if the player is invincinle
    # The player is invincible for 5 seconds after getting hit
    def isPlayerInvincible(self) -> bool:
        return (self.game.currentTime <= self.invincibleTime)

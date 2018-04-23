
import pygame
import random
import math
#vec = pygame.math.Vector2

# Constants
HEIGHT = 500
WIDTH = 500
TITLE = "LOZ"
FPS = 60
FONT_NAME = "arial"

# Define Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 186, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (138, 43, 226)
PINK = (255, 192,203)
DARK_PINK = (255, 0, 255)
GROUND = (255,218,185)

#Moving Pictures
ChrisF1Img= pygame.image.load("Pictures/chris forward 1.png")
ChrisF2Img= pygame.image.load("Pictures/chris forward 2.png")
ChrisB1Img= pygame.image.load("Pictures/chris backwards 1.png")
ChrisB2Img= pygame.image.load("Pictures/chris backwards 2.png")
ChrisL1Img= pygame.image.load("Pictures/chris left 1.png")
ChrisL2Img= pygame.image.load("Pictures/chris left 2.png")
ChrisR1Img= pygame.image.load("Pictures/chris right 1.png") 
ChrisR2Img= pygame.image.load("Pictures/chris right 2.png") 
#Attack Pictures
ChrisAFImg= pygame.image.load("Pictures/chris attack forward.png")
ChrisABImg= pygame.image.load("Pictures/chris attack back.png")
ChrisALImg= pygame.image.load("Pictures/chris attack left.png")
ChrisARImg= pygame.image.load("Pictures/chris attack right.png")

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.direction = 'U'
        self.state = 'walk' 
        self.animation_list = self.create_animation_dict()
        self.image_list = self.animation_list[self.state][self.direction]
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)   
        self.timer = 0.0
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pygame.math.Vector2(0, 0)
        #self.acc = pygame.math.Vector2(0, 0)
        
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
        restU = ChrisB1Img
        restD = ChrisF1Img
        restL = ChrisL1Img
        restR = ChrisR1Img
        attackU = ChrisABImg
        attackD = ChrisAFImg
        attackL = ChrisALImg
        attackR = ChrisARImg         
        
        # Animation Dictionary Dictionary (A Dictionay of actions with a Dictionary of directions to give the proper animation list)
        animation_dict = {'walk': {'U': [walkU1, walkU2], 'D': [walkD1, walkD2], 'L': [walkL1, walkL2], 'R': [walkR1, walkR2]},
                      'rest': {'U': [restU], 'D': [restD], 'L': [restL], 'R': [restR]},
                      'attack': {'U': [attackU], 'D': [attackD], 'L': [attackL], 'R': [attackR]}}
        
        return animation_dict    

    def animation(self):
        if (pygame.time.get_ticks()- self.timer) > 200: # Alternate between sprites in the list
            if self.image_index < (len(self.image_list) - 1):
                self.image_index += 1
            else:
                self.image_index = 0
            self.timer = pygame.time.get_ticks()
        
        if (self.image_index > (len(self.image_list) - 1)): # Sanity Check: since rest and attack contain 1 image in their list
            return self.image_list[0]  
        
        return self.image_list[self.image_index]    
        
    def update(self):
        #nothing
        self.vel.x = 0
        self.vel.y = 0               
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]): # Spacebar = Attack
            self.state = "attack"
        elif (keys[pygame.K_UP]): # Up Arrow Key = Move Up
            self.state = "walk"
            self.direction = 'U'
            self.vel.y = -1
        elif (keys[pygame.K_DOWN]): # Down Arrow Key = Move Down
            self.state = "walk"
            self.direction = 'D'
            self.vel.y = 1            
        elif (keys[pygame.K_LEFT]): # Left Arrow Key = Move Left
            self.state = "walk"
            self.direction = 'L'
            self.vel.x = -1
        elif (keys[pygame.K_RIGHT]): # Right Arrow Key = Move Right
            self.state = "walk"
            self.direction = 'R'
            self.vel.x = 1
        else: # Nothing = Rest
            self.state = "rest"
            
        self.image_list = self.animation_list[self.state][self.direction]

        self.pos += self.vel
        self.rect.midbottom = self.pos
        self.image = self.animation()

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        #Game loop - Events
        for event in pygame.event.get():
            # Check for closing the window
            if (event.type == pygame.QUIT):
                self.playing = False
                self.running = False
                

    def draw(self):
            # Game Loop - Draw
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            # *After drawing everything, flip the display
            pygame.display.flip()

game = Game()
while(game.running):
    game.new()

pygame.quit

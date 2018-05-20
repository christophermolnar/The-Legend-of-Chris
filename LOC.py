
import pygame
import random
import math
import sys
from os import path
from GameSetting import *
#vec = pygame.math.Vector2

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
#Obstacles
BushImg = pygame.image.load(pictures_path + "bush.png")
RupeeImg = pygame.image.load(pictures_path + "rupee.png")

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
        self.rect.topleft = (15 * TILE_SIZE, 15 * TILE_SIZE)  
        self.timer = 0.0
        self.pos = pygame.math.Vector2(15 * TILE_SIZE, 15 * TILE_SIZE)
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
        attackU = ChrisABImg
        attackD = ChrisAFImg
        attackL = ChrisALImg
        attackR = ChrisARImg         
        
        # Animation Dictionary Dictionary (A Dictionay of actions with a Dictionary of directions to give the proper animation list)
        animation_dict = {'walk': {'U': [walkU1, walkU2], 'D': [walkD1, walkD2], 'L': [walkL1, walkL2], 'R': [walkR1, walkR2]},
                      'attack': {'U': [attackU], 'D': [attackD], 'L': [attackL], 'R': [attackR]}}
        
        return animation_dict    

    def animation(self):
        if self.image_index < (len(self.image_list) - 1):
            self.image_index += 1
        else:
            self.image_index = 0
        
        return self.image_list[self.image_index]    
    
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
            if pygame.sprite.spritecollideany(self, self.game.walls):
                self.pos.x -= self.vel[0] * self.game.dt
                self.pos.y -= self.vel[1] * self.game.dt
                self.rect.topleft = (self.pos.x, self.pos.y)  
            collects_rupee =  pygame.sprite.spritecollide(self, self.game.items, True) # Collect Rupee
            if (collects_rupee):
                pass
        elif (previous_state == "attack"): # After attacking switch back to a standard image
            self.image_list = self.animation_list["walk"][self.direction]                   
            self.image = self.animation()            
        

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Bush(Wall):
    
    def __init__(self, game, x, y):
        Wall.__init__(self, game, x, y)
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)        
        self.image = BushImg

class Rupee(Wall):
    
    def __init__(self, game, x, y):
        Wall.__init__(self, game, x, y)
        self.image = RupeeImg
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)

class Map:
    
    def __init__(self, filename):
        self.data = []
        game_folder = path.dirname(__file__)
        file_path = game_folder + filename
        with open(file_path, 'rt') as file:
            for line in file:
                self.data.append(line)

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
        self.map = Map(map_directory + "Map1.txt")
        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.draw_scenery()
        self.run()
        
    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, LIGHT_GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, LIGHT_GREY, (0, y), (WIDTH, y))    
    
    def draw_scenery(self):
        for r in range (0, HEIGHT//TILE_SIZE):
            for c in range (0, WIDTH//TILE_SIZE):
                if (self.map.data[c][r] == 'B'):
                    Bush(self, r, c)
                if (self.map.data[c][r] == 'R'):
                    Rupee(self, r, c)
                    
        

    def run(self):
        self.playing = True
        self.timer = pygame.time.get_ticks()
        self.counter = 0
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.counter += 1
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
            self.screen.fill(GROUND)
            self.draw_grid()
            self.all_sprites.draw(self.screen)
            # *After drawing everything, flip the display
            pygame.display.flip()

game = Game()
while(game.running):
    game.new()

pygame.quit

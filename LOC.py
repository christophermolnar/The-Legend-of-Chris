
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
Ground= (255,218,185)

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        
        self.animation_list = self.create_animation_dict()
        self.image_list = self.animation_list['walkU']
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)   
        self.timer = 0.0
        #self.state_dict = self.create_state_dict()
        #self.state = 'resting'        
        
        #self.image = pygame.Surface((40,40))
        #self.image.fill(PURPLE)
        #self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pygame.math.Vector2(0, 0)
        #self.acc = pygame.math.Vector2(0, 0)
        
    def create_animation_dict(self):
        size = (40,40)
        walkU1 = pygame.Surface(size).convert()
        walkU1.fill(GREEN)
        walkU2 = pygame.Surface(size).convert()
        walkU2.fill(WHITE)          
        walkR1 = pygame.Surface(size).convert()
        walkR1.fill(RED)
        walkR2 = pygame.Surface(size).convert()
        walkR2.fill(BLUE) 
        walkD1 = pygame.Surface(size).convert()
        walkD1.fill(YELLOW)
        walkD2 = pygame.Surface(size).convert()
        walkD2.fill(PURPLE)          
        walkL1 = pygame.Surface(size).convert()
        walkL1.fill(PINK)
        walkL2 = pygame.Surface(size).convert()
        walkL2.fill(ORANGE) 
        rest = pygame.Surface(size).convert()
        rest.fill(Ground)          
        
        animation_dict = {'walkL': [walkL1, walkL2],
                      'walkR': [walkR1, walkR2],
                      'walkU': [walkU1, walkU2],
                      'walkD': [walkD1, walkD2],
                      'rest': [rest, rest]}
        
        return animation_dict    

    def animation(self):
        if (pygame.time.get_ticks()- self.timer) > 200:
            if self.image_index < (len(self.image_list) - 1):
                self.image_index += 1
            else:
                self.image_index = 0
            self.timer = pygame.time.get_ticks()

        return self.image_list[self.image_index]    
        
    def update(self):
        #nothing
        self.vel.x = 0
        self.vel.y = 0               
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            self.vel.x = -1
            self.image_list = self.animation_list['walkL']
        elif (keys[pygame.K_RIGHT]):
            self.vel.x = 1
            self.image_list = self.animation_list['walkR']
        elif (keys[pygame.K_UP]):
            self.vel.y = -1
            self.image_list = self.animation_list['walkU']
        elif (keys[pygame.K_DOWN]):
            self.vel.y = 1
            self.image_list = self.animation_list['walkD']
        else:
            self.image_list = self.animation_list['rest']

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
            #if (event.type == KEYDOWN):
                #if event.key == K_DOWN: #Check to see if down arrow key is pressed
                    #direction = "down"
                #elif event.key == K_RIGHT: #Check to see if right arrow key is pressed
                    #direction = "right"
                #elif event.key == K_LEFT: #Check to see if left arrow key is pressed
                    #direction = "left"
                #elif event.key == K_UP: #Check to see if up arrow key is pressed
                    #direction = "up"   
                #else:
                    #pass #resting
                

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

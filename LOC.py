
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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (138, 43, 226)

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((40,40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pygame.math.Vector2(0, 0)
        #self.acc = pygame.math.Vector2(0, 0)

    def update(self):
        #nothing
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            self.vel.y = 0
            self.vel.x = -1
        if (keys[pygame.K_RIGHT]):
            self.vel.y = 0
            self.vel.x = 1
        if (keys[pygame.K_UP]):
            self.vel.x = 0
            self.vel.y = -1
        if (keys[pygame.K_DOWN]):
            self.vel.x = 0
            self.vel.y = 1
        #else:
            #self.vel.x = 0
            #self.vel.y = 0

        self.pos += self.vel
        self.rect.midbottom = self.pos

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

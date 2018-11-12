import pygame
import random
import math
import sys
import time
from os import path
from GameSetting import *
from Enemies import *
from Obstacle import *
from Item import *
from Map import *
from Player import *
from Scoreboard import *
#vec = pygame.math.Vector2

# Game
class Game:

    # __init__
    # Crete a Game object
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.startTime = time.time()
        self.currentTime = time.time()
        self.gameTime = 0
        self.running = True
        self.fontName = pygame.font.match_font(FONT_NAME)
        self.points = 0


    # new
    # Sets up sprite groups and map at the start of a game
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.items = pygame.sprite.Group()
        self.playerItems = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.map = Map(map_directory + "Map1.txt", self)
        self.scoreboard = Scoreboard(self)

        self.run()


    # end_game
    # Bring up the Game Over screen
    def endGame(self):
        self.screen.fill(BLACK)
        self.map.draw_text("GAME OVER", 22, RED, WIDTH/2, HEIGHT/2)
        pygame.display.flip()
        time.sleep(2)


    # run
    # run the game
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


    # update
    # Update all of the sprites
    def update(self):
        self.currentTime = time.time()
        self.gameTime = int((self.currentTime - self.startTime))
        self.scoreboard.update(0, 0)
        self.all_sprites.update()


    # events
    # Check what events occured in the game
    def events(self):
        #Game loop - Events
        for event in pygame.event.get():
            # Check for closing the window
            if (event.type == pygame.QUIT):
                self.playing = False
                self.running = False
            if (not self.player.alive):
                self.playing = False
                self.running = False


    # draw
    # Draw eveything to the GUI
    def draw(self):
            # Game Loop - Draw
            self.screen.fill(GROUND)
            self.map.draw_grid()
            self.scoreboard.draw(self.gameTime, self.points, self.player.lives)
            self.all_sprites.draw(self.screen)

            # *After drawing everything, flip the display
            pygame.display.flip()


pygame.init()
game = Game()
while(game.running):
    game.new()
    if (not game.player.alive): # If player died run endGame()
        game.endGame()

pygame.quit

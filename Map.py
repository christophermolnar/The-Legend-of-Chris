import pygame
import sys
from os import path
from GameSetting import *
from Enemies import *
from Obstacle import *
from Item import *

# Map
# The map for the player
class Map:

    # __init__
    # Initializes the map
    # Gets the map details from the map.txt file
    # Parameters: The filename for the map
    def __init__(self, filename, game):
        self.data = []
        self.game = game
        gameFolder = path.dirname(__file__)
        filePath = gameFolder + filename
        with open(filePath, 'rt') as file:
            for line in file:
                self.data.append(line)

        self.draw_scenery()
        #self.draw_enemy()
       # self.draw_scoreboard()


    # draw_text
    # Draw a specified message with a certain colout, size and x/y position
    def draw_text(self, message, size, colour, xPosition, yPosition):
        font = pygame.font.SysFont(FONT_NAME, size)
        textSurface = font.render(message, True, colour)
        self.game.screen.blit(textSurface, (xPosition, yPosition))

        # TODO
        # Add centering, left or right justifying the text


    # draw_grid
    # Draws lines on the grid in the TILE_SIZE size
    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.game.screen, LIGHT_GREY, (x, SCORE_BOARD_TILES * TILE_SIZE), (x, HEIGHT))
        for y in range(SCORE_BOARD_TILES * TILE_SIZE, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.game.screen, LIGHT_GREY, (0, y), (WIDTH, y))


    # draw_scenery
    # Places the bushes and rupees on the map
    def draw_scenery(self):
        for r in range (0, (HEIGHT // TILE_SIZE  - SCORE_BOARD_TILES)): # Y-coordinate of the map
            for c in range (0, WIDTH // TILE_SIZE): # X-coordinate of the map
                if (self.data[r][c] == 'B'):
                    Bush(self.game, c, r + SCORE_BOARD_TILES)
                if (self.data[r][c] == 'R'):
                    Rupee(self.game, c, r + SCORE_BOARD_TILES)
                if (self.data[r][c] == 'O'):
                    OrangeOcto(self.game, c, r + SCORE_BOARD_TILES)

    # draw_scoreboard
    # Draws the scoreboard
    def draw_scoreboard(self):
        pygame.draw.rect(self.game.screen, PURPLE, (0, 0, WIDTH, SCORE_BOARD_TILES*TILE_SIZE))
        # MAKE A SCOREBOARD OBJECT STORE SCORE, TIME AND LIVES


    # draw_enemies
    # Places the enemies on the map
    #def draw_enemy(self):
        #OrangeOcto(self.game, 25, 25)

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
                elif (self.data[r][c] == 'R'):
                    Rupee(self.game, c, r + SCORE_BOARD_TILES)
                elif (self.data[r][c] == 'O'): # Big O for octo enemy moving left and right
                    OrangeOcto(self.game, c, r + SCORE_BOARD_TILES, 'R', ENEMY_SPEED_2, 0)
                elif (self.data[r][c] == 'o'): # little o for octo enemy moving up and down
                    OrangeOcto(self.game, c, r + SCORE_BOARD_TILES, 'D', 0, ENEMY_SPEED_2)   
                elif (self.data[r][c] == 'D'): # Big O for dog guard moving left and right
                    DogGuard(self.game, c, r + SCORE_BOARD_TILES, 'R', ENEMY_SPEED_1, 0)
                elif (self.data[r][c] == 'd'): # little o for dog guard moving up and down
                    DogGuard(self.game, c, r + SCORE_BOARD_TILES, 'D', 0, ENEMY_SPEED_1)                  
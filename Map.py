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
        game_folder = path.dirname(__file__)
        file_path = game_folder + filename
        with open(file_path, 'rt') as file:
            for line in file:
                self.data.append(line)
        
        self.draw_scenery()
        self.draw_enemy()  
        
                
    # draw_text
    # Draw a specified message with a certain colout, size and x/y position
    def draw_text(self, message, size, colour, xPosition, yPosition):
        font = pygame.font.SysFont(FONT_NAME, size)
        text_surface = font.render(message, True, colour)
        self.game.screen.blit(text_surface, (xPosition, yPosition))

        # TODO
        # Add centering, left or right justifying the text    
    
    
    # draw_grid
    # Draws lines on the grid in the TILE_SIZE size
    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.game.screen, LIGHT_GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.game.screen, LIGHT_GREY, (0, y), (WIDTH, y))


    # draw_scenery
    # Places the bushes and rupees on the map
    def draw_scenery(self):
        for r in range (0, HEIGHT//TILE_SIZE):
            for c in range (0, WIDTH//TILE_SIZE):
                if (self.data[c][r] == 'B'):
                    Bush(self.game, r, c)
                if (self.data[c][r] == 'R'):
                    Rupee(self.game, r, c)


    # draw_enemies
    # Places the enemies on the map
    def draw_enemy(self):
        OrangeOcto(self.game, 25, 25)   
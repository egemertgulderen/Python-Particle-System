import pygame
import sys


from particles import Particle
from particles import Sand
from particles import Wood
from particles import Water

white = (255, 255, 255)
black = (0, 0, 0)

sand_colors = [
    (240, 230, 140),  # Khaki
    (210, 180, 140),  # Tan
    (194, 178, 128),  # Burlywood
    (222, 184, 135),  # Blanched Almond
    (244, 164, 96),   # Sandy Brown
    (188, 143, 143),  # Rosy Brown
]


wood_colors = [
    (139, 69, 19),      # Saddle Brown
    (205, 133, 63),     # Peru
    (160, 82, 45),      # Sienna
]


water_color = (0, 128, 255) 

import random


class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.cell_size = 5

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.rows , self.cols = self.height // self.cell_size, self.width // self.cell_size


        # Set curcor properties
        self.cursor_radius = 10  # Adjust the radius according to your preference
        self.cursor_color = (255, 255, 255)
        self.cursor_rect = pygame.Rect(0, 0, 2 * self.cursor_radius, 2 * self.cursor_radius)

      
        
      # Set up button properties
        button_width, button_height = 100, 50
        button_x, button_y = self.width - button_width - 10, 10  # Adjusted for top-right corner
        self.sand_button = pygame.Rect(button_x, button_y, button_width, button_height)
        self.wood_button = pygame.Rect(button_x,button_y+55,button_width,button_height)
        self.water_button = pygame.Rect(button_x, button_y+ 110, button_width,button_height)


        pygame.display.set_caption("Pixel Sand")

        # Creating grid with the initial empty Particle Object
        self.grid = [[Particle() for _ in range(self.cols)] for _ in range(self.cols)]
        
    # Function for drawing each pixel according to the color variable
    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell_value = self.grid[i][j].color

                pygame.draw.rect(self.screen, cell_value, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

    def change_pixel(self,mouse_x,mouse_y,particle_type):

        # locating the pixel of clicked place on screen
        x = mouse_x//self.cell_size 
        y = mouse_y//self.cell_size

         # Define the relative positions of neighboring pixels
        positions = [
            (-2, 0), (2, 0), (0, 2), (0, -2),
            (-1, -1), (-1, 1), (1, -1), (1, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (-2, 1), (-1, 2), (1, 2), (2, 1),
            (0, 0)]

        for dx, dy in positions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < self.cols and 0 <= new_y < self.rows:
                current_pixel = self.grid[new_y][new_x]

            if current_pixel.is_empty():
                # Assign a random color from sand_colors or wood_colors list
                    if particle_type == "Sand":
                        temp = random.randrange(0, len(sand_colors))
                        self.grid[new_y][new_x] = Sand(sand_colors[temp])
                    elif particle_type == "Wood":
                        temp = random.randrange(0, len(wood_colors))
                        self.grid[new_y][new_x] = Wood(wood_colors[temp])
                    elif particle_type =="Water":
                        self.grid[new_y][new_x] = Water(water_color)

   
    def update(self):
        for i in range(self.rows-1,-1,-1):
            left_to_right = random.random() < 0.5

            for j in range(self.cols):
                column_offset = j if left_to_right else -j - 1 + self.cols
                if (isinstance(self.grid[i][column_offset], Sand)):
                    self.grid[i][column_offset].sand_behaviour(i,column_offset,self.grid)

                elif (isinstance(self.grid[i][j],Wood)):
                    self.grid[i][j].wood_behaviour(i,j,self.grid)

                elif (isinstance(self.grid[i][j],Water)):
                    self.grid[i][j].water_behaviour(i,j,self.grid)


    def render(self):
        # Main game loop
        particle_type = "Sand"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse click is within the button rectangle
                    if self.sand_button.collidepoint(event.pos):
                        if particle_type != "Sand":
                            particle_type = "Sand"
                    elif self.wood_button.collidepoint(event.pos):
                        if particle_type != "Wood":
                            particle_type = "Wood"
                    elif self.water_button.collidepoint(event.pos):
                        if particle_type != "Water":
                            particle_type = "Water"

            mouse_buttons = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_buttons[0]:
                self.change_pixel(mouse_x,mouse_y,particle_type)

            # Clear the screen
            self.screen.fill(black)

            # Draw the grid
            self.update()
            self.draw_grid()


            # Drawing buttons
            self.draw_buttons()

            
            # Update the display
            pygame.display.flip()

         
            pygame.time.Clock().tick(300)


    def draw_buttons(self):
        # Blit the text surface onto the screen
        pygame.draw.rect(self.screen,white,self.sand_button)
        pygame.draw.rect(self.screen,white,self.wood_button)
        pygame.draw.rect(self.screen,white,self.water_button)

        # Draw text on the button
        font = pygame.font.Font(None, 36)
        text_sand = font.render("Sand", True, black)
        text_rect = text_sand.get_rect(center=self.sand_button.center)
        self.screen.blit(text_sand, text_rect)
        
        wood_text = font.render("Wood", True, black)
        text_rect_1 = wood_text.get_rect(center=self.wood_button.center)
        self.screen.blit(wood_text, text_rect_1)

        water_text = font.render("Water", True, black)
        text_rect_2 = water_text.get_rect(center=self.water_button.center)
        self.screen.blit(water_text, text_rect_2)


if __name__ == '__main__':
    game = Game()
    game.render()



import pygame
import math
import random

class Particle:
    def __init__(self,color = (0,0,0)):
        self.color = color
        self.velocity = 0
        self.mass = 0
        self.accelaration = 0
        self.max_speed = 0

    def set_color(self,color):
        self.color = color

    def is_empty(self):
        return self.color == (0,0,0)
    
    
class Sand(Particle):
    def __init__(self, color=(0, 0, 0)):
        super().__init__(color)

    def sand_behaviour(self, i, j, grid):
        below = i +1
        below_left = j - 1
        below_right = j + 1

        # Swapping the object at the locations
        if grid[below][j].is_empty():
            grid[below][j], grid[i][j] = grid[i][j], grid[below][j]
        elif below_left >= 0 and grid[below][below_left].is_empty():
            grid[below][below_left], grid[i][j] = grid[i][j], grid[below][below_left]
        elif below_right < len(grid[0]) and grid[below][below_right].is_empty():
            grid[below][below_right], grid[i][j] = grid[i][j], grid[below][below_right]

class Wood(Particle):
    def __init__(self, color=(0, 0, 0)):
        super().__init__(color)

    def wood_behaviour(self,i,j,grid):
        pass


class Water(Particle):
    def __init__(self, color=(0, 0, 0)):
        super().__init__(color)
        self.density = 1.0
        self.pressure = 0.0
    
    def water_behaviour(self,i,j,grid):
        below = i +1
        below_left = j - 1
        below_right = j + 1
        left = j-1
        right = j+1

        # Swapping the object at the locations
        if grid[below][j].is_empty():
            grid[below][j], grid[i][j] = grid[i][j], grid[below][j]
        elif below_left >= 0 and grid[below][below_left].is_empty():
            grid[below][below_left], grid[i][j] = grid[i][j], grid[below][below_left]
        elif below_right < len(grid[0]) and grid[below][below_right].is_empty():
            grid[below][below_right], grid[i][j] = grid[i][j], grid[below][below_right]
        elif left >=0 and grid[i][left].is_empty():
            grid[i][left], grid[i][j] = grid[i][j], grid[i][left]
        elif right < len(grid[0]) and grid[i][right].is_empty():
            grid[i][right], grid[i][j] = grid[i][j], grid[i][right]



class Fire(Particle):
    def __init__(self, color=(0, 0, 0)):
        super().__init__(color)




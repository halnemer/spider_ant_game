import pygame
import random
from constants import *

class Ant:
    COL = [-1, 1, 0, 0]
    ROW = [0, 0, 1, -1]
    def __init__(self, color):
        self.color = color
        self.row = random.randint(0, 15)
        self.col = random.randint(0, 15)
        self.x = 0
        self.y = 0
        self.score = 0

    def checkPosition(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row
    
    def increaseScore(self):
        self.score += 1
    
    def move(self):
        random_move = random.randint(0, 3)
        self.row += self.ROW[random_move]
        self.col += self.COL[random_move]

    def draw(self, surface):
        self.checkPosition()
        pygame.draw.rect(surface, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
    
    def reset(self):
        self.row = random.randint(0, 15)
        self.col = random.randint(0, 15)
        self.x = 0
        self.y = 0
    
    def isOutOfScreen(self, surface):
        return self.row < 0 or self.row > 15 or self.col < 0 or self.col > 15
           
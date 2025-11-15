import pygame
import os

class Turtle_object(pygame.sprite.Sprite):
    # Initialize the turtle object

    def __init__(self, x=100, y=100):
        super().__init__()
        self.image = pygame.image.load("Images/Turtle.png")

        # set a rect so Group.draw() can blit this sprite
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.lives = 3
        self.score = 0
    
    def lose_life(self, running):
        # Decrease life count by 1, if lives reach 0, set running to False
        if self.lives > 0:
            self.lives -= 1
        elif self.lives == 0:
            running = False
        return running

    def gain_score(self, points):
        self.score += points
        return self.score
    

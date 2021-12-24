import pygame
from UIObject import UIObject
import random 

class SnowFlake(UIObject):
    def __init__(self, UI, size):
        ## draw a snowflake using lines and recs
        super().__init__(UI)
        self.location = [random.randrange(0, UI.width), 0]
        self.size = size
        self.surface = pygame.Surface((size,size))
        self.removeSurface = pygame.Surface((size,size))
        self.surface.fill((255,255,255))
        self.removeSurface.fill(UI.CHRISTMAS_RED)

    def timeStep(self):
        self.UI.screen.blit(self.removeSurface, self.location)
        self.location[1] += 1
        ## make the snowflakes float from left to right 
        if self.age > self.UI.height + self.size:
            self.remove()
        return super().timeStep()

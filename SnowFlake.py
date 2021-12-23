import pygame

class SnowFlake(object):

    def __init__(self, size):
        ## draw a snowflake using lines and recs
        self.age = 0

    def print(self, pos, screen):
        """prints the snowflake on the screen"""
        pass
    
    def timeStep(self):
        self.age += 1
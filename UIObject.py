import pygame 

class UIObject(object):
    def __init__(self, UI):
        self.age = 0
        self.UI = UI
        self.surface = None
        self.location = [0,0]

    def timeStep(self):
        self.age += 1

    def animate(self):
        pass
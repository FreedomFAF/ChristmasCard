import pygame 

class Text(object):
    def __init__(self, UI, message):
        self.UI = UI
        self.surface = UI.myfont.render(message,False, (255,255,255))
        self.age = 0
        self.location = [(UI.width - self.surface.get_width())/2, (UI.height - self.surface.get_height())/2]

    def animate(self):
        pass 

    def timeStep(self):
        self.age += 1
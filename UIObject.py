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

    def remove(self):
        removeSurface = pygame.Surface((self.surface.get_width(), self.surface.get_height()))
        removeSurface.fill((214,0,28))
        self.UI.screen.blit(removeSurface, self.location)
        self.UI.gameObjects = {key:val for key, val in self.UI.gameObjects.items() if val != self}
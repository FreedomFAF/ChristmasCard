import pygame 
from UIObject import UIObject

class Text(UIObject):
    line = 0
    def __init__(self, UI, message):
        Text.line += 1
        super().__init__(UI)
        self.surface = UI.myfont.render(message,False, (255,255,255))
        self.location = [(UI.width - self.surface.get_width())/8, Text.line*(UI.height - self.surface.get_height())/4]
import pygame 
from UIObject import UIObject

class Text(UIObject):
    line = 0
    def __init__(self, UI, message):
        Text.line += 1
        super().__init__(UI)
        self.surface = UI.myfont.render(message,False, (255,255,255))
        self.location = [UI.width/10, (Text.line)*(UI.height - self.surface.get_height())/5]
        self.message = message
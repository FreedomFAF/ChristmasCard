import pygame, sys
from Text import Text
from SnowFlake import SnowFlake
from pygame.locals import *

class cardUI(object):
    LEFT = 1
    RIGHT = 2
    def __init__(self):
        pygame.init()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)
        #self.music =
        ## TODO record some christmas music using my guitar computer and pod HD 500
        infoObject = pygame.display.Info()
        self.size = self.width, self.height = infoObject.current_w, infoObject.current_h
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.gameObjects = {}

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Tahoma', 20)

    def mainLoop(self):
        Game = True
        while Game:
            self.clock.tick(60)
            # Quit game
            for event in pygame.event.get():  # game code that happens when any button is pressed
                if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT:
                    if 'merryChristmas' not in self.gameObjects:
                        self.gameObjects['merryChristmas'] = Text(self, 'Merry Christmas')
                    else: 
                        self.closeCard()
                elif event.type == MOUSEBUTTONDOWN and event.button == self.RIGHT:
                    pass
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.closeCard()
                    
            
            self.everyFrame()

            pygame.display.update()

    def everyFrame(self):
        for k, v in self.gameObjects.items():
            v.timeStep()
            self.screen.blit(v.surface, v.location)

    def closeCard(self):
        pygame.display.quit()
        sys.exit() 

if __name__ == '__main__':
    card = cardUI()
    card.mainLoop()
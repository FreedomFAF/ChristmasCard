import pygame, sys
from pygame.locals import *

class cardUI():
    def __init__(self):
        pygame.init()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)
        #self.music =
        ## TODO record some christmas music using my guitar computer and pod HD 500
        infoObject = pygame.display.Info()
        self.size = width, height = infoObject.current_w, infoObject.current_h
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Tahoma Bold', 20)

    def mainLoop(self):
        Game = True
        while Game:
            self.clock.tick(60)
            # Quit game
            for event in pygame.event.get():  # game code that happens when any button is pressed
                if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT:
                    pass
                elif event.type == MOUSEBUTTONDOWN and event.button == self.RIGHT:
                    pass
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()  # closes the game in an event loop

            pygame.display.update()

    def everyFrame(self):
        pass


if __name__ == '__main__':
    card = cardUI()
    card.mainLoop()
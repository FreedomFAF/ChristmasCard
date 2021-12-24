import pygame
from UIObject import UIObject

class SnowFlake(UIObject):

    def __init__(self, UI, size):
        ## draw a snowflake using lines and recs
        super().__init__(UI)
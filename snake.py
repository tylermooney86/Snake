# Snake Clone

import random, pygame, sys
from pygame.locals import *

### Set up window size ###
FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE==0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE==0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = INT(WINDOWHEIGHT/CELLSIZE)

#        R   G   B
WHITE = (255,255,255)
BLACK = (0,0,0)
RED  = (255,0,0)
GREEN = (0,255,0)
DARKGREEN = (0,155,0)
DARKGRAY = (40,40,40)
BGCOLOR = BLACK

#Controls
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD=0

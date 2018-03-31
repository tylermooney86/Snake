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

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_caption('Snake')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    #set random start point
    startx = random.randint(5,CELLWIDTH-6)
    starty = random.randint(5,CELLHEIGHT-6)
    wormCoords = [('x': startx, 'y': starty),
    ('x': startx-1, 'y': starty),
    ('x': startx-2, 'y': starty)]
    direction = RIGHT

    #start the apple in a random place
    apple = getRandomLocation()

    ### Main Game Loop ###
    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if(event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif(event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif(event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif(event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        #check if snake has hit itself or edge of screen
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return #game over

        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return #game over

        #check if snake has eaten apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            #dont remove tail segment
            apple = getRandomLocation()
        else:#remove tail segment
            del wormCoords[-1]

        #move the snake by adding a segment in direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y']-1}
        if direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y']+1}
        if direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x']-1, 'y': wormCoords[HEAD]['y']}
        if direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x']+1, 'y': wormCoords[HEAD]['y']}
        #insert new head
        wormCoords.insert(0, newHead)

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawSnake(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords)-3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.RENDER('Press a key to play.', True, DARKGRAY)
    perssKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():
    pass

def terminate():
    pygame.quit()
    sys.exit()

def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y':random.randint(0, CELLHEIGHT - 1)}

def showGameOverScreen():
    pass

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s'%(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, snakeInnerSegmentRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWWIDTH, CELLSIZE)
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))

if __name__ == '__main__':
    main()

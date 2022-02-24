import pygame
from pygame.locals import *
from spider import *
from ant import *
from constants import *
import sys
from queue import PriorityQueue
from math import *

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('New Spider Game')
FPS = 3
click = False
FONT = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()
# global ant, spider
# # spider = Spider(RED)
# # ant = Ant(GREEN)

# reset the queues, stacks and dictionary
def reset():
    global open_, closed, visited, shortestPath, priorityQueue, currentCost, parant, temp
    visited = {}
    closed = {}
    open_ = []
    shortestPath = []
    priorityQueue = PriorityQueue()
    currentCost = {}
    parant = {}
    temp = []

# for button settings
def drawText(text, font, color, surface, y):
    text = font.render(text, 1, color)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, y)
    surface.blit(text, textRect)

# Set Grid the grid 16 X 16 
def setGrid(surface):
    x = 0
    y = 0
    for _ in range(ROWS):
        x = x + SQUARE_SIZE
        y = y + SQUARE_SIZE
        pygame.draw.line(surface, WHITE, (x, 0), (x, WIDTH))
        pygame.draw.line(surface, WHITE, (0, y), (WIDTH, y))

# update the score and the place of the spider and ant
def changeScore(surface, spider, ant):
    surface.fill(BLACK)
    setGrid(surface)
    spider.draw(WIN)
    ant.draw(WIN)
    pygame.display.update()

# check ant is collected or not
def isCollected(spider, ant):
    if spider.row == ant.row and spider.col == ant.col:
        spider.collectAnt(ant, WIN)
        return True

# start screen with meue bar
def menu():
    global click
    buttonWidth = 200
    buttonHeight = 50
    while True:
 
        WIN.fill((0,0,0))
        drawText('Main Menu', FONT, (255, 255, 255), WIN, 50)
 
        mx, my = pygame.mouse.get_pos() 
        
 
        buttonPlay = pygame.Rect((WIDTH - buttonWidth) // 2, 100, buttonWidth, buttonHeight)
        buttonBfs = pygame.Rect((WIDTH - buttonWidth) // 2, 175, buttonWidth, buttonHeight)
        buttonDfs = pygame.Rect((WIDTH - buttonWidth) // 2, 250, buttonWidth, buttonHeight)
        buttonAStar = pygame.Rect((WIDTH - buttonWidth) // 2, 325, buttonWidth, buttonHeight)
        buttonExit = pygame.Rect((WIDTH - buttonWidth) // 2, 400, buttonWidth, buttonHeight)

        pygame.draw.rect(WIN, (100, 100, 100), buttonPlay)
        pygame.draw.rect(WIN, (100, 100, 100), buttonBfs)
        pygame.draw.rect(WIN, (100, 100, 100), buttonDfs)
        pygame.draw.rect(WIN, (100, 100, 100), buttonAStar)
        pygame.draw.rect(WIN, (100, 100, 100), buttonExit)

        drawText('Play', FONT, (255, 255, 255), WIN, 100 + buttonHeight // 2)
        drawText('BFS', FONT, (255, 255, 255), WIN, 175 + buttonHeight // 2)
        drawText('DFS', FONT, (255, 255, 255), WIN, 250 + buttonHeight // 2)
        drawText('A*', FONT, (255, 255, 255), WIN, 325 + buttonHeight // 2)
        drawText('EXIT', FONT, (255, 255, 255), WIN, 400 + buttonHeight // 2)

        if buttonPlay.collidepoint((mx, my)):
            if click:
                humanPlayer()
            pygame.draw.rect(WIN, (50, 50, 50), buttonPlay)
            drawText('Play', FONT, (255, 255, 255), WIN, 100 + buttonHeight // 2)

        if buttonBfs.collidepoint((mx, my)):
            if click:
                bfsShortestPath()
            pygame.draw.rect(WIN, (50, 50, 50), buttonBfs)
            drawText('BFS', FONT, (255, 255, 255), WIN, 175 + buttonHeight // 2)

        if buttonDfs.collidepoint((mx, my)):
            if click:
                dfsShortestPath()
            pygame.draw.rect(WIN, (50, 50, 50), buttonDfs)
            drawText('DFS', FONT, (255, 255, 255), WIN, 250 + buttonHeight // 2)

        if buttonAStar.collidepoint((mx, my)):
            if click:
                AStarMove()
            pygame.draw.rect(WIN, (50, 50, 50), buttonAStar)
            drawText('A*', FONT, (255, 255, 255), WIN, 325 + buttonHeight // 2)
            
        if buttonExit.collidepoint((mx, my)):
            if click:
                humanPlayer()
            pygame.draw.rect(WIN, (50, 50, 50), buttonExit)
            drawText('EXIT', FONT, (255, 255, 255), WIN, 400 + buttonHeight // 2)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()

# play using keyboard
def humanPlayer():
    run = True

    spider = Spider(RED)
    spider.draw(WIN)

    ant = Ant(GREEN)
    ant.draw(WIN)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_UP] and keys[pygame.K_1]:
                spider.move(0)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_UP] and keys[pygame.K_2]:
                spider.move(1)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_UP] and keys[pygame.K_3]:
                spider.move(2)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_UP] and keys[pygame.K_4]:
                spider.move(3)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_DOWN] and keys[pygame.K_1]:
                spider.move(4)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_DOWN] and keys[pygame.K_2]:
                spider.move(5)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_DOWN] and keys[pygame.K_3]:
                spider.move(6)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)

            if keys[pygame.K_DOWN] and keys[pygame.K_4]:
                spider.move(7)
                isCollected(spider, ant)
                ant.move()
                isCollected(spider, ant)
            
        if spider.isOutOfScreen(WIN):
            spider.reset()
            ant.reset()
        
        if ant.isOutOfScreen(WIN):
            ant.reset()

        changeScore(WIN, spider, ant)

    pygame.quit()

# bfs algorithm
def bfsAlgorithm(initState, targetState):
    global open_, visited, parants, ant, spider
    changeScore(WIN, spider, ant)
    clock.tick(FPS)
    
    open_.append(initState)
    while len(open_) > 0:
        currentState = open_.pop(0)
        if(currentState[0] == targetState[0] and currentState[1] == targetState[1]):
            return

        for i in range(8):
            x = currentState[0] + spider.ROW[i]
            y = currentState[1] + spider.COL[i]
            if(x<=15 and x>=0 and y<=15 and y>=0 and not(tuple([x,y]) in visited)):
                open_.append([x, y])
                visited[tuple([x, y])] = currentState
        
    return


def bfsShortestPath():
    global spider, ant, temp, shortestPath
    spider = Spider(RED)
    ant = Ant(GREEN)

    while True:
        spider.draw(WIN)
        ant.draw(WIN)
        reset()

        while not isCollected(spider, ant) :
            ant.move()
            ant.draw(WIN)
            if ant.isOutOfScreen(WIN):
                ant.reset()
                ant.increaseScore()
                reset()
                break

            bfsAlgorithm([spider.row,spider.col], [ant.row,ant.col])
            temp = [ant.row,ant.col]
            
            while(temp != [spider.row,spider.col] and not temp in shortestPath):
                shortestPath.append(temp)
                temp = visited[tuple(temp)]

            nextStep = shortestPath[len(shortestPath)-1]
            for i in range(8):
                if nextStep[0] == (spider.row + spider.ROW[i]) and nextStep[1] == (spider.col + spider.COL[i]):
                    spider.move(i)
                    spider.draw(WIN)
                    break

            reset()
        print("Spider Score:", spider.score, "Ant Score ", ant.score)

# dfs algorithm
def dfsAlgorithm(initState, targetState):
    global open_, visited, closed, ant, spider
    changeScore(WIN, spider, ant)
    clock.tick(FPS)
    
    open_.append(initState)
    while len(open_) > 0:
        currentState = open_[0]
        closed[tuple(open_.pop(0))] = True
        if(currentState[0] == targetState[0] and currentState[1] == targetState[1]):
            return

        count = 0
        for i in range(8):
            x = currentState[0] + spider.ROW[i]
            y = currentState[1] + spider.COL[i]
            if(x<=15 and x>=0 and y<=15 and y>=0 and not(tuple([x,y]) in visited)):
                open_.insert(count,[x, y])
                visited[tuple([x, y])] = currentState
                count = count + 1

    return

def dfsShortestPath():
    global temp, shortestPath, ant, spider
    spider = Spider(RED)
    ant = Ant(GREEN)

    while True:
        spider.draw(WIN)
        ant.draw(WIN)
        reset()

        while not isCollected(spider, ant) :
            ant.move()
            ant.draw(WIN)
            if ant.isOutOfScreen(WIN):
                ant.reset()
                ant.increaseScore()
                reset()
                break
            
            dfsAlgorithm([spider.row,spider.col], [ant.row,ant.col])

            for key in closed.keys():
                closed[key] = visited[key]

            temp = [ant.row,ant.col]
            while(temp != [spider.row,spider.col] and not temp in shortestPath):
                shortestPath.append(temp)
                temp = closed[tuple(temp)]
            
            nextStep = shortestPath[len(shortestPath)-1]
            for i in range(8):
                if nextStep[0] == (spider.row + spider.ROW[i]) and nextStep[1] == (spider.col + spider.COL[i]):
                    spider.move(i)
                    spider.draw(WIN)
                    break
            reset()
        print("Spider Score:", spider.score, ", Ant Score:", ant.score)
 
# the distance between two points A* using h1
def AStarAlgorithm(initState, targetState):
    global parant, priorityQueue, currentCost, ant, spider
    priorityQueue.put(tuple(initState), 0)
    currentCost[tuple(initState)] = 0
    parant[tuple(initState)] = []

    while(not priorityQueue.empty()):
        currentState = list(priorityQueue.queue[0])
        if(currentState[0] == targetState[0] and currentState[1] == targetState[1]):
            return

        for _ in range(8):
            x = currentState[0] + spider.ROW[0]
            y = currentState[1] + spider.COL[1]
            if(x<=15 and x>=0 and y<=15 and y>=0 and not(tuple([x,y]) in currentCost)):
                currentCost[(tuple([x,y]))] = currentCost[tuple(currentState)] + 1
                priorityQueue.put(tuple([x,y]),currentCost[tuple([x,y])] + sqrt(pow(x-ant.row,2) + pow(y-ant.col,2)))
                parant[tuple([x, y])] = currentState


def AStarMove():
    global priorityQueue, shortestPath, parant, ant, spider
    spider = Spider(RED)
    ant = Ant(GREEN)
    changeScore(WIN, spider, ant)
    clock.tick(FPS)
    while True:
        reset()
        while not isCollected(spider, ant) :
            ant.move()
            ant.draw(WIN)
            if ant.isOutOfScreen(WIN):
                ant.reset()
                reset()
                break
            
            AStarAlgorithm([spider.row, spider.col], [ant.row, ant.col])
            temp = [ant.row,ant.col]
            while(temp != [spider.row,spider.col] and not temp in shortestPath):
                shortestPath.append(temp)
                temp = parant[tuple(temp)]
                
            nextStep = priorityQueue.queue[1]
            for i in range(8):
                if nextStep[0] == (spider.row + spider.ROW[i]) and nextStep[1] == (spider.col + spider.COL[i]):
                    spider.move(i)
                    spider.draw(WIN)
                    break
            reset()

menu()

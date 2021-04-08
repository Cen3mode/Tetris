import pygame
from random import randint
from blocks import *
import time

width = 512
height = 512

frameRate = 60

class Tetris:
    def __init__(self):

        self.currentBlock = [3,0,[]]

        self.running = True

        pygame.init()
        pygame.display.set_caption("Tetris")

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.dt = self.clock.tick(frameRate)
        self.rowTimeCntr = 0

        self.blockFallingInterval = 1000

        self.blockGrid = [[0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0]]

    def selectRandomBlock(self):
        self.currentBlock[2] = blockSet[randint(0, len(blockSet)-1)]

    def drawCurrentBlock(self):
        for row in range(len(self.currentBlock[2])):
            for point in range(len(self.currentBlock[2][row])):
                if(self.currentBlock[2][row][point] == 1):
                    pygame.draw.rect(self.screen, 255 ,pygame.Rect(((height/len(self.blockGrid))*5)+(height/len(self.blockGrid))*(point+self.currentBlock[0]), (height/len(self.blockGrid))*(row+self.currentBlock[1]), (height/len(self.blockGrid)), (height/len(self.blockGrid))))

    def moveCurrentBlock(self):
        self.currentBlock[1] += 1

    def pushBlockToMatrix(self):
        for i in range(len(self.currentBlock[2])):
            for j in range(len(self.currentBlock[2][i])):
                self.blockGrid[i][j+self.currentBlock[0]] = self.currentBlock[2][i][j]

    def draw(self):
        self.screen.fill(0)
        for row in range(len(self.blockGrid)):
            for point in range(len(self.blockGrid[row])):
                if(self.blockGrid[row][point] == 1):
                    pygame.draw.rect(self.screen, 255 ,pygame.Rect((height/len(self.blockGrid))*5+(height/len(self.blockGrid))*point, (height/len(self.blockGrid))*row, (height/len(self.blockGrid)), (height/len(self.blockGrid))))
        self.drawCurrentBlock()
        pygame.display.flip()

    def update(self):
        self.rowTimeCntr += self.clock.tick(frameRate)
        if(self.rowTimeCntr > self.blockFallingInterval):
            self.moveCurrentBlock()
            self.rowTimeCntr = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    self.currentBlock[0] -= 1
                if event.key == pygame.K_RIGHT:
                    self.currentBlock[0] += 1

    def run(self):
        self.selectRandomBlock()
        #self.pushBlockToMatrix()
        while self.running:
            self.update()
            self.draw()            

game = Tetris()
game.run()
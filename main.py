import pygame
from random import randint
from blocks import *
import time
from copy import deepcopy

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

        self.blockGrid = [[1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,0,0,1],
                          [1,1,1,1,1,1,1,1,1,1,1,1]]

    def moveDown(self, dropRow) :
        for row in range(dropRow, 1, -1) :
            self.blockGrid[row] = self.blockGrid[row-1]
        self.blockGrid[0] = 1,0,0,0,0,0,0,0,0,0,0,1

    def checkIfRowMade(self) :
        for row in range(len(self.blockGrid)-1) :
            if all(self.blockGrid[row][1:-2]) != 0 :
                self.blockGrid[row][1:-1] = 0,0,0,0,0,0,0,0,0,0
                self.moveDown(row)

    def rotateBlock(self):
        A = deepcopy(self.currentBlock)
        N = len(A[2][0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[2][i][j]
                A[2][i][j] = A[2][N - 1 - j][i]
                A[2][N - 1 - j][i] = A[2][N - 1 - i][N - 1 - j]
                A[2][N - 1 - i][N - 1 - j] = A[2][j][N - 1 - i]
                A[2][j][N - 1 - i] = temp
        if not self.blockIntersects(A) :
            self.currentBlock = A

    def selectRandomBlock(self):
        self.currentBlock[0] = 3
        self.currentBlock[1] = 0
        self.currentBlock[2] = blockSet[randint(0, len(blockSet)-1)]

    def drawCurrentBlock(self):
        for row in range(len(self.currentBlock[2])):
            for point in range(len(self.currentBlock[2][row])):
                if(self.currentBlock[2][row][point] != 0):
                    pygame.draw.rect(self.screen, colorTable[self.currentBlock[2][row][point]] ,pygame.Rect(((height/len(self.blockGrid)-1)*5)+(height/len(self.blockGrid)-1)*(point+self.currentBlock[0]), (height/len(self.blockGrid)-1)*(row+self.currentBlock[1]), (height/len(self.blockGrid)-1), (height/len(self.blockGrid)-1)))

    def blockIntersects(self, block) -> bool :
        for blockRow in range(len(block[2])):
            for blockColumn in range(len(block[2][blockRow])):
                if(block[2][blockRow][blockColumn] != 0):
                    if(self.blockGrid[blockRow+block[1]][blockColumn+block[0]] != 0):
                        return True
        return False

    def checkBlockCollision(self):
        if self.blockIntersects(self.currentBlock) :
            self.currentBlock[1] -= 1
            self.pushBlockToMatrix()
            self.selectRandomBlock()

    def checkBlockCollisionLeft(self):
        for blockRow in range(len(self.currentBlock[2])):
            for blockColumn in range(len(self.currentBlock[2][blockRow])):
                if(self.currentBlock[2][blockRow][blockColumn] != 0):
                    if(self.blockGrid[blockRow+self.currentBlock[1]][blockColumn-1+self.currentBlock[0]] != 0):
                        return False
        return True
    
    def checkBlockCollisionRight(self):
        for blockRow in range(len(self.currentBlock[2])):
            for blockColumn in range(len(self.currentBlock[2][blockRow])):
                if(self.currentBlock[2][blockRow][blockColumn] != 0):
                    if(self.blockGrid[blockRow+self.currentBlock[1]][blockColumn+1+self.currentBlock[0]] != 0):
                        return False
        return True

    def moveCurrentBlock(self):
        self.currentBlock[1] += 1

    def pushBlockToMatrix(self):
        for i in range(len(self.currentBlock[2])):
            for j in range(len(self.currentBlock[2][i])):
                if(self.currentBlock[2][i][j] != 0 ):
                    self.blockGrid[i+self.currentBlock[1]][j+self.currentBlock[0]] = self.currentBlock[2][i][j]

    def draw(self):
        self.screen.fill(0)
        for row in range(len(self.blockGrid)-1):
            for point in range(len(self.blockGrid[row])):
                if(self.blockGrid[row][point] != 0):
                    pygame.draw.rect(self.screen, colorTable[self.blockGrid[row][point]] ,pygame.Rect((height/len(self.blockGrid)-1)*5+(height/len(self.blockGrid)-1)*point, (height/len(self.blockGrid)-1)*row, (height/len(self.blockGrid)-1), (height/len(self.blockGrid)-1)))
        self.drawCurrentBlock()
        pygame.display.flip()

    def update(self):
        self.rowTimeCntr += self.clock.tick(frameRate)
        self.checkBlockCollision()
        self.checkIfRowMade()
        if(self.rowTimeCntr > self.blockFallingInterval):
            self.moveCurrentBlock()
            self.rowTimeCntr = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT and self.checkBlockCollisionLeft():
                    self.currentBlock[0] -= 1
                if event.key == pygame.K_RIGHT and self.checkBlockCollisionRight():
                    self.currentBlock[0] += 1
                if event.key == pygame.K_s :
                    self.blockFallingInterval = 10
                if event.key == pygame.K_a :
                    self.rotateBlock()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s :
                    self.blockFallingInterval = 1000

    def run(self):
        self.selectRandomBlock()
        #self.pushBlockToMatrix()
        while self.running:
            self.update()
            self.draw()            

game = Tetris()
game.run()
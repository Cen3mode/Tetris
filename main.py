import pygame
from pygame.locals import *
from random import randint
from blocks import *
import time, math
from copy import deepcopy

width = 512
height = 512

frameRate = 60

scorePerLine = [40, 100, 300, 1200]

class Tetris:
    def __init__(self):

        self.game_state = 0

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


        self.block_size = (height/len(self.blockGrid)-1)
        self.currentBlock = [3,0,[]]

        self.running = True

        pygame.init()
        pygame.display.set_caption("Tetris")

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.dt = self.clock.tick(frameRate)
        self.rowTimeCntr = 0

        self.level = 0
        self.score = 0

        self.fall = False

        self.linesBroken = 0

        self.blockFallingInterval = fallSpeed[self.level]

    def moveDown(self, dropRow) :
        for row in range(dropRow, 1, -1) :
            self.blockGrid[row] = self.blockGrid[row-1]
        self.blockGrid[0] = [1,0,0,0,0,0,0,0,0,0,0,1]

    def checkIfRowMade(self) :
        rowsCompleted = 0
        for row in range(len(self.blockGrid)-1) :
            if all(self.blockGrid[row][1:-1]) != 0 :
                self.blockGrid[row][1:-1] = [0,0,0,0,0,0,0,0,0,0]
                self.moveDown(row)
                rowsCompleted += 1
                self.linesBroken += 1 
        if rowsCompleted != 0 :
            self.score += scorePerLine[rowsCompleted] * (self.level + 1)

    def checkIfLost(self) :
        for point in self.blockGrid[0][1:-1] :
            if point != 0 :
                self.game_state = 2

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
        block = randint(0, len(blockSet)-1)
        self.currentBlock[0] = 3
        self.currentBlock[1] = 0 + startOffsetTable[block]
        self.currentBlock[2] = blockSet[block]

    def drawCurrentBlock(self):
        for row in range(len(self.currentBlock[2])):
            for point in range(len(self.currentBlock[2][row])):
                if(self.currentBlock[2][row][point] != 0):
                    pygame.draw.rect(self.screen, 
                        colorTable[self.currentBlock[2][row][point]],
                        pygame.Rect((self.block_size*5)+self.block_size*(point+self.currentBlock[0]), 
                        self.block_size*(row+self.currentBlock[1]), 
                        self.block_size, 
                        self.block_size)
                    )

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
        self.screen.blit(self.myfont.render("Score: {}".format(self.score), False, (255, 255, 255)), (0, 0))
        self.screen.blit(self.myfont.render("Level: {}".format(self.level), False, (255, 255, 255)), (0, 20))
        pygame.display.flip()

    def update(self):
        self.rowTimeCntr += self.clock.tick(frameRate)
        self.checkBlockCollision()
        self.checkIfRowMade()
        self.checkIfLost()
        self.level =  int(math.floor(self.linesBroken/10))
        if self.fall :
            self.blockFallingInterval = fallSpeed[self.level]/100
        else :
            self.blockFallingInterval = fallSpeed[self.level]
        if(self.rowTimeCntr > self.blockFallingInterval):
            self.moveCurrentBlock()
            self.rowTimeCntr = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT and self.checkBlockCollisionLeft():
                    self.currentBlock[0] -= 1
                if event.key == pygame.K_RIGHT and self.checkBlockCollisionRight():
                    self.currentBlock[0] += 1
                if event.key == pygame.K_s :
                    self.fall = True
                if event.key == pygame.K_a :
                    self.rotateBlock()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s :
                    self.fall = False

    def game_menu(self) :
        while self.game_state == 0 :
            self.screen.fill(0)
            self.screen.blit(self.myfont.render("Press [S] to start", True, (255, 255, 255)), (width / 2, height / 2))
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_s :
                        self.game_state = 1
            pygame.display.flip()

    def game(self) :
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
        while self.game_state == 1 :
            self.update()
            self.draw() 

    def lost_screen(self) :
        while self.game_state == 2 :
            self.screen.fill(0)
            self.screen.blit(self.myfont.render("You have lost press [S] to return to menu", True, (255, 255, 255)), (width / 2, height / 2))
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_s :
                        self.game_state = 0
            pygame.display.flip()


    def run(self):
        self.selectRandomBlock()
        while self.running:
            self.game_menu()
            self.game()
            self.lost_screen()
                       

game = Tetris()
game.run()
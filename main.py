import pygame
from random import randint
from blocks import *

width = 512
height = 512

class Tetris:
    def __init__(self):

        self.currentBlock = []

        self.running = True

        pygame.init()
        pygame.display.set_caption("Tetris")

        self.screen = pygame.display.set_mode((width, height))

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
        self.currentBlock = blockSet[randint(0, len(blockSet)-1)]

    def spawnBlock(self, block):
        for i in range(len(block)):
            for j in range(len(block[i])):
                self.blockGrid[i][j+3] = block[i][j]

    def draw(self):
        self.screen.fill(0)
        for row in range(len(self.blockGrid)):
            for point in range(len(self.blockGrid[row])):
                if(self.blockGrid[row][point] == 1):
                    pygame.draw.rect(self.screen, 255 ,pygame.Rect(128+(height/len(self.blockGrid))*point, (height/len(self.blockGrid))*row, (height/len(self.blockGrid)), (height/len(self.blockGrid))))
        pygame.display.flip()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN :
                pass

    def run(self):
        self.selectRandomBlock()
        self.spawnBlock(self.currentBlock)
        while self.running:
            self.update()
            self.draw()            

game = Tetris()
game.run()
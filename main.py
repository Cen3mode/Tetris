import pygame

class Tetris:
    def __init__(self):

        self.running = True

        pygame.init()
        pygame.display.set_caption("Tetris")

        self.screen = pygame.display.set_mode((512, 512))

    def draw(self):
        self.screen.fill((255,255,255))
        pygame.display.flip()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.update()
            self.draw()            

game = Tetris()
game.run()
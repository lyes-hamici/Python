import pygame
from Game import Game
import random

class View:
    def __init__(self, controller) -> None:
            # Configuration of the window & the game (maybe put on another config file)
            self.WIDTH = 500
            self.HEIGHT = 500
            self.COLOR = "#C0C0C0"
            self.difficulty = 'easy'
            
            # Initialize the pygame & setup the window
            pygame.init()
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("MineSweeper")
            
            # Initialize the game and the controller
            self.controller = controller
            self.game = Game(self)
            
            
            
    def main_loop(self):
        '''Main loop of the game, where the game is played and the events are handled'''
        while True:
            #event loop -> put on controller
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.game.draw()       
            pygame.display.update()
    
    
        
        
# Debug purposes
if __name__ == "__main__":
    class Controller:
        def __init__(self) -> None:
            self.board = [[0 for _ in range(10)] for _ in range(10)]
    controller = Controller()
    board = controller.board
    board[1][1] = 1
    board[2][2] = 2
    board[3][3] = 3
    board[4][4] = 4
    board[5][5] = 5
    
    board[1][8] = 11
    board[2][8] = 12
    board[3][8] = 13
    board[4][8] = 14
    board[5][8] = 15
    board[6][8] = 16
    board[7][8] = 17
    board[8][8] = 18
    
    for _ in board:
        print(_)
    view = View(controller)
    view.main_loop()
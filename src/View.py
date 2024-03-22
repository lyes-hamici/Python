import pygame
from Game import Game
from Menu import Menu
import time
# from Controller import Controller

class View:
    # Static variables to represent the states of the game (frames)
    START_MENU = 0
    GAME = 1
    END_MENU = 2
    def __init__(self, controller) -> None:
            # Configuration of the window & the game (maybe put on another config file)
            self.WIDTH = 500
            self.HEIGHT = 500
            self.COLOR = "#C0C0C0"
            self.difficulty = None
            self.current_state = View.START_MENU
            self.is_matrix_created = False
            self.is_it_first_click = True
            self.game_state = None
            self.end_click = False
            
            # Initialize the pygame & setup the window
            pygame.init()
            pygame.font.init()
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("MineSweeper")
            
            # Initialize the game and the controller
            self.controller = controller
            self.game = Game(self)
            self.menu = Menu(self)
            
            
            
    def main_loop(self):
        '''Main loop of the game, where the game is played and the events are handled'''
        count = 0
        timer = 0
        while True:
            # Test purposes
            count = self.controller.get_mines_number()
            timer = self.controller.update_timer()
            self.game.flag_count = int(count)
            if len(str(timer)) == 1:
                self.game.timer = '000' + str(timer)
            elif len(str(timer)) == 2:
                self.game.timer = '00' + str(timer)
            elif len(str(timer)) == 3:
                self.game.timer = '0' + str(timer)
            elif len(str(timer)) == 4:
                self.game.timer = str(timer)
            # End of test purposes
            
            # Conditions to change the state of the game
            if self.current_state == View.START_MENU:
                self.handle_start_menu_events()
                self.menu.main_menu()
            elif self.current_state == View.GAME:
                if self.controller.difficulty != None and self.is_matrix_created == False:
                    self.resize_window(self.controller.difficulty)
                    self.is_matrix_created = True
                    self.controller.create_game_board()
                    self.game.board = self.controller.get_apparent_matrix()
               
                self.game.draw()
                self.handle_game_events()
                if self.game_state == True and self.end_click == True:
                    self.menu.win()
                elif self.game_state == False and self.end_click == True:
                    self.menu.loose()
                # self.game.draw()
                # self.handle_game_events()
            
            # Put on screen the drawing     
            pygame.display.update()
    
    def on_click_cell(self, x, y):
        '''Handles the click on a cell'''
        return self.click_attributes(x, y , is_first_click = False)
    
    def handle_game_events(self):
        '''Handles the game events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    is_in_grid = self.is_in_grid(x, y)
                    x = (x - Game.margin[0]) // self.game.TILE_SIZE
                    y = (y - Game.margin[1]) // self.game.TILE_SIZE
                    
                    if event.button == 1 and is_in_grid and self.game_state == None:
                        if self.is_it_first_click == True:
                            self.controller.set_mines()
                            self.controller.set_numbers()
                            self.controller.start_timer()
                            self.is_it_first_click = False
                        # Temporary solution to resolve the inversion of the x and y
                        self.game_state = self.controller.game_logic(y, x)
                        print(" game board ")
                        for i in self.game.board:
                            print(i)
                    elif event.button == 3 and is_in_grid and self.game_state == None:
                        print("right click",x,y)
                        self.controller.on_right_click(y, x)
                    elif event.button == 1 and not self.end_click :
                        self.end_click = True
                self.game.board = self.controller.get_apparent_matrix()
                    
    def handle_start_menu_events(self):
        '''Handles the start menu events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    def handle_end_menu_events(self):
        '''Handles the end menu events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
    def set_current_state(self, state):
        '''Sets the current state of the game'''
        self.current_state = state
    def set_difficulty(self, difficulty):
        '''Sets the difficulty of the game'''
        self.difficulty = difficulty
        self.controller.set_difficulty(difficulty)
    def get_difficulty(self):
        '''Gets the difficulty of the game'''
        return self.menu.get_difficulty()
    
    def is_in_grid(self, x, y):
        if x >= Game.margin[0] and x <= Game.margin[0] + Game.rows * self.game.TILE_SIZE:
            if y >= Game.margin[1] and y <= Game.margin[1] + Game.cols * self.game.TILE_SIZE:
                return True
        return False
    
    def resize_window(self, difficulty):
        '''Resizes the window based on the difficulty'''
        if difficulty == 'easy':
            self.WIDTH = 500
            self.HEIGHT = 500
        elif difficulty == 'medium':
            self.WIDTH = 750
            self.HEIGHT = 750
        elif difficulty == 'hard':
            self.WIDTH = 1000
            self.HEIGHT = 1000
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        
# Debug purposes
if __name__ == "__main__":
    class Controller:
        def __init__(self) -> None:
            self.board = [[0 for _ in range(10)] for _ in range(10)]
        def set_position(self, x, y):
            self.board[y][x] = 1
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
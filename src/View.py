import pygame
from .Game import Game
from .Menu import Menu
import time
from .Win import Win
from .Loose import Loose
from .User_menu import User_menu
from .Choose_difficulty import Choose_difficulty
# from Controller import Controller

class View:
    # Static variables to represent the states of the game (frames)
    START_MENU = 0
    GAME = 1
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
            self.is_resized = False
            
            # Initialize the pygame & setup the window
            pygame.init()
            pygame.font.init()
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("MineSweeper")
            
            # Initialize the game and the controller
            self.controller = controller
            self.game = Game(self)
            self.menu = Menu(self)
            self.win = Win(self)
            self.loose = Loose(self)
            self.user_menu = User_menu(self)
            self.choose_difficulty = Choose_difficulty(self)
            
            
            
    def main_loop(self):
        '''Main loop of the game, where the game is played and the events are handled'''
        count = 0
        timer = 0
        while True:
            # Handling timer and flag count
            self.game.timer = self.controller.update_timer()
            self.game.flag_count = int(self.controller.get_mines_number())
            
            # Conditions to change the state of the game
            if self.current_state == View.START_MENU:
                self.menu.main_menu()

            elif self.current_state == View.GAME:
                if self.controller.difficulty != None and self.is_matrix_created == False:
                    self.resize_window(self.controller.difficulty)
                    self.is_matrix_created = True
                    self.controller.create_game_board()
                    self.game.board = self.controller.get_apparent_matrix()
                if self.game_state == True and self.end_click == True:
                    if not self.is_resized:
                        self.resize_window("oups")
                        self.is_resized = True
                    self.win.win()
                elif self.game_state == False and self.end_click == True:
                    if not self.is_resized:
                        self.resize_window("oups")
                        self.is_resized = True
                    self.loose.loose()
                else:
                    self.game.draw()
                    self.handle_game_events()
            
            # Put on screen the drawing     
            pygame.display.update()
            
    def resize_window(self, difficulty):
            '''Resizes the window based on the difficulty'''
            
            if difficulty == 'easy' or self.current_state == View.START_MENU or (self.game_state == True and self.end_click == True) or (self.game_state == False and self.end_click == True):
                self.WIDTH = 500
                self.HEIGHT = 500
            elif difficulty == 'medium':
                self.WIDTH = 750
                self.HEIGHT = 750
            elif difficulty == 'hard':
                self.WIDTH = 1600
                self.HEIGHT = 750
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
    
    #=================INPUTS=================#
    
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
                    
                    if event.button == 1 and is_in_grid and self.game_state == None: # left click
                        if self.is_it_first_click == True:
                            self.controller.set_mines(x, y)
                            self.controller.set_numbers()
                            self.controller.start_timer()
                            self.is_it_first_click = False
                        # Temporary solution to resolve the inversion of the x and y
                        self.game_state = self.controller.game_logic(y, x)
                    elif event.button == 3 and is_in_grid and self.game_state == None: # right click
                        self.controller.on_right_click(y, x)
                    elif event.button == 1 and not self.end_click : # end click to show lose or win screen
                        self.end_click = True


                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.game.handle_click(event.pos)
                self.game.board = self.controller.get_apparent_matrix()
                    
    #=================SETTERS AND GETTERS=================#
                    
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
    
    #=================VERIFICATION FUNCTIONS=================#
    
    def is_in_grid(self, x, y):
        if x >= Game.margin[0] and x <= Game.margin[0] + Game.cols * self.game.TILE_SIZE:
            if y >= Game.margin[1] and y <= Game.margin[1] + Game.rows * self.game.TILE_SIZE:
                return True
        return False
    
    def resize_window(self, difficulty):
        '''Resizes the window based on the difficulty'''
          
        if difficulty == 'easy' or self.current_state == View.START_MENU or (self.game_state == True and self.end_click == True) or (self.game_state == False and self.end_click == True):
            self.WIDTH = 500
            self.HEIGHT = 500
        elif difficulty == 'medium':
            self.WIDTH = 750
            self.HEIGHT = 750
        elif difficulty == 'hard':
            self.WIDTH = 1300
            self.HEIGHT = 750
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    
import pygame
import time

class Game:
    margin = 10
    def __init__(self, view) -> None:
        self.view = view
        self.window = view.window
        self.controller = view.controller
        self.board = self.controller.get_apparent_matrix()
        self.TILE_SIZE = 30
        
    #Loading assets for the game itself (maybe put on a config file)
        # Tiles assets   
        self.tile_numbers = self.load_tile_numbers()
        self.base_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/base_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.empty_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/empty_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.flag_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/flag_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.clicked_bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/clicked_bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.interrogant_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/interrogant_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        # Timer assets
        self.digital_numbers = self.load_digital_numbers()
        self.digital_hyphen = pygame.transform.scale(pygame.image.load("assets/images/digits/-.png"), (20, 30))
        self.digital_null = pygame.transform.scale(pygame.image.load("assets/images/digits/null.png"), (20, 30))
        
    def draw(self):
        '''Draws the game play interface'''
        self.window.fill(self.view.COLOR)
        # Draw the grid based on the difficulty
        if self.view.difficulty == 'easy':
            self.calculate_margin(10, 10)
            self.draw_grid(10, 10)
            self.draw_timer()
        elif self.view.difficulty == 'medium':
            self.calculate_margin(20, 20)
            self.draw_grid(20, 20)
        elif self.view.difficulty == 'hard':
            self.calculate_margin(30, 40)
            self.draw_grid(30, 40)
            
    def calculate_margin(self,rows, cols):
        '''Sets the margin of the game'''
        grid_width = rows * self.TILE_SIZE
        grid_height = cols * self.TILE_SIZE
        start_x = (self.view.WIDTH - grid_width) // 2
        start_y = (self.view.HEIGHT - grid_height) // 2
        Game.margin = (start_x, start_y)
        
    def draw_grid(self, rows, cols):
        '''Draws the grid based on the rows and cols given as parameters'''
        start_x, start_y = Game.margin
        
        for y in range(0, rows):
            for x in range(0, cols):
                y_increment = y * self.TILE_SIZE
                x_increment = x * self.TILE_SIZE
                #!!!!!CHANGE THE NUMBERS!!!!!
                if self.board[y][x] == 0:
                    self.window.blit(self.base_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 1:
                    self.window.blit(self.empty_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 2:
                    self.window.blit(self.bomb_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 3:
                    self.window.blit(self.flag_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 4:
                    self.window.blit(self.interrogant_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 5:
                    self.window.blit(self.clicked_bomb_tile, (start_x + x_increment, start_y + y_increment))
                
                elif self.board[y][x] == 11:
                    self.window.blit(self.tile_numbers[0], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 12:
                    self.window.blit(self.tile_numbers[1], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 13:
                    self.window.blit(self.tile_numbers[2], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 14:
                    self.window.blit(self.tile_numbers[3], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 15:
                    self.window.blit(self.tile_numbers[4], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 16:
                    self.window.blit(self.tile_numbers[5], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 17:
                    self.window.blit(self.tile_numbers[6], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 18:
                    self.window.blit(self.tile_numbers[7], (start_x + x_increment, start_y + y_increment))
                    
    def draw_timer(self):
        '''Draws the timer on the screen'''
        timer_x = self.view.WIDTH // 2 - 60
        timer_y = Game.margin[1] - 50
        self.window.blit(self.digital_numbers[5], (timer_x, timer_y))
        self.window.blit(self.digital_numbers[0], (timer_x + 20, timer_y))
        self.window.blit(self.digital_numbers[0], (timer_x + 40, timer_y))
        self.window.blit(self.digital_hyphen, (timer_x + 60, timer_y))
        self.window.blit(self.digital_numbers[6], (timer_x + 80, timer_y))
        self.window.blit(self.digital_numbers[0], (timer_x + 100, timer_y))
        self.window.blit(self.digital_numbers[0], (timer_x + 120, timer_y))
        
    def load_tile_numbers(self):
        '''Loads the tile numbers from the assets folder and returns them as a list of images'''
        tile_numbers = []
        for i in range(1,9):
            tile_numbers.append(pygame.transform.scale(pygame.image.load(f"assets/images/cases/{i}.png"), (self.TILE_SIZE, self.TILE_SIZE)))
        return tile_numbers
    
    def load_digital_numbers(self):
        '''Loads the digital numbers from the assets folder and returns them as a list of images'''
        digital_numbers = []
        for i in range(10):
            digital_numbers.append(pygame.transform.scale(pygame.image.load(f"assets/images/digits/{i}.png"), (20, 30)))
        return digital_numbers
           
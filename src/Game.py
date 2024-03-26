import pygame
import time

class Game:
    margin = ()
    rows = 0
    cols = 0
    def __init__(self, view) -> None:
        """Initializes the main game view"""
        self.view = view
        self.window = view.window
        self.board = self.view.controller.get_apparent_matrix()
        self.TILE_SIZE = 25
        
        self.flag_count = 0
        self.timer = '0000'
        
    #Loading assets for the game itself (maybe put on a config file)
        # Tiles assets   
        self.tile_numbers = self.load_tile_numbers()
        self.base_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/base_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.empty_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/empty_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.flag_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/flag_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.clicked_bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/clicked_bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.interrogant_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/interrogant_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.repeat_button = pygame.transform.scale(pygame.image.load("assets/images/button/repeat_button.png"),(self.TILE_SIZE*1.5, self.TILE_SIZE*1.5))
        # Timer assets
        self.digital_numbers = self.load_digital_numbers()
        self.digital_hyphen = pygame.transform.scale(pygame.image.load("assets/images/digits/-.png"), (20, 30))
        self.digital_null = pygame.transform.scale(pygame.image.load("assets/images/digits/null.png"), (20, 30))
        
        
    def draw(self):
        '''Draws the game play interface'''
        self.window.fill(self.view.COLOR)
        rows = len(self.board)
        cols = len(self.board[0])
        # Draw the grid based on the difficulty
        self.calculate_margin(rows,cols)
        self.draw_grid(rows,cols)
        self.draw_timer()
        self.draw_flag_counter(self.flag_count)
        self.draw_reset_button()

    def calculate_margin(self,rows, cols):
        '''Sets the margin of the game'''
        grid_width = cols * self.TILE_SIZE
        grid_height = rows * self.TILE_SIZE
        start_x = (self.view.WIDTH - grid_width) // 2
        start_y = (self.view.HEIGHT - grid_height) // 2
        Game.margin = (start_x, start_y)
        Game.rows = rows
        Game.cols = cols
        
    def draw_grid(self, rows, cols):
        '''Draws the grid based on the rows and cols given as parameters'''
        self.resize_tile()
        
        start_x, start_y = Game.margin
        
        for y in range(0, rows):
            for x in range(0, cols):
                y_increment = y * self.TILE_SIZE
                x_increment = x * self.TILE_SIZE
                #Condition to show the tiles in fonction of the value of the matrix
                if self.board[y][x] == 0:
                    self.window.blit(self.base_tile, (start_x + x_increment, start_y + y_increment))
                    if [y,x] in self.view.controller.get_vis():
                        self.window.blit(self.empty_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == -1:
                    self.window.blit(self.bomb_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 11:
                    self.window.blit(self.flag_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 12:
                    self.window.blit(self.interrogant_tile, (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 13:
                    self.window.blit(self.clicked_bomb_tile, (start_x + x_increment, start_y + y_increment))
                
                elif self.board[y][x] == 1:
                    self.window.blit(self.tile_numbers[0], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 2:
                    self.window.blit(self.tile_numbers[1], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 3:
                    self.window.blit(self.tile_numbers[2], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 4:
                    self.window.blit(self.tile_numbers[3], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 5:
                    self.window.blit(self.tile_numbers[4], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 6:
                    self.window.blit(self.tile_numbers[5], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 7:
                    self.window.blit(self.tile_numbers[6], (start_x + x_increment, start_y + y_increment))
                elif self.board[y][x] == 8:
                    self.window.blit(self.tile_numbers[7], (start_x + x_increment, start_y + y_increment))
                    
    def draw_timer(self):
        '''Draws the timer on the screen'''
        timer = self.timer
        
        if len(str(timer)) == 1:
                timer = '000' + str(timer)
        elif len(str(timer)) == 2:
            timer = '00' + str(timer)
        elif len(str(timer)) == 3:
            timer = '0' + str(timer)
        elif len(str(timer)) == 4:
            timer = str(timer)
            
        parsed_timer = [int(i) for i in str(timer)]
        
        timer_x = self.view.WIDTH // 2 - self.digital_numbers[0].get_width() // 2 * 5
        timer_y = (Game.margin[1] // 2) - self.digital_numbers[0].get_height() // 1.5
        
        self.window.blit(self.digital_numbers[parsed_timer[0]], (timer_x, timer_y))
        self.window.blit(self.digital_numbers[parsed_timer[1]], (timer_x + 22, timer_y))
        self.window.blit(self.digital_hyphen, (timer_x + 47, timer_y))
        self.window.blit(self.digital_numbers[parsed_timer[2]], (timer_x + 72, timer_y))
        self.window.blit(self.digital_numbers[parsed_timer[3]], (timer_x + 94, timer_y))
        
        self.draw_text("Time", timer_x + 40, timer_y + 35, 20)
    
    def draw_flag_counter(self,digit):
        '''Draws the flag counter on the screen'''
        parsed_digit = [int(i) for i in str(digit)]
        flag_counter_x = (self.view.WIDTH - Game.margin[0] ) - self.digital_numbers[0].get_width() * 2
        flag_counter_y = (Game.margin[1] // 2) - self.digital_numbers[0].get_height() // 1.5

        self.window.blit(self.flag_tile, (flag_counter_x + 68, flag_counter_y))        
        self.draw_text("Flags", flag_counter_x + 20, flag_counter_y + 35, 20)
        if len(parsed_digit) == 1:
            self.window.blit(self.digital_numbers[0], (flag_counter_x, flag_counter_y))
            self.window.blit(self.digital_numbers[0], (flag_counter_x + 22, flag_counter_y))
            self.window.blit(self.digital_numbers[parsed_digit[0]], (flag_counter_x + 44, flag_counter_y))
        elif len(parsed_digit) == 2:
            self.window.blit(self.digital_numbers[0], (flag_counter_x, flag_counter_y))
            self.window.blit(self.digital_numbers[parsed_digit[0]], (flag_counter_x + 22, flag_counter_y))
            self.window.blit(self.digital_numbers[parsed_digit[1]], (flag_counter_x + 44, flag_counter_y))
        elif len(parsed_digit) == 3:
            self.window.blit(self.digital_numbers[parsed_digit[0]], (flag_counter_x, flag_counter_y))
            self.window.blit(self.digital_numbers[parsed_digit[1]], (flag_counter_x + 22, flag_counter_y))
            self.window.blit(self.digital_numbers[parsed_digit[2]], (flag_counter_x + 44, flag_counter_y))
        else:
            self.window.blit(self.digital_null, (flag_counter_x, flag_counter_y))
            self.window.blit(self.digital_null, (flag_counter_x + 22, flag_counter_y))
            self.window.blit(self.digital_null, (flag_counter_x + 44, flag_counter_y))
        
    def draw_text(self, text, x, y, size):
        '''Draws text on the screen'''
        font = pygame.font.Font(None, size)
        text = font.render(text, True, (0,0,0))
        self.window.blit(text, (x, y))

    def draw_reset_button(self):
        '''Draws the reset button on the screen'''
        counter_x = Game.margin[0]
        counter_y = (Game.margin[1] // 2) - self.digital_numbers[0].get_height() // 1.5

        self.window.blit(self.repeat_button, (counter_x, counter_y))
        return pygame.Rect(counter_x, counter_y, self.repeat_button.get_width(), self.repeat_button.get_height())

    def handle_click(self, pos):
        button_rect = self.draw_reset_button()
        if button_rect.collidepoint(pos):
            self.view.controller.reset_game()
        
    def resize_tile(self):
        if self.view.difficulty == 'easy':
            self.TILE_SIZE = 35
        elif self.view.difficulty == 'medium':
            self.TILE_SIZE = 30
        elif self.view.difficulty == 'hard':
            self.TILE_SIZE = 25
        self.load_all_assets()
    
    def load_all_assets(self):
        self.tile_numbers = self.load_tile_numbers()
        self.base_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/base_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.empty_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/empty_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.flag_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/flag_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.clicked_bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/clicked_bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.interrogant_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/interrogant_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        
                    

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
           
import pygame

class Game:
    def __init__(self, view) -> None:
        self.view = view
        self.difficulty = view.difficulty
        self.window = view.window
        self.controller = view.controller
        self.board = self.controller.board
        self.TILE_SIZE = 30
        
    #Loading assets for the game itself (maybe put on a config file)
        self.tile_numbers = self.load_tile_numbers()
        self.base_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/base_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.empty_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/empty_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.flag_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/flag_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.clicked_bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/clicked_bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.interrogant_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/interrogant_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
    
    def draw(self):
        '''Draws the game play interface'''
        self.window.fill(self.view.COLOR)
        
        # Draw the grid based on the difficulty
        if self.difficulty == 'easy':
            self.draw_grid(10, 10)
        elif self.difficulty == 'medium':
            self.draw_grid(20, 20)
        elif self.difficulty == 'hard':
            self.draw_grid(30, 40)
    
    def draw_grid(self, rows, cols):
        '''Draws the grid based on the rows and cols given as parameters'''
        grid_width = rows * self.TILE_SIZE
        grid_height = cols * self.TILE_SIZE
        
        start_x = (self.view.WIDTH - grid_width) // 2
        start_y = (self.view.HEIGHT - grid_height) // 2
        
        for y in range(0, grid_width, self.TILE_SIZE):
            for x in range(0, grid_height, self.TILE_SIZE):
                if self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 0:
                    self.window.blit(self.base_tile, (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 1:
                    self.window.blit(self.empty_tile, (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 2:
                    self.window.blit(self.bomb_tile, (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 3:
                    self.window.blit(self.flag_tile, (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 4:
                    self.window.blit(self.interrogant_tile, (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 5:
                    self.window.blit(self.clicked_bomb_tile, (start_x + x, start_y + y))
                
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 11:
                    self.window.blit(self.tile_numbers[0], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 12:
                    self.window.blit(self.tile_numbers[1], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 13:
                    self.window.blit(self.tile_numbers[2], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 14:
                    self.window.blit(self.tile_numbers[3], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 15:
                    self.window.blit(self.tile_numbers[4], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 16:
                    self.window.blit(self.tile_numbers[5], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 17:
                    self.window.blit(self.tile_numbers[6], (start_x + x, start_y + y))
                elif self.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 18:
                    self.window.blit(self.tile_numbers[7], (start_x + x, start_y + y))    
    def load_tile_numbers(self):
        '''Loads the tile numbers from the assets folder and returns them as a list of images'''
        tile_numbers = []
        for i in range(1,9):
            tile_numbers.append(pygame.transform.scale(pygame.image.load(f"assets/images/cases/{i}.png"), (self.TILE_SIZE, self.TILE_SIZE)))
        return tile_numbers
           
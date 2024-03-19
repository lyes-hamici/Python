import pygame
class View:
    def __init__(self, controller) -> None:
            # Configuration of the window & the game (maybe put on another config file)
            self.WIDTH = 500
            self.HEIGHT = 500
            self.COLOR = "#C0C0C0"
            self.TILE_SIZE = 30
            self.difficulty = 'easy'
            
            #Loading assets for the game itself (maybe put on a config file)
            self.tile_numbers = self.load_tile_numbers()
            self.base_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/base_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
            self.empty_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/empty_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
            self.flag_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/flag_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
            self.bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
            self.clicked_bomb_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/clicked_bomb_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
            self.interrogant_tile = pygame.transform.scale(pygame.image.load("assets/images/cases/interrogant_case.png"), (self.TILE_SIZE, self.TILE_SIZE))
            
            # Initialize the pygame & setup the window
            pygame.init()
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("MineSweeper")
            
            self.controller = controller
            
    def main_loop(self):
        '''Main loop of the game, where the game is played and the events are handled'''
        while True:
            #event loop -> put on controller
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.draw_game()        
            pygame.display.update()
    
    def draw_game(self):
        '''Draws the game play interface'''
        self.window.fill(self.COLOR)
        
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
        
        start_x = (self.WIDTH - grid_width) // 2
        start_y = (self.HEIGHT - grid_height) // 2
        
        for y in range(0, grid_width, self.TILE_SIZE):
            for x in range(0, grid_height, self.TILE_SIZE):
                if self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 0:
                    self.window.blit(self.base_tile, (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 1:
                    self.window.blit(self.empty_tile, (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 2:
                    self.window.blit(self.bomb_tile, (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 3:
                    self.window.blit(self.flag_tile, (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 4:
                    self.window.blit(self.interrogant_tile, (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 5:
                    self.window.blit(self.clicked_bomb_tile, (start_x + x, start_y + y))
                
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 11:
                    self.window.blit(self.tile_numbers[0], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 12:
                    self.window.blit(self.tile_numbers[1], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 13:
                    self.window.blit(self.tile_numbers[2], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 14:
                    self.window.blit(self.tile_numbers[3], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 15:
                    self.window.blit(self.tile_numbers[4], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 16:
                    self.window.blit(self.tile_numbers[5], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 17:
                    self.window.blit(self.tile_numbers[6], (start_x + x, start_y + y))
                elif self.controller.board[y//self.TILE_SIZE][x//self.TILE_SIZE] == 18:
                    self.window.blit(self.tile_numbers[7], (start_x + x, start_y + y))    
                
                
    
    def load_tile_numbers(self):
        '''Loads the tile numbers from the assets folder and returns them as a list of images'''
        tile_numbers = []
        for i in range(1,9):
            tile_numbers.append(pygame.transform.scale(pygame.image.load(f"assets/images/cases/{i}.png"), (self.TILE_SIZE, self.TILE_SIZE)))
        return tile_numbers
        
        
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
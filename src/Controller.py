from .Model import Model
from .View import View

class Controller:
    def __init__(self) -> None:
        """
        Initializes the controller - the main class of the game.
        We instantiate the Model and View classes here.
        """
        self.model = Model()
        self.view = View(self)     
        self.difficulty = None
    
    def main(self):
        '''Main function of the controller'''
        self.view.main_loop()
        
    #=================SETTERS AND GETTERS=================#
        #=================GETTERS=================#
    def get_mines_number(self):
        '''Gets the number of mines'''
        return self.model.get_mines_number()

    def get_vis(self):
        """Returns a list of list that represents the tiles that have been visited by the flood fill algorithm"""
        return self.model.vis
    
    def get_apparent_matrix(self):
        return self.model.get_apparent_matrix()
        
        #=================SETTERS=================#
    def set_position(self, x, y):
        '''Sets the position of the controller'''
        self.model.set_position(x, y)
    
    def set_difficulty(self, difficulty):
        self.difficulty=difficulty
    
    def set_numbers(self):
        '''Sets the number of mines'''
        self.model.set_numbers()

    #=================GAME FUNCTIONS=================#

    def create_game_board(self):
        '''Creates the game board based on the difficulty'''
        if self.difficulty == 'easy':
            self.model.create_matrix(10,10)
        elif self.difficulty == 'medium':
            self.model.create_matrix(20,20)
        elif self.difficulty == 'hard':
            self.model.create_matrix(50, 20)

    def game_logic(self, x, y):
        '''Handles the game logic'''
        return self.model.game_logic(x, y)

    def set_mines(self, x, y):
        '''Sets the mines'''
        if self.difficulty == 'easy':
            self.model.set_mines_number(10)
        elif self.difficulty == 'medium':
            self.model.set_mines_number(40)
        elif self.difficulty == 'hard':
            self.model.set_mines_number(99)
        self.model.set_mines(x, y)
    
    def on_right_click(self, x, y):
        '''Handles the right click'''
        return self.model.action_right_click(x, y)
    
    def reset_game(self):
        '''Resets the game'''
        # self.model.reset_game()
        self.model = Model()
        self.view = View(self)
        controller.main()
    
        #=================TIMER=================#
    def start_timer(self):
        '''Starts the timer'''
        if self.view.is_it_first_click:
            return self.model.start_timer()
        else:
            pass
    
    def update_timer(self):
        '''Updates the timer'''
        return self.model.update_timer()
    
    def reset_game(self):
        '''Resets the game'''
        # self.model.reset_game()
        self.model = Model()
        self.view = View(self)
        controller = Controller()
        controller.main()
    
                
if __name__ == "__main__":
    controller = Controller()
    controller.main()
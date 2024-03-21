from Model import Model
from View import View

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)     
        self.difficulty = None  

    def get_vis(self):
        return self.model.vis
        
    def set_position(self, x, y):
        '''Sets the position of the controller'''
        self.model.set_position(x, y)


    def main(self):
        '''Main function of the controller'''
        self.view.main_loop()

    def get_apparent_matrix(self):
        return self.model.get_apparent_matrix()
    
    def set_difficulty(self, difficulty):
        self.difficulty=difficulty

    def create_game_board(self):
        '''Creates the game board based on the difficulty'''
        if self.difficulty == 'easy':
            self.model.create_matrix(10)
        elif self.difficulty == 'medium':
            self.model.create_matrix(20)
        elif self.difficulty == 'hard':
            self.model.create_matrix(30)

    def game_logic(self, x, y):
        '''Handles the game logic'''
        return self.model.game_logic(x, y)
    
    def show_cases(self, x, y):
        '''Shows the cases'''
        return self.model.show_cases(x, y)

    def set_numbers(self):
        '''Sets the number of mines'''
        self.model.set_numbers()
    
    def set_mines(self):
        '''Sets the mines'''
        if self.difficulty == 'easy':
            self.model.set_mines_number(10)
        elif self.difficulty == 'medium':
            self.model.set_mines_number(40)
        elif self.difficulty == 'hard':
            self.model.set_mines_number(99)
        self.model.set_mines()

    def check_win(self):
        '''Checks if the player has won'''
        return self.model.check_win()
    
    def on_right_click(self, x, y):
        '''Handles the right click'''
        return self.model.action_right_click(x, y)
    
    def reset_game(self):
        '''Resets the game'''
        pass
        
if __name__ == "__main__":
    controller = Controller()
    controller.main()
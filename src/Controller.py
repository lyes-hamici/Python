from Model import Model
from View import View

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)       
        
    def set_position(self, x, y):
        '''Sets the position of the controller'''
        self.model.set_position(x, y)


    def main(self):
        '''Main function of the controller'''
        self.view.main_loop()

    def get_apparent_matrix(self):
        return self.model.get_apparent_matrix()

if __name__ == "__main__":
    controller = Controller()
    controller.main()
from Model import Model
from View import View

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)       
        
    def set_position(self, x, y):
        '''Sets the position of the controller'''
        self.model.set_position(x, y)
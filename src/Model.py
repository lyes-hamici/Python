from random import randint

class Model:
    def __init__(self) -> None:
        self.matrix_variable = []
        self.apparent_matrix = []
        self.mines_number = 0
        self.matrix_size = 0
        self.flagged_positions = ()
        self.interrogation_positions = ()
        self.clicked_positions = ()
        self.vis = []

    #=================SETTERS AND GETTERS=================#
        #=================SETTERS=================#
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_mines_number(self, mines_number):
        self.mines_number = mines_number
    
    def set_matrix_size(self, matrix_size):
        self.matrix_size = matrix_size

    def set_matrix_variable(self, matrix_variable):
        self.matrix_variable = matrix_variable

    def set_apparent_matrix(self, apparent_matrix):
        self.apparent_matrix = apparent_matrix

    def set_flagged_positions(self, flagged_positions):
        self.flagged_positions = flagged_positions
    
    def set_interrogation_positions(self, interrogation_positions):
        self.interrogation_positions = interrogation_positions
    
    def set_clicked_positions(self, clicked_positions):
        self.clicked_positions = clicked_positions

    #=================SETTERS AND GETTERS=================#
        #=================GETTERS=================#

    def get_mines_number(self):
        return self.mines_number
    
    def get_matrix_size(self):
        return self.matrix_size
    
    def get_matrix_variable(self):
        return self.matrix_variable
    
    def get_apparent_matrix(self):
        return self.apparent_matrix
    
    def get_flagged_positions(self):
        return self.flagged_positions
    
    def get_interrogation_positions(self):
        return self.interrogation_positions
    
    def get_clicked_positions(self):
        return self.clicked_positions
    
    def get_vis(self):
        return self.vis
    
    #=================CREATING GAME OBJECTS=================#

    def create_matrix(self, matrix_size):
        self.matrix_size = matrix_size
        self.matrix_variable = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
        self.apparent_matrix = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    #create the matrix with the size of the game


    def set_mines(self):
        mines = 0
        while mines < self.mines_number:
            x = randint(0, self.matrix_size - 1)
            y = randint(0, self.matrix_size - 1)
            if self.matrix_variable[x][y] != -1:
                self.matrix_variable[x][y] = -1
                mines += 1
    #set the mines in the matrix

    def set_numbers(self):
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.matrix_variable[i][j] != -1:
                    self.matrix_variable[i][j] = self.count_mines(i, j)
    #set the number of mines around a cell
                       
    def count_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i >= 0 and x + i < self.matrix_size and y + j >= 0 and y + j < self.matrix_size:
                    if self.matrix_variable[x + i][y + j] == -1:
                        count += 1
        return count
    #count the number of mines around a cell for the set_numbers function

    #=================GAME LOGIC=================#

    def game_logic(self, x, y):
        if self.check_lose():
            print ("game over")
            return "Game Over", False
        elif self.matrix_variable[x][y] == 0 or self.matrix_variable[x][y] == -1:
            self.show_cases(x, y)
        else:
            self.apparent_matrix[x][y] = self.matrix_variable[x][y]
            if [x,y] not in self.vis:
                self.vis.append([x,y])
            if self.check_win():
                self.show_mines()
                print ("you win")
                return "You win", True
            return "Continue", None
        
    def check_win(self):
        if len(self.vis) == self.matrix_size * self.matrix_size - self.mines_number:
            return True
        else:
            return False
        
    def check_lose(self):
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.apparent_matrix[i][j] == 13:
                    return True
        return False

        
    #=================DISPLAY CASES=================#
        
    def show_cases(self, x, y):
        if self.matrix_variable[x][y] == -1:
            self.apparent_matrix[x][y] = 13
            self.vis.append([x,y])
            self.show_mines()
            self.game_status = "Game Over"
        #if the case is a mine, the game is over and the mines are shown
        elif self.matrix_variable[x][y] == 0:
            print ("apparent matrix")
            for i in self.apparent_matrix:
                print(i)
            print ("matrix variable")
            for i in self.matrix_variable:
                print(i)
            self.show_neighbours(x, y)
            print ("apparent matrix after show_neighbours")
            for i in self.apparent_matrix:
                print(i)
        #if the case is empty, the empty cases are shown
        

    def show_mines(self):
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.matrix_variable[i][j] == -1 and not [i,j] in self.vis:
                    self.apparent_matrix[i][j] = -1
    #show the mines when the game is over

    def show_neighbours(self, x, y):
        if [x,y] not in self.vis:

            self.vis.append([x,y])
            if self.matrix_variable[x][y] == 0:
                self.apparent_matrix[x][y] = self.matrix_variable[x][y]
                #show the empty case as empty case
                if x > 0:
                    self.show_neighbours(x-1, y)
                if x < self.matrix_size - 1:
                    self.show_neighbours(x+1, y)
                if y > 0:
                    self.show_neighbours(x, y-1)
                if y < self.matrix_size - 1:
                    self.show_neighbours(x, y+1)
                if x > 0 and y > 0:
                    self.show_neighbours(x-1, y-1)
                if x > 0 and y < self.matrix_size - 1:
                    self.show_neighbours(x-1, y+1)
                if x < self.matrix_size - 1 and y > 0:
                    self.show_neighbours(x+1, y-1)
                if x < self.matrix_size - 1 and y < self.matrix_size - 1:
                    self.show_neighbours(x+1, y+1)
                #show the neighbours of an empty case
            if self.matrix_variable[x][y] != 0 and self.matrix_variable[x][y] != -1:
                self.apparent_matrix[x][y] = self.matrix_variable[x][y]
            #show the number of mines around a case    

    #=================FLAG AND QUESTION MARKS=================#
    def action_right_click(self, x, y):
        if self.apparent_matrix[x][y] == 0 and [x,y] not in self.vis:
            self.apparent_matrix[x][y] = 11
        elif self.apparent_matrix[x][y] == 11:
            self.apparent_matrix[x][y] = 12
        elif self.apparent_matrix[x][y] == 12:
            self.apparent_matrix[x][y] = 0     

    
#==================================================================================================#
        #=================TESTING=================#

if __name__ == "__main__":
    model = Model()
    model.set_mines_number(10)
    model.create_matrix(10)
    model.set_mines()
    model.set_numbers()
    print ("matrix values")
    for i in model.get_matrix_variable():
        print(i)
    print ("apparent matrix")
    for i in model.get_apparent_matrix():
        print(i)

    print(model.game_logic(0, 0))
    model.show_cases(0, 0)
    print ("apparent matrix")
    for i in model.get_apparent_matrix():
        print(i)
    print(model.vis)


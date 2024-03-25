import pygame
from .Button import Button
import sys
from pygame import *
from pygame.locals import *

class Choose_difficulty:
    def __init__(self, view):
        """Initializes the class were the user can choose the difficulty of the game"""
        self.view = view
        pygame.init()
        self.WIDTH = 500
        self.HEIGHT = 500
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.police = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 30)
        self.police_small = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 25)
        self.police_big = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 50)

        self.size = (500,500)
        self.size_button = (150,100)

        self.BG = pygame.image.load("assets\\images\\background\\BG_Logo.jpg")
        self.BG = pygame.transform.scale(self.BG, self.size)

        self.play_button = pygame.image.load("assets\\images\\button\\Play Rect.png")
        self.play_button = pygame.transform.scale(self.play_button, self.size_button)

        self.quit_button = pygame.image.load("assets\\images\\button\\Quit Rect.png")
        self.quit_button = pygame.transform.scale(self.quit_button, self.size_button)

        self.choose_difficulty_running = False



    def get_font(self,size): 
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)

    def choose_game_difficulty(self):
        """Draws the screen where the user can choose the difficulty of the game"""
        difficulty = self.police_big.render(f"Choose a difficulty",True,"white")
        self.current_run = True
        self.SCREEN.blit(self.BG, (0, 0))
        self.SCREEN.blit(difficulty, (100, 50))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        
        EASY_BUTTON = Button(image=self.play_button, pos=(250, 180), 
                            text_input="Easy", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        MEDIUM_BUTTON = Button(image=self.quit_button, pos=(250, 300), 
                            text_input="Medium", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        HARD_BUTTON = Button(image=self.quit_button, pos=(250, 420), 
                            text_input="Hard", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")


        for button in [EASY_BUTTON,MEDIUM_BUTTON,HARD_BUTTON]:

            button.changeColor(MENU_MOUSE_POS)

            button.update(self.SCREEN)

        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.view.set_current_state(self.view.GAME)
                    self.current_run = False
                    self.difficulty = "easy"
                    self.view.set_difficulty(self.difficulty)
                    self.stop_running_choose_difficulty_menu()
                    

                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.view.set_current_state(self.view.GAME)
                    self.current_run = False
                    self.difficulty = "medium"
                    self.view.set_difficulty(self.difficulty)
                    self.stop_running_choose_difficulty_menu()
                    

                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.view.set_current_state(self.view.GAME)
                    self.current_run = False
                    self.difficulty = "hard"
                    self.view.set_difficulty(self.difficulty)
                    self.stop_running_choose_difficulty_menu()
                    
                        
        pygame.display.update()


    def get_difficulty(self):
        return self.difficulty

    def stop_running_choose_difficulty_menu(self):
        self.choose_difficulty_running = False

    def running_choose_difficulty_menu(self):
        self.choose_difficulty_running = True

    def get_running_choose_difficulty_menu(self):
        return self.choose_difficulty_running
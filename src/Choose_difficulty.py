import pygame
from .Button import Button
import sys
from pygame import *
from pygame.locals import *

class Choose_difficulty:
    def __init__(self, view):
        """Initializes the class where the user can choose the difficulty of the game"""
        self.view = view
        pygame.init()  # Initialize pygame
        self.WIDTH = 500
        self.HEIGHT = 500
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # Create a display surface
        self.police = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 30)  # Load font
        self.police_small = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 25)
        self.police_big = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 50)

        self.size = (500, 500)  # Size of the screen
        self.size_button = (150, 100)  # Size of buttons

        # Load background and buttons images
        self.BG = pygame.image.load("assets\\images\\background\\BG_Logo.jpg")
        self.BG = pygame.transform.scale(self.BG, self.size)

        self.play_button = pygame.image.load("assets\\images\\button\\Play Rect.png")
        self.play_button = pygame.transform.scale(self.play_button, self.size_button)

        self.quit_button = pygame.image.load("assets\\images\\button\\Quit Rect.png")
        self.quit_button = pygame.transform.scale(self.quit_button, self.size_button)

        self.choose_difficulty_running = False  # Flag to control whether the choose difficulty menu is running
        self.difficulty = ""  # Store the chosen difficulty

    def get_font(self,size): 
        # Helper function to get font with given size
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)

    def choose_game_difficulty(self):
        """Draws the screen where the user can choose the difficulty of the game"""
        difficulty = self.police_big.render(f"Choose a difficulty", True, "white")  # Render difficulty message
        self.current_run = True
        self.SCREEN.blit(self.BG, (0, 0))  # Draw background image
        self.SCREEN.blit(difficulty, (100, 50))  # Draw difficulty message
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position

        # Create buttons for each difficulty level
        EASY_BUTTON = Button(image=self.play_button, pos=(250, 180), 
                            text_input="Easy", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        MEDIUM_BUTTON = Button(image=self.quit_button, pos=(250, 300), 
                            text_input="Medium", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        HARD_BUTTON = Button(image=self.quit_button, pos=(250, 420), 
                            text_input="Hard", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

        # Handle button events
        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)  # Change button color if mouse hovers over it
            button.update(self.SCREEN)  # Update button appearance
        
        for event in pygame.event.get():
            # Check events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Perform actions if easy button is clicked
                    self.view.set_current_state(self.view.GAME)
                    self.current_run = False
                    self.difficulty = "easy"
                    self.view.set_difficulty(self.difficulty)
                    self.stop_running_choose_difficulty_menu()

                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Perform actions if medium button is clicked
                    self.view.set_current_state(self.view.GAME)
                    self.current_run = False
                    self.difficulty = "medium"
                    self.view.set_difficulty(self.difficulty)
                    self.stop_running_choose_difficulty_menu()

                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Perform actions if hard button is clicked
                    self.view.set_current_state(self.view.GAME)
                    self.current_run = False
                    self.difficulty = "hard"
                    self.view.set_difficulty(self.difficulty)
                    self.stop_running_choose_difficulty_menu()
                    
        pygame.display.update()  # Update the display

    def get_difficulty(self):
        # Get the chosen difficulty
        return self.difficulty

    def stop_running_choose_difficulty_menu(self):
        # Stop running the choose difficulty menu
        self.choose_difficulty_running = False

    def running_choose_difficulty_menu(self):
        # Set running state of the choose difficulty menu
        self.choose_difficulty_running = True

    def get_running_choose_difficulty_menu(self):
        # Get running state of the choose difficulty menu
        return self.choose_difficulty_running
import pygame
from .Button import Button
import sys
from pygame import *
from pygame.locals import *

class User_menu:
    def __init__(self, view):
        # Initialize the User_menu class
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

        self.user_running = True  # Flag to control whether user menu is running
        self.go_to_main = False  # Flag to control whether to go back to main menu
        self.go_to_next_menu = False  # Flag to control whether to go to next menu

        self.user_text = ''  # Store user input text

    def get_font(self, size): 
        # Helper function to get font with given size
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)

    def enter_user_name(self):
        # Function to handle user name input
        if self.go_to_next_menu == False:
            message = self.police.render("What is your name, agent?", True, "white")  # Render message
            MENU_MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position

            CONTINUE_BUTTON = Button(image=self.play_button, pos=(250, 280), 
                                text_input="Continue", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            
            GO_BACK_BUTTON = Button(image=self.quit_button, pos=(250, 400), 
                                text_input="Go Back", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

            # Handle button events
            for button in [CONTINUE_BUTTON, GO_BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)  # Change button color if mouse hovers over it
                button.update(self.SCREEN)  # Update button appearance
            
            for event in pygame.event.get():
                # Check events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN: 
                    # Check for keypress
                    if event.key == pygame.K_BACKSPACE: 
                        self.user_text = self.user_text[:-1]  # Remove last character if backspace is pressed
                    else: 
                        self.user_text += event.unicode  # Add character to user input text

                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        mixer.music.stop()  # Stop music
                        self.active_go_to_next_menu()  # Activate going to next menu
                        self.view.choose_difficulty.choose_game_difficulty()  # Go to next menu

                    if GO_BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.active_go_to_main()  # Go back to main menu

        else:
            self.view.choose_difficulty.choose_game_difficulty()  # Go to next menu
            pygame.display.update()  # Update the display

    def stop_running_user_menu(self):
        # Stop running the user menu
        self.user_running = False

    def running_user_menu(self):
        # Set running state of the user menu
        self.user_running = True

    def active_go_to_main(self):
        # Activate going back to main menu
        self.go_to_main = True

    def active_go_to_next_menu(self):
        # Activate going to next menu
        self.go_to_next_menu = True

    def get_running_user_menu(self):
        # Get running state of the user menu
        return self.user_running
    
    def get_go_to_main(self):
        # Get state of going back to main menu
        return self.go_to_main
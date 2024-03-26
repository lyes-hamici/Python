import pygame
from .Button import Button
import sys
from pygame import *
from pygame.locals import *

class Menu:
    def __init__(self, view):
        # Initialize the Menu class
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

        self.difficulty = ""  # Store difficulty level
        self.go_to_enter_user_name = False  # Flag to control whether to go to user name input screen

    def get_font(self, size): 
        # Helper function to get font with given size
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)

    def main_menu(self):
        """Draws the main menu of the game"""
        if self.go_to_enter_user_name == False:
            pygame.display.set_caption("Mines Weeper")  # Set window caption

            musique = pygame.mixer.music.load("assets\\music\\Mission Impossible Theme (Full Theme).mp3")  # Load music
            mixer.music.set_volume(0.1)  # Set music volume
            mixer.music.play(-1)  # Play music in loop

            self.running = True  # Flag to control main menu loop
            self.SCREEN.blit(self.BG, (0, 0))  # Draw background image

            MENU_MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position

            PLAY_BUTTON = Button(image=self.play_button, pos=(250, 280), 
                                text_input="PLAY", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            
            QUIT_BUTTON = Button(image=self.quit_button, pos=(250, 400), 
                                text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

            # Handle button events
            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)  # Change button color if mouse hovers over it
                button.update(self.SCREEN)  # Update button appearance
            
            for event in pygame.event.get():
                # Check events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        # Perform actions if play button is clicked
                        self.active_go_to_user_menu()
                        self.view.user_menu.enter_user_name()

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        # Perform actions if quit button is clicked
                        pygame.quit()
                        sys.exit()

                pygame.display.update()  # Update the display
        else:
            # Go to user name input screen
            self.view.user_menu.enter_user_name()
            pygame.display.update()

    def stop_running_main_menu(self):
        # Stop running the main menu
        self.main_running = False

    def running_main_menu(self):
        # Set running state of the main menu
        self.main_running = True

    def active_go_to_user_menu(self):
        # Activate going to user menu
        self.go_to_enter_user_name = True

    def get_running_main_menu(self):
        # Get running state of the main menu
        return self.main_running
    
    def get_go_to_user_menu(self):
        # Get state of going to user menu
        return self.go_to_enter_user_name
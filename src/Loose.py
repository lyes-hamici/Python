import pygame
from .Button import Button
import sys
from pygame import *
from pygame.locals import *

class Loose:
    def __init__(self, view):
        # Initialize the Loose class
        self.view = view
        pygame.init()
        self.WIDTH = 500
        self.HEIGHT = 500
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # Create a display surface
        self.police = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 30)  # Load font
        self.police_small = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 25)
        self.police_big = pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", 50)

        self.size = (500,500)  # Size of the screen
        self.size_button = (150,100)  # Size of buttons

        # Load background and buttons images
        self.BG = pygame.image.load("assets\\images\\background\\BG_Logo.jpg")
        self.BG = pygame.transform.scale(self.BG, self.size)

        self.play_button = pygame.image.load("assets\\images\\button\\Play Rect.png")
        self.play_button = pygame.transform.scale(self.play_button, self.size_button)

        self.quit_button = pygame.image.load("assets\\images\\button\\Quit Rect.png")
        self.quit_button = pygame.transform.scale(self.quit_button, self.size_button)

        self.loose_running = False  # Flag to control whether the loose menu is running

    def get_font(self,size): 
        # Helper function to get font with given size
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)

    def loose(self):
        """Draws the loose screen"""
        pygame.display.set_caption("Loose Menu")  # Set window caption
        pygame.display.update()  # Update the display

        loose = self.police_big.render(f"You Die !", True, "white")  # Render text

        self.SCREEN.blit(self.BG, (0, 0))  # Draw background image
        self.SCREEN.blit(loose, (180, 100))  # Draw text

        MENU_MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position

        # Create buttons
        MENU_BUTTON = Button(image=self.play_button, pos=(250, 280), 
                            text_input="MENU", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=self.quit_button, pos=(250, 400), 
                            text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

        # Handle button events
        for button in [MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)  # Change button color if mouse hovers over it
            button.update(self.SCREEN)  # Update button appearance

        for event in pygame.event.get():
            # Check events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Perform actions if menu button is clicked
                    self.stop_running_loose_menu()
                    self.view.current_state = 0
                    self.view.resize_window("oups")
                    self.view.controller.reset_game()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Perform actions if quit button is clicked
                    pygame.quit()
                    sys.exit()
                        
        pygame.display.update()  # Update the display

    def stop_running_loose_menu(self):
        # Stop running the loose menu
        self.loose_running = False

    def running_loose_menu(self):
        # Set running state of the loose menu
        self.loose_running = True

    def get_running_loose_menu(self):
        # Get running state of the loose menu
        return self.loose_running

    

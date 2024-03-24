import pygame
from Button import Button
import sys
from pygame import *
from pygame.locals import *

class Menu:
    def __init__(self, view):
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

        self.difficulty = ""

        self.go_to_enter_user_name = False



    def get_font(self,size): 
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)



    def main_menu(self):
        """Draws the main menu of the game"""
        if self.go_to_enter_user_name == False:
            pygame.display.set_caption("Mines Weeper")

            musique = pygame.mixer.music.load("assets\\music\\Mission Impossible Theme (Full Theme).mp3")
            mixer.music.set_volume(0.1)
            mixer.music.play(-1)

            self.running = True
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()


            PLAY_BUTTON = Button(image=self.play_button, pos=(250, 280), 
                                text_input="PLAY", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            
            
            QUIT_BUTTON = Button(image=self.quit_button, pos=(250,400), 
                                text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")


            for button in [PLAY_BUTTON,QUIT_BUTTON]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    #if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.active_go_to_user_menu()
                        self.view.user_menu.enter_user_name()

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):

                        pygame.quit()

                        sys.exit()

                pygame.display.update()


        else:
            self.view.user_menu.enter_user_name()
            pygame.display.update()



    def stop_running_main_menu(self):
        self.main_running = False

    def running_main_menu(self):
        self.main_running = True

    def active_go_to_user_menu(self):
        self.go_to_enter_user_name = True

    def get_running_main_menu(self):
        return self.main_running
    
    def get_go_to_user_menu(self):
        return self.go_to_enter_user_name
import pygame
from .Button import Button
import sys
from pygame import *
from pygame.locals import *

class User_menu:
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

        self.user_running = True
        self.go_to_main = False
        self.go_to_next_menu = False

        self.user_text = '' 



    def get_font(self,size): 
        return pygame.font.Font("assets\\font\\BroncoPersonalUse.ttf", size)

    def enter_user_name(self):
        if self.go_to_next_menu == False:
            message = self.police.render("What is your name, agent?",True,"white")
            '''clock = pygame.time.Clock() 
            input_rect = pygame.Rect(200, 180, 140, 38) 


            color_passive = pygame.Color('grey') 
            color = color_passive 
            base_font = self.get_font(30) 
        
            self.SCREEN.blit(self.BG,(0,0))
            self.SCREEN.blit(message,(115,100))'''
            MENU_MOUSE_POS = pygame.mouse.get_pos()


            CONTINUE_BUTTON = Button(image=self.play_button, pos=(250, 280), 
                                text_input="Continue", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            
            
            GO_BACK_BUTTON = Button(image=self.quit_button, pos=(250,400), 
                                text_input="Go Back", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")


            for button in [CONTINUE_BUTTON,GO_BACK_BUTTON]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

                if event.type == pygame.KEYDOWN: 

                    # Check for backspace 
                    if event.key == pygame.K_BACKSPACE: 

                        self.user_text = self.user_text[:-1] 
                    else: 
                        self.user_text += event.unicode


        


                    
        


                if event.type == pygame.MOUSEBUTTONDOWN: 

                    if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        mixer.music.stop()
                        self.active_go_to_next_menu()
                        self.view.choose_difficulty.choose_game_difficulty()

                    if GO_BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.active_go_to_main()

        else:
            self.view.choose_difficulty.choose_game_difficulty()
            pygame.display.update()


        



    def stop_running_user_menu(self):
        self.user_running = False

    def running_user_menu(self):
        self.user_running = True

    def active_go_to_main(self):
        self.go_to_main = True

    def active_go_to_next_menu(self):
        self.go_to_next_menu = True

    def get_running_user_menu(self):
        return self.user_running
    
    def get_go_to_main(self):
        return self.go_to_main
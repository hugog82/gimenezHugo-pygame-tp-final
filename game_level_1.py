import pygame
from pygame.locals import *
from constants import *
#from gui_form import Form
from gui_button import Button
#from gui_textbox import TextBox
#from gui_progressbar import ProgressBar
from player import *
from enemy import *
from platform import *
from background import *
from bullet import *
from level_1 import *

class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        # self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        # self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        # self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        # self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        # self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        # --- GAME ELEMNTS --- 
        self.time_game = 20
        self.static_background = Background(x=0,y=0,width=w,height=h,path=IMAGE_PATH + "bg.jpg")

        self.player_1 = Player(x=SCREEN_WIDTH/2,y=450,speed_walk=25,speed_run=50,gravity=30,frame_rate_ms=50,move_rate_ms=50,jump_power=100,jump_height=120,p_scale=0.22)

        self.enemy_list = []
        self.enemy_list.append (Enemy(x=200,y=452,speed_walk=8,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))
        self.enemy_list.append (Enemy(x=1000,y=452,speed_walk=8,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))

        self.platforms_list = get_platform()
        self.items_list = get_item()
        self.bullets_list = []

    # def on_click_boton1(self, parametro):
    #     self.set_active(parametro)

    # def on_click_shoot(self, parametro):
    #     for enemy_element in self.enemy_list:
    #         self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))

    def update(self, events_list,keys,delta_ms):
        
        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)

        self.pb_lives.value = self.player_1.lives 


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)
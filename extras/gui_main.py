import pygame, sys
from pygame.locals import *
from constants import *
from extras.gui_button import Button

flag = True
flags = DOUBLEBUF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)
pygame.init()
clock = pygame.time.Clock()

def on(parameter):
    print("click",parameter)

button1 = Button(master_surface=screen,x=100,y=50,w=200,h=50,color_background=RED,color_border=GREEN,on_click=on,on_click_param="Hello",text="MENU",font="Verdana",font_size=30,font_color=("blue"))
button2 = Button(master_surface=screen,x=400,y=50,w=200,h=50,color_background=RED,color_border=GREEN,on_click=on,on_click_param="Goodbye",text="OPCIONES",font="Arial",font_size=30,font_color=("green"))
buttons_list = [button1,button2]

while flag:
    events_list = pygame.event.get()
    for event in events_list:
        if event.type == pygame.QUIT:   
            flag = False
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    '''
    events
    update
    draw
    '''
    for button_aux in buttons_list:
        button_aux.update(events_list)

    for button_aux in buttons_list:
        button_aux.draw()

    pygame.display.flip()
        
pygame.quit()
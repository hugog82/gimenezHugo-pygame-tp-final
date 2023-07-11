import pygame, sys, pygame.color
from pygame.locals import *
from constants import *
from button import Button

pygame.init()

size = (800, 600   )
screen = pygame.display.set_mode(size)
running = True

pygame.display.set_caption('Main Menu')

game_paused = False
menu_state = "main"

font = pygame.font.SysFont("timesnewroman",50)

TEXT_COLOUR =("white")
#load button images
resume_image = pygame.image.load(IMAGE_PATH+"images/button_resume.png").convert_alpha()
options_image = pygame.image.load(IMAGE_PATH+"images/button_options.png").convert_alpha()
exit_image = pygame.image.load(IMAGE_PATH+"images/button_exit.png").convert_alpha()
video_image = pygame.image.load(IMAGE_PATH+"images/button_resume.png").convert_alpha()
audio_image = pygame.image.load(IMAGE_PATH+"images/button_options.png").convert_alpha()
exit_image = pygame.image.load(IMAGE_PATH+"images/button_exit.png").convert_alpha()

#create button instances
resume_button = Button(240,125,resume_image,0.12)
options_button = Button(240,250,options_image,0.12)
exit_button = Button(240,375,exit_image,0.12)
video_button = Button(240,125,resume_image,0.15)
audio_button = Button(240,250,options_image,0.15)
quit_button = Button(240,375,exit_image,0.15)

def draw_text(text,font,text_color,x,y):
    image = font.render(text,True,text_color)
    screen.blit(image,(x,y))
    
    
while running:
    
    screen.fill(("steelblue"))
    
    if game_paused == True:
        #check menu state
        if menu_state == "main":
            #draw pause screen button
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if exit_button.draw(screen):
                running = False
        if menu_state == "options":
            #draw the differents options buttons
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if quit_button.draw(screen):
                menu_state = "main"
            
    else:
        draw_text("Press ESC to pause",font,TEXT_COLOUR,200,250)
        
        
 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        if event.type == pygame.QUIT:
            running = False
      
    pygame.display.update()    
pygame.quit()
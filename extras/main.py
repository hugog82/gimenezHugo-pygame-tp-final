import pygame, sys, pygame.color
from pygame.locals import *
from extras.button import *
from constants import *
from auxiliar import *

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Menu :D')

start_image = pygame.image.load("extras/start.png")
exit_image = pygame.image.load("extras/exit.png")
resume_image = pygame.image.load("extras/resume.png")


start_button = Button(250,150,start_image,0.5)
exit_button = Button(250,300,exit_image,0.23)
resume_button = Button(250,300,resume_image,0.5)

game_paused = False
game_state = "main"

running = True

while running:
    screen.fill("lightblue")
    if start_button.draw_button(screen):
        game_state = "main"
    if exit_button.draw_button(screen):
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = not game_paused
                if start_button.draw_button(screen):
                    game_state = "main"
                if exit_button.draw_button(screen):
                    running = False
    if not game_paused:
        game_state = "main"
    else:
        draw_text(screen,"Press ESC to pause",50,400,SCREEN_HEIGHT//2)       
                
            
    pygame.display.update()
    
pygame.quit()


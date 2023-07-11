import pygame, sys
from pygame.locals import *

class Widget:
    def __init__(self,master_surface,x,y,w,h,color_background,color_border) -> None:
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
    
    
    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.master_surface.blit(self.slave_surface,self.slave_rect)

class Button(Widget):
    def __init__(self,master_surface,x,y,w,h,color_background,color_border,on_click,on_click_param,text,font,font_size,font_color) -> None:
        super().__init__(master_surface,x,y,w,h,color_background,color_border)
        pygame.font.init()

        self.on_click = on_click
        self.on_click_param = on_click_param
        self.text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
    
    def render(self):
        image_text = self.font_sys.render(self.text,True,self.font_color,self.color_background)
        self.slave_surface = pygame.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_surface.fill(self.color_background)
        self.slave_surface.blit(image_text,(5,5))

    def update(self,events_list):
        for event in events_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect.collidepoint(event.pos)):
                    self.on_click(self.on_click_param)

        self.render()
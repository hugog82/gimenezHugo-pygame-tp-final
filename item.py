import pygame
from constants import *
from auxiliar import Auxiliar

class Item:
    def __init__(self,path,index,quantity,x,y,width,height) -> None: 
        
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(path,index,quantity,flip=False,w=width,h=height)
        self.frame = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()        
    
        self.rect.x = x
        self.rect.y = y
        self.rect_collition = pygame.Rect(self.rect)
        
        self.current_time_animation = 0
        self.frame_rate_ms = 100
        
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        
    
    def do_animation(self,delta_ms):
        self.current_time_animation += delta_ms
        if(self.current_time_animation >= self.frame_rate_ms):
            self.current_time_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    

    def update(self,delta_ms):               
        self.do_animation(delta_ms)
      

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=("red"),rect=self.collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
    
    
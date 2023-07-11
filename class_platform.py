import pygame
from constants import *
from auxiliar import Auxiliar

class Platform:
    def __init__(self,path,index,quantity,x,y,width,height,type=0) -> None:
        
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(path,index,quantity,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_collition = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect)
        self.rect_ground_collition.height = GROUND_COLLIDE_H

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color="red",rect=self.rect_collition)
            pygame.draw.rect(screen,color="green",rect=self.rect_ground_collition)
        screen.blit(self.image,self.rect)
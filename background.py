import pygame
from constants import *
from auxiliar import Auxiliar


class Background:
    def __init__(self, x, y,screen_size,path):

        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,screen_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self,screen):
        screen.blit(self.image,self.rect)
       
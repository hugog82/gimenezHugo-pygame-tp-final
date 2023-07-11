import pygame, sys
from constants import *
from auxiliar import Auxiliar


class Player_2:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1) -> None:
        self.stay_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Stand/{0}.png",0,10,False,scale=p_scale)
        self.stay_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Stand/{0}.png",0,10,True,scale=p_scale)        
        self.walk_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Walk/{0}.png",0,10,False,scale=p_scale)
        self.walk_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Walk/{0}.png",0,10,True,scale=p_scale)
        self.jump_right =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Jump/{0}.png",0,10,False,scale=p_scale)
        self.jump_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Jump/{0}.png",0,10,True,scale=p_scale)
        self.knife_right =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Attack1H/{0}.png",0,10,False,scale=p_scale)
        self.knife_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/viking_sword/Attack1H/{0}.png",0,10,True,scale=p_scale)
        
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_right
        self.direction = DIRECTION_RIGHT
        self.image = self.animation[self.frame]              
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.current_time_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.current_time_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        
        self.rect_colliton = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3,self.rect.y + self.rect.h -GROUND_RECT_H,self.rect.w /3,GROUND_RECT_H)
    
    def walk (self, direction):
        
        if (self.direction != direction or (self.animation != self.walk_right and self.animation != self.walk_left)):
            self.frame = 0
        
            self.direction = direction
            if (direction == DIRECTION_RIGHT):
                self.move_x = self.speed_walk
                self.animation = self.walk_right
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_left
    
    def jump (self, on_off=True):
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if (self.direction == DIRECTION_RIGHT):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_right
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_left
            self.frame = 0
            self.is_jump = True
        elif(on_off == False):
            self.is_jump = False
            self.stay()
            
    def knife(self,on_off = True):
        
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_right and self.animation != self.knife_left):
                self.frame = 0
                if(self.direction == DIRECTION_RIGHT):
                    self.animation = self.knife_right
                else:
                    self.animation = self.knife_left
            
    def stay (self):
        if (self.animation != self.stay_right and self.animation != self.stay_left):
            if (self.direction == DIRECTION_RIGHT):
                self.animation = self.stay_right
            else:
                self.animation = self.stay_left
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement (self, delta_ms,platforms_list):
        self.current_time_move += delta_ms
        if (self.current_time_move >= self.move_rate_ms):
            if (abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
            
            self.current_time_move = 0                          
            self.add_x (self.move_x)
            self.add_y (self.move_y)  
            
            if not (self.is_on_platform(platforms_list)):
                self.add_y (self.gravity)
            elif(self.is_jump): #SACAR
                self.jump(False)
                
    def is_on_platform(self,platforms_list):
        retorno = False
        if (self.rect.y >= GROUND_LEVEL):
            retorno = True
        else:
            for platform in platforms_list:
                if(self.rect_ground_collition.colliderect(platform.rect_ground_collition)):
                    retorno = True
                    break
        return retorno
    
    def collide_item (self,items_list):
        retorno = False
        for item in items_list:
            if(self.rect_colliton.colliderect(item.rect_collition)):
                retorno = True
                break
        return retorno
                
    def add_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        
    def add_y(self, delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        
        
    def do_animation (self, delta_ms):
        self.current_time_animation += delta_ms
        if (self.current_time_animation >= self.frame_rate_ms):
            self.current_time_animation = 0
            if (self.frame < len(self.animation) -1):
                self.frame += 1
            else:
                self.frame = 0
                
    def update(self, delta_ms,platforms_list):
        self.do_movement(delta_ms,platforms_list)
        self.do_animation(delta_ms)

        
    def draw (self, screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)           
        self.image = self.animation[self.frame]              
        screen.blit(self.image, self.rect)

    def events (self,delta_ms,keys):
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_LEFT)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_RIGHT)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys [pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys [pygame.K_SPACE]):
            self.stay()
        if(keys [pygame.K_SPACE]):
            self.jump(True)
        if(keys[pygame.K_a]):
            self.knife()  
            
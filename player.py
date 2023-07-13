import pygame, sys
from constants import *
from auxiliar import *
from bullet import Bullet
from background import Background

class Player:
    def __init__(self,name,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1) -> None:
        self.stay_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Idle__00{0}.png",0,10,False,scale=p_scale)
        self.stay_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Idle__00{0}.png",0,10,True,scale=p_scale)        
        self.walk_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Run__00{0}.png",0,10,False,scale=p_scale)
        self.walk_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Run__00{0}.png",0,10,True,scale=p_scale)
        self.jump_right =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Jump__00{0}.png",0,10,False,scale=p_scale)
        self.jump_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Jump__00{0}.png",0,10,True,scale=p_scale)
        self.knife_right =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Attack__00{0}.png",0,10,False,scale=p_scale)
        self.knife_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Attack__00{0}.png",0,10,True,scale=p_scale)
        self.throw_right =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Throw__00{0}.png",0,10,False,scale=p_scale)
        self.throw_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Throw__00{0}.png",0,10,True,scale=p_scale)
        self.dead_right =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Dead__00{0}.png",0,10,False,scale=p_scale)
        self.dead_left =Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"players/ninja_boy/Dead__00{0}.png",0,10,True,scale=p_scale)
        self.name = name        
        self.frame = 0
        self.lives = 5
        self.energy = 100
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
        # self.is_shoot = False
        # self.is_knife = False
        
        self.rect_collition = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3,self.rect.y + self.rect.h -GROUND_RECT_H,self.rect.w /3,GROUND_RECT_H)
        self.is_dead = False
    
    def receive_shoot(self):
        self.energy -= 0.5
        
        
    def dead (self):
        if self.energy <= 0:
            if not self.is_dead:
                if (self.direction == DIRECTION_RIGHT):
                    self.animation = self.dead_right
                else:
                    self.animation = self.dead_left
                self.frame = 0
                self.is_dead = True
            
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
            if self.rect.right > SCREEN_WIDTH:
                    self.rect.right = SCREEN_WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
                
    def throw (self):
        
        if (self.animation != self.throw_right and self.animation != self.throw_left):
            if (self.direction == DIRECTION_RIGHT):
                self.animation = self.throw_right
            else:
                self.animation = self.throw_left
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
    
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
            elif(self.is_jump):
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
        self.do_animation(delta_ms)
        self.dead()
        if not self.is_dead:
            self.do_movement(delta_ms,platforms_list)
        else:
            if self.frame == len(self.animation)-1:
                self.frame = len(self.animation)-2

        
    def draw (self, screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)           
        self.image = self.animation[self.frame]              
        screen.blit(self.image, self.rect)

    def events (self,delta_ms,keys,bullets_list,arrow_sound):
        if not self.is_dead:
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_LEFT)
                if self.rect.left < 0:
                    self.rect.left = 0
                    self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3,self.rect.y + self.rect.h -GROUND_RECT_H,self.rect.w /3,GROUND_RECT_H)
            if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_RIGHT)
                if self.rect.right > SCREEN_WIDTH:
                    self.rect.right = SCREEN_WIDTH
                    self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3,self.rect.y + self.rect.h -GROUND_RECT_H,self.rect.w /3,GROUND_RECT_H)
            if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                self.stay()
            if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                self.stay()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jump(True)
                        if self.rect.y <= 0:
                            self.rect.y = 0
                            self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3,self.rect.y + self.rect.h -GROUND_RECT_H,self.rect.w /3,GROUND_RECT_H)
                    if event.key == pygame.K_a:
                        if self.direction == DIRECTION_RIGHT:
                            bullets_list.append(Bullet(self,self.rect.centerx,self.rect.centery,SCREEN_WIDTH,self.rect.centery,10,IMAGE_PATH+"players/ninja_boy/Kunai.png",100,20,10,5))
                            arrow_sound.play()
                            self.throw()
                        else:
                            bullets_list.append(Bullet(self,self.rect.centerx,self.rect.centery,0,self.rect.centery,10,IMAGE_PATH+"players/ninja_boy/Kunai.png",100,20,10,5))
                            arrow_sound.play()
                            self.throw()

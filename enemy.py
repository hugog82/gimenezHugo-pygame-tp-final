from player import *
from constants import *
from auxiliar import Auxiliar
from bullet import Bullet

class Enemy():
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        self.stay_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_sword/IDLE/IDLE_00{0}.png",0,7,False,scale=p_scale)
        self.stay_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_sword/IDLE/IDLE_00{0}.png",0,7,True,scale=p_scale)
        self.walk_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_sword/WALK/WALK_00{0}.png",0,7,False,scale=p_scale)
        self.walk_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_sword/WALK/WALK_00{0}.png",0,7,True,scale=p_scale)
        self.die_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_sword/DIE/DIE_00{0}.png",0,7,False,scale=p_scale)
        self.die_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_sword/DIE/DIE_00{0}.png",0,7,True,scale=p_scale)
          
        self.counter = 0
        self.frame = 0
        self.lives = 1
        self.energy = 20
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_right
        self.direction = DIRECTION_RIGHT
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_fall = False
        self.is_dead = False

        self.current_time_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.current_time_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.current_time = 0
        self.last_jump_time = 0
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,platforms_list,bullets_list):
        if not self.dead():
            self.current_time_move += delta_ms
            if(self.current_time_move >= self.move_rate_ms):
                self.current_time_move = 0

                if(not self.is_on_platform(platforms_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                else:
                    self.is_fall = False
                    self.change_x(self.move_x)
                    if self.counter <= 20:
                        self.move_x = -self.speed_walk
                        self.animation = self.walk_left
                        self.counter += 1                 
                        
                    elif self.counter <= 40:
                        self.move_x = self.speed_walk
                        self.animation = self.walk_right
                        self.counter += 1
                    else:
                        self.counter = 0
                      
                        
    def is_on_platform(self,platforms_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for platform in  platforms_list:
                if(self.ground_collition_rect.colliderect(platform.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        if not self.dead():
            self.current_time_animation += delta_ms
            if(self.current_time_animation >= self.frame_rate_ms):
                self.current_time_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0
    
    
    def dead (self):
        if self.energy <= 0:
            if not self.is_dead:
                if (self.direction == DIRECTION_RIGHT):
                    self.animation = self.die_right
                else:
                    self.animation = self.die_left
                self.frame = 0
                self.is_dead = True

    def update(self,delta_ms,platforms_list,bullets_list):
        self.do_animation(delta_ms)
        self.dead()
        if not self.is_dead:
            self.do_movement(delta_ms,platforms_list,bullets_list)
        else:
            if self.frame == len(self.animation)-1:
                self.frame = len(self.animation)-2
                
      

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=("red"),rect=self.collition_rect)
            pygame.draw.rect(screen,color=("green"),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.energy -= 1

class Enemy_2():
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        self.stay_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_hammer/IDLE/IDLE_00{0}.png",0,7,False,scale=p_scale)
        self.stay_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_hammer/IDLE/IDLE_00{0}.png",0,7,True,scale=p_scale)
        self.walk_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_hammer/WALK/WALK_00{0}.png",0,7,False,scale=p_scale)
        self.walk_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_hammer/WALK/WALK_00{0}.png",0,7,True,scale=p_scale)
        self.die_right = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_hammer/DIE/DIE_00{0}.png",0,7,False,scale=p_scale)
        self.die_left = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"enemy/ork_hammer/DIE/DIE_00{0}.png",0,7,True,scale=p_scale)
          
        self.counter = 0
        self.frame = 0
        self.lives = 1
        self.energy = 20
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_right
        self.direction = DIRECTION_RIGHT
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_fall = False
        self.is_dead = False

        self.current_time_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.current_time_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.current_time = 0
        self.last_jump_time = 0
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,platforms_list,bullets_list):
        if not self.dead():
            self.current_time_move += delta_ms
            if(self.current_time_move >= self.move_rate_ms):
                self.current_time_move = 0
                self.change_x(self.move_x)
                if self.counter <= 20:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_left
                    self.counter += 1                 
                    
                elif self.counter <= 40:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_right
                    self.counter += 1
                else:
                    self.counter = 0
                        

    def do_animation(self,delta_ms):
        if not self.dead():
            self.current_time_animation += delta_ms
            if(self.current_time_animation >= self.frame_rate_ms):
                self.current_time_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0
    
    
    def dead (self):
        if self.energy <= 0:
            if not self.is_dead:
                if (self.direction == DIRECTION_RIGHT):
                    self.animation = self.die_right
                else:
                    self.animation = self.die_left
                self.frame = 0
                self.is_dead = True

    def update(self,delta_ms,platforms_list,bullets_list):
        self.do_animation(delta_ms)
        self.dead()
        if not self.is_dead:
            self.do_movement(delta_ms,platforms_list,bullets_list)
        else:
            if self.frame == len(self.animation)-1:
                self.frame = len(self.animation)-2
                
      

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=("red"),rect=self.collition_rect)
            pygame.draw.rect(screen,color=("green"),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.energy -= 1


class Enemy_3():
    def __init__(self,x,y,speed_walk,speed_run) -> None:
        self.walk_left = Auxiliar.getSurfaceFromSpriteSheet (IMAGE_PATH+"enemy/hell_bartender/hell_bartender__x1_idle1_png_1354837767.png",14,6,flip=False, step=1)[:81]
        self.walk_right = Auxiliar.getSurfaceFromSpriteSheet (IMAGE_PATH+"enemy/hell_bartender/hell_bartender__x1_idle1_png_1354837767.png",14,6,flip=True, step=1)[:81]
        self.die_right = Auxiliar.getSurfaceFromSpriteSheet(IMAGE_PATH+"effects/explosions/explosion-4.png",12,1,flip=False, step=1)
        self.die_left = Auxiliar.getSurfaceFromSpriteSheet(IMAGE_PATH+"effects/explosions/explosion-4.png",12,1,flip=True, step=1)
        self.counter = 0
        self.frame = 0
        self.lives = 1
        self.energy = 20
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.animation = self.walk_right
        self.direction = DIRECTION_RIGHT
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_fall = False
        self.is_dead = False

        self.current_time_animation = 0
        self.frame_rate_ms = 50 
        self.current_time_move = 0
        self.move_rate_ms = 50
        self.y_start_jump = 0

        self.current_time = 0
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,platforms_list,bullets_list):
        if not self.dead():
            self.current_time_move += delta_ms
            if(self.current_time_move >= self.move_rate_ms):
                self.current_time_move = 0
                self.change_x(self.move_x)
                if self.counter <= 20:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_left
                    self.counter += 1                 
                    
                elif self.counter <= 40:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_right
                    self.counter += 1
                else:
                    self.counter = 0
                        

    def do_animation(self,delta_ms):
        if not self.dead():
            self.current_time_animation += delta_ms
            if(self.current_time_animation >= self.frame_rate_ms):
                self.current_time_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0
    
    
    def dead (self):
        if self.energy <= 0:
            if not self.is_dead:
                if (self.direction == DIRECTION_RIGHT):
                    self.animation = self.die_right
                else:
                    self.animation = self.die_left
                self.frame = 0
                self.is_dead = True

    def update(self,delta_ms,platforms_list,bullets_list):
        self.do_animation(delta_ms)
        self.dead()
        if not self.is_dead:
            self.do_movement(delta_ms,platforms_list,bullets_list)
        else:
            if self.frame == len(self.animation)-1:
                self.frame = len(self.animation)-2
                
      

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=("red"),rect=self.collition_rect)
            pygame.draw.rect(screen,color=("green"),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.energy -= 1

class Enemy_4():
    def __init__(self,x,y,speed_walk) -> None:
        self.walk_right = Auxiliar.getSurfaceFromSpriteSheet (IMAGE_PATH+"enemy/jabba1/npc_jabba1__x1_walk_png_1354831096.png",2,7,flip=False, step=1)
        self.walk_left = Auxiliar.getSurfaceFromSpriteSheet (IMAGE_PATH+"enemy/jabba1/npc_jabba1__x1_walk_png_1354831096.png",2,7,flip=True, step=1)
        self.die_right = Auxiliar.getSurfaceFromSpriteSheet(IMAGE_PATH+"effects/explosions/explosion-4.png",12,1,flip=False, step=1)
        self.die_left = Auxiliar.getSurfaceFromSpriteSheet(IMAGE_PATH+"effects/explosions/explosion-4.png",12,1,flip=True, step=1)
        self.counter = 0
        self.frame = 0
        self.lives = 1
        self.energy = 20
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.animation = self.walk_right
        self.direction = DIRECTION_RIGHT
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.is_dead = False

        self.current_time_animation = 0
        self.frame_rate_ms = 50 
        self.current_time_move = 0
        self.move_rate_ms = 50

        self.current_time = 0
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,platforms_list,bullets_list):
        if not self.dead():
            self.current_time_move += delta_ms
            if(self.current_time_move >= self.move_rate_ms):
                self.current_time_move = 0
                self.change_x(self.move_x)
                if self.counter <= 10:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_left
                    self.counter += 1                 
                    
                elif self.counter <= 20:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_right
                    self.counter += 1
                else:
                    self.counter = 0
                        

    def do_animation(self,delta_ms):
        if not self.dead():
            self.current_time_animation += delta_ms
            if(self.current_time_animation >= self.frame_rate_ms):
                self.current_time_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0
    
    
    def dead (self):
        if self.energy <= 0:
            if not self.is_dead:
                if (self.direction == DIRECTION_RIGHT):
                    self.animation = self.die_right
                else:
                    self.animation = self.die_left
                self.frame = 0
                self.is_dead = True

    def update(self,delta_ms,platforms_list,bullets_list):
        self.do_animation(delta_ms)
        self.dead()
        if not self.is_dead:
            self.do_movement(delta_ms,platforms_list,bullets_list)
        else:
            if self.frame == len(self.animation)-1:
                self.frame = len(self.animation)-2
                

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=("red"),rect=self.collition_rect)
            pygame.draw.rect(screen,color=("green"),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.energy -= 1
       
from player import *
from constants import *
from auxiliar import Auxiliar
from bullet import Bullet

class Dynamic_platform():
    def __init__(self,x,y,speed_move,frame_rate_ms,move_rate_ms,p_scale=1) -> None:
        self.surface = Auxiliar.getSurfaceFromSeparateFiles(IMAGE_PATH+"tileset/space_ship/Tiles/BGTile ({0}).png",3,4,False,scale=p_scale)
        
        self.counter = 0
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_move =  speed_move
        self.animation = self.surface
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_collition = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect)
        self.rect_ground_collition.height = GROUND_COLLIDE_H
    
        self.current_time_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.current_time_move = 0
        self.move_rate_ms = move_rate_ms
        
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_collition.x += delta_x
        self.rect_ground_collition.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_collition.y += delta_y
        self.rect_ground_collition.y += delta_y

    def do_movement(self,delta_ms):
        self.current_time_move += delta_ms
        if(self.current_time_move >= self.move_rate_ms):
            self.current_time_move = 0
            self.change_x(self.move_x)
            if self.counter <= 20:
                self.move_x = -self.speed_move
                self.animation = self.surface
                self.counter += 1                 
                
            elif self.counter <= 40:
                self.move_x = self.speed_move
                self.animation = self.surface
                self.counter += 1
            else:
                self.counter = 0
                        

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
        self.do_movement(delta_ms)
              

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=("red"),rect=self.rect_collition)
            pygame.draw.rect(screen,color=("green"),rect=self.rect_ground_collition)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
import pygame, sys
from button import Button
from constants import *
from player import *
from auxiliar import *
from enemy import *
from class_platform import Platform
from dynamic_platf import *
from level_1 import *
from level_3 import *
from level_2 import *
from score import *
from bullet import *
from item import *
from platform import *

pygame.init()


SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Menu")

background = pygame.image.load("assets/Background.png")
stage_flag_1 = False
stage_flag_2 = False
stage_flag_3 = False


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def stage_1():
    flag = True
    time_game = 50
    
    pygame.mixer.set_num_channels(8)
    pygame.mixer.music.load(IMAGE_PATH+"sounds/Street-Mayhem.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    item_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/coin.mp3")
    player_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/CHILD6.mp3")
    arrow_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/throw.mp3")
        
    background = pygame.image.load("Assets/bg.jpg")
    background = pygame.transform.scale(background, SCREEN_SIZE)
    
    event_time_1000_ms = pygame.USEREVENT
    pygame.time.set_timer(event_time_1000_ms,1000)

    event_time_shoot_2000_ms = pygame.USEREVENT +1
    pygame.time.set_timer(event_time_shoot_2000_ms,5000)

    clock = pygame.time.Clock()

    player = Player(x=SCREEN_WIDTH/2,y=GROUND_LEVEL,speed_walk=25,speed_run=50,gravity=20,frame_rate_ms=50,move_rate_ms=50,jump_power=100,jump_height=120,p_scale=0.22)

    enemy_list = []
    enemy_list.append (Enemy(x=200,y=452,speed_walk=8,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))
    enemy_list.append (Enemy(x=1000,y=452,speed_walk=8,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))

    path_platform = IMAGE_PATH+"tileset/forest/Tiles/{0}.png"
    
    platforms_list = []
    platforms_list.append(Platform(path_platform,1,18,x=50,y=250,width=50,height=30,type=12))
    platforms_list.append(Platform(path_platform,1,18,x=100,y=250,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=150,y=250,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=200,y=250,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=250,y=250,width=50,height=30,type=14))
    platforms_list.append(Platform(path_platform,1,18,x=900,y=250,width=50,height=30,type=12))
    platforms_list.append(Platform(path_platform,1,18,x=950,y=250,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=1000,y=250,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=1050,y=250,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=1100,y=250,width=50,height=30,type=14))

    platforms_list.append(Platform(path_platform,1,18,x=450,y=200,width=50,height=30,type=12))
    platforms_list.append(Platform(path_platform,1,18,x=500,y=200,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=550,y=200,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=600,y=200,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=650,y=200,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=700,y=200,width=50,height=30,type=14))

    platforms_list.append(Platform(path_platform,1,18,x=380,y=350,width=50,height=30,type=12))
    platforms_list.append(Platform(path_platform,1,18,x=430,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=480,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=530,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=580,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=630,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=680,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=730,y=350,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=780,y=350,width=50,height=30,type=14))

    platforms_list.append(Platform(path_platform,1,18,x=50,y=400,width=50,height=30,type=12))
    platforms_list.append(Platform(path_platform,1,18,x=100,y=400,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=150,y=400,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=200,y=400,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=250,y=400,width=50,height=30,type=14))
    platforms_list.append(Platform(path_platform,1,18,x=900,y=400,width=50,height=30,type=12))
    platforms_list.append(Platform(path_platform,1,18,x=950,y=400,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=1000,y=400,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=1050,y=400,width=50,height=30,type=13))
    platforms_list.append(Platform(path_platform,1,18,x=1100,y=400,width=50,height=30,type=14))
    
    items_list = []
    items_list.append(Item(path_amber,0,2,x=100,y=100,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=150,y=100,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=200,y=100,width=25,height=25))
    
    items_list.append(Item(path_amber,0,2,x=950,y=100,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=1000,y=100,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=1050,y=100,width=25,height=25))
    
    items_list.append(Item(path_amber,0,2,x=500,y=80,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=550,y=80,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=600,y=80,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=650,y=80,width=25,height=25))
    
    items_list.append(Item(path_amber,0,2,x=100,y=300,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=150,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=200,y=300,width=25,height=25))
    
    items_list.append(Item(path_amber,0,2,x=950,y=300,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=1000,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=1050,y=300,width=25,height=25))
    
    items_list.append(Item(path_amber,0,2,x=480,y=250,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=530,y=250,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=630,y=250,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=680,y=250,width=25,height=25))
    
    bullets_list = []
    
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                flag = False
                sys.exit()
            if event.type == event_time_1000_ms:
                time_game -= 1
            if event.type == event_time_shoot_2000_ms:
                for enemy in enemy_list:
                    if not enemy.is_dead:
                        if enemy.direction == DIRECTION_RIGHT:
                            bullets_list.append(Bullet(enemy,enemy.rect.centerx,enemy.rect.centery,player.rect.centerx,player.rect.centery,2,IMAGE_PATH+"images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",100,5,5,5))
                        else:
                            bullets_list.append(Bullet(enemy,enemy.rect.centerx,enemy.rect.centery,player.rect.centerx,player.rect.centery,2,IMAGE_PATH+"images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",100,5,5,5))
                    
        keys = pygame.key.get_pressed()
                        
        delta_ms = clock.tick(FPS)
                
        SCREEN.blit(background,(0,0))
        
        for class_platform in platforms_list:
            class_platform.draw(SCREEN)
            
        for item in items_list:
            item.update(delta_ms)
            item.draw(SCREEN)
            
            if(player.rect.colliderect(item.rect_collition)):
                items_list.remove(item)
                player.score += 10
                item_sound.play()
                
        for bullet in bullets_list:
            bullet.update(delta_ms,platforms_list,enemy_list,player)
            bullet.draw(SCREEN)
            
            
        for enemy in enemy_list:     
            enemy.update(delta_ms,platforms_list,bullets_list)
            enemy.draw(SCREEN)
            if not enemy.is_dead:
                if(player.rect.colliderect(enemy.collition_rect)):
                    player.energy -= 0.5
                    player_sound.play()
        
        player.events(delta_ms,keys,bullets_list,arrow_sound)
        player.update(delta_ms,platforms_list)
        player.draw(SCREEN)
        
        
        draw_text (SCREEN, str("Time = {0}".format(time_game)), 30, SCREEN_WIDTH -SCREEN_WIDTH+100, 10)
        draw_text (SCREEN, str("Score = {0}".format(player.score)), 30, SCREEN_WIDTH // 2, 10)
        draw_player_energy(SCREEN,SCREEN_WIDTH -250,10,player.energy)
        
        if time_game <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            time_up()
            
        elif player.energy <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            loser()
            
        elif items_list == [] and enemy.energy <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            winner()

        pygame.display.flip()
   
def stage_2():
    flag = True
    time_game = 50
    event_time_1000_ms = pygame.USEREVENT
    pygame.time.set_timer(event_time_1000_ms,1000)

    event_time_shoot_5000_ms = pygame.USEREVENT +1
    pygame.time.set_timer(event_time_shoot_5000_ms,5000)

    clock = pygame.time.Clock()
    background = pygame.image.load("extras/bg_2.jpg")
    background = pygame.transform.scale(background, SCREEN_SIZE)

    pygame.mixer.set_num_channels(8)
    pygame.mixer.music.load(IMAGE_PATH+"sounds/Into-the-Haunted-Forest.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    item_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/coin.mp3")
    player_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/CHILD6.mp3")
    arrow_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/throw.mp3")
                                
    player = Player(x=SCREEN_WIDTH-SCREEN_WIDTH+25,y=GROUND_LEVEL,speed_walk=25,speed_run=50,gravity=20,frame_rate_ms=50,move_rate_ms=50,jump_power=100,jump_height=120,p_scale=0.22)

    enemy_list = []
    enemy_list.append (Enemy_3(x=200,y=50,speed_walk=8,speed_run=16))
    enemy_list.append (Enemy_5(x=1000,y=GROUND_LEVEL,speed_walk=10))
    enemy_list.append (Enemy_6(x=1100,y=250,speed_walk=8))
    enemy_list.append (Enemy_7(x=550,y=350,speed_walk=8))
    enemy_list.append (Enemy_7(x=750,y=350,speed_walk=8))
    enemy_list.append (Enemy_7(x=950,y=350,speed_walk=8))
    
    path_platform = IMAGE_PATH+"tileset/space_ship/Tiles/Tile ({0}).png"
    platforms_list = []
    platforms_list.append(Platform(path_platform,1,15,x=400,y=250,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=450,y=250,width=50,height=30,type=2))
    platforms_list.append(Platform(path_platform,1,15,x=600,y=250,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=650,y=250,width=50,height=30,type=2))
    platforms_list.append(Platform(path_platform,1,15,x=800,y=250,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=850,y=250,width=50,height=30,type=2))
    platforms_list.append(Platform(path_platform,1,15,x=1000,y=250,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=1050,y=250,width=50,height=30,type=2))
    platforms_list.append(Platform(path_platform,1,15,x=350,y=400,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=400,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=450,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=500,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=550,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=600,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=650,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=700,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=750,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=800,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=850,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=900,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=950,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=1000,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=1050,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=1100,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=1150,y=400,width=50,height=30,type=2))

    items_list = []
    items_list.append(Item(path_ruby,0,2,x=415,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=465,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=1015,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=1065,y=300,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=400,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=450,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=500,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=550,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=600,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=650,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=700,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=750,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=800,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=850,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=900,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=950,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=1000,y=450,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=450,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=500,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=550,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=600,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=650,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=700,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=750,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=800,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=850,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=900,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=950,y=80,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=1000,y=80,width=25,height=25))
    
    bullets_list = []

    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                flag = False
                sys.exit()
            if event.type == event_time_1000_ms:
                time_game -= 1
            if event.type == event_time_shoot_5000_ms:
                for enemy in enemy_list:
                    if not enemy.is_dead:
                        if enemy.direction == DIRECTION_RIGHT:
                            bullets_list.append(Bullet(enemy,enemy.rect.centerx,enemy.rect.centery,player.rect.centerx,player.rect.centery,2,IMAGE_PATH+"images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",100,5,5,5))
                        else:
                            bullets_list.append(Bullet(enemy,enemy.rect.centerx,enemy.rect.centery,player.rect.centerx,player.rect.centery,2,IMAGE_PATH+"images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",100,5,5,5))
                    
        keys = pygame.key.get_pressed()
                        
        delta_ms = clock.tick(FPS)
                
        SCREEN.blit(background,(0,0))        
                    
        for platform in platforms_list:
            platform.draw(SCREEN)
            
        for item in items_list:
            item.update(delta_ms)
            item.draw(SCREEN)
            
            if(player.rect.colliderect(item.rect_collition)):
                items_list.remove(item)
                player.score += 10
                item_sound.play()
                
                
        for bullet in bullets_list:
            bullet.update(delta_ms,platforms_list,enemy_list,player)
            bullet.draw(SCREEN)
            
        for enemy in enemy_list:     
            enemy.update(delta_ms,platforms_list,bullets_list)
            enemy.draw(SCREEN)
            if not enemy.is_dead:
                if(player.rect.colliderect(enemy.collition_rect)):
                    player.energy -= 0.5
                    player_sound.play()
        
        player.events(delta_ms,keys,bullets_list,arrow_sound)
        player.update(delta_ms,platforms_list) 
        player.draw(SCREEN)
        
        
        draw_text (SCREEN, str("Time = {0}".format(time_game)), 30, SCREEN_WIDTH -SCREEN_WIDTH+100, 10)
        draw_text (SCREEN, str("Score = {0}".format(player.score)), 30, SCREEN_WIDTH // 2, 10)
        draw_player_energy(SCREEN,SCREEN_WIDTH -250,10,player.energy)
        
        if time_game <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            time_up()
            
        elif player.energy <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            loser()
            
        elif items_list == [] and enemy.energy <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            winner()
                    
        pygame.display.flip()
    
def stage_3():
    flag = True
    time_game = 50

    event_time_1000_ms = pygame.USEREVENT
    pygame.time.set_timer(event_time_1000_ms,1000)

    event_time_shoot_2000_ms = pygame.USEREVENT +1
    pygame.time.set_timer(event_time_shoot_2000_ms,5000)
    
    clock = pygame.time.Clock()
    background = pygame.image.load("extras/bg_3.png")
    background = pygame.transform.scale(background, SCREEN_SIZE)

    pygame.mixer.set_num_channels(8)
    pygame.mixer.music.load(IMAGE_PATH+"sounds/Insane-Gameplay.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    item_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/coin.mp3")
    player_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/CHILD6.mp3")
    arrow_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/throw.mp3")
                                
    player = Player(x=SCREEN_WIDTH-SCREEN_WIDTH+25,y=GROUND_LEVEL,speed_walk=25,speed_run=50,gravity=20,frame_rate_ms=50,move_rate_ms=50,jump_power=100,jump_height=120,p_scale=0.22)

    enemy_list = []
    enemy_list.append (Enemy_2(x=600,y=380,speed_walk=8))
    enemy_list.append (Enemy_4(x=10,y=200,speed_walk=15))
    
    
    dynamic_platforms_list = []
    dynamic_platforms_list.append(Dynamic_platform(x=550,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=600,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=650,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=700,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=750,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=800,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=850,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=950,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    dynamic_platforms_list.append(Dynamic_platform(x=1000,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    dynamic_platforms_list.append(Dynamic_platform(x=1050,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    dynamic_platforms_list.append(Dynamic_platform(x=1100,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    dynamic_platforms_list.append(Dynamic_platform(x=1150,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    dynamic_platforms_list.append(Dynamic_platform(x=550,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=600,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=650,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=700,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=750,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=800,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=850,y=250,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    
    items_list = []
    items_list.append(Item(path_sapphire,0,2,x=450,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=500,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=550,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=600,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=650,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=700,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=750,y=300,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=450,y=150,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=500,y=150,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=550,y=150,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=600,y=150,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=650,y=150,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=700,y=150,width=25,height=25))
    items_list.append(Item(path_moonstone,0,2,x=750,y=150,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=100,y=200,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=150,y=200,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=200,y=200,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=950,y=200,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=1000,y=200,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=1050,y=200,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=1100,y=200,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=1150,y=200,width=25,height=25))

    bullets_list = []

    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                flag = False
                sys.exit()
            if event.type == event_time_1000_ms:
                time_game -= 1
            if event.type == event_time_shoot_2000_ms:
                for enemy in enemy_list:
                    if not enemy.is_dead:
                        if enemy.direction == DIRECTION_RIGHT:
                            bullets_list.append(Bullet(enemy,enemy.rect.centerx,enemy.rect.centery,player.rect.centerx,player.rect.centery,2,IMAGE_PATH+"images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",100,5,5,5))
                        else:
                            bullets_list.append(Bullet(enemy,enemy.rect.centerx,enemy.rect.centery,player.rect.centerx,player.rect.centery,2,IMAGE_PATH+"images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",100,5,5,5))
                    
        keys = pygame.key.get_pressed()
                        
        delta_ms = clock.tick(FPS)
                
        SCREEN.blit(background,(0,0))        
                    
        for platform in dynamic_platforms_list:
            platform.update(delta_ms)
            platform.draw(SCREEN)  
            
        for item in items_list:
            item.update(delta_ms)
            item.draw(SCREEN)
            
            if(player.rect.colliderect(item.rect_collition)):
                items_list.remove(item)
                player.score += 10
                item_sound.play()
                
                
        for bullet in bullets_list:
            bullet.update(delta_ms,dynamic_platforms_list,enemy_list,player)
            bullet.draw(SCREEN)
            
        for enemy in enemy_list:     
            enemy.update(delta_ms,dynamic_platforms_list,bullets_list)
            enemy.draw(SCREEN)
            if not enemy.is_dead:
                if(player.rect.colliderect(enemy.collition_rect)):
                    player.energy -= 0.5
                    player_sound.play()            
        
        player.events(delta_ms,keys,bullets_list,arrow_sound)
        player.update(delta_ms,dynamic_platforms_list) 
        player.draw(SCREEN)
        
        
        draw_text (SCREEN, str("Time = {0}".format(time_game)), 30, SCREEN_WIDTH -SCREEN_WIDTH+100, 10)
        draw_text (SCREEN, str("Score = {0}".format(player.score)), 30, SCREEN_WIDTH // 2, 10)
        draw_player_energy(SCREEN,SCREEN_WIDTH -250,10,player.energy)
        
        if time_game <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            time_up()
            
        elif player.energy <= 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            loser()
            
        elif enemy.lives == 0:
            flag = False
            stage_flag_1 = True
            pygame.mixer.music.stop()
            winner()
                    
        pygame.display.flip()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Aca deberian estar las opciones!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(600, 400), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        
def winner():
    pygame.mixer.music.load(IMAGE_PATH+"sounds/victory.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(100).render("YOU WIN!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(600, 400), 
                            text_input="BACK TO STAGES", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    stages()

        pygame.display.update()
        
def loser():
    pygame.mixer.music.load(IMAGE_PATH+"sounds/game_over.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(100).render("YOU LOSE!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(600, 400), 
                            text_input="BACK TO STAGES", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    stages()

        pygame.display.update()
        
def time_up():
    pygame.mixer.music.load(IMAGE_PATH+"sounds/time_up.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(100).render("TIME UP!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(600, 400), 
                            text_input="BACK TO STAGES", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    stages()

        pygame.display.update()

def stages():
    pygame.mixer.music.stop()
    while True:
        SCREEN.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("STAGES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        STAGE_1_BUTTON = Button(image=pygame.image.load("assets/stage_rect.png"), pos=(600, 200), 
                            text_input="STAGE_1", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        STAGE_2_BUTTON = Button(image=pygame.image.load("assets/stage_rect.png"), pos=(600, 270), 
                            text_input="STAGE_2", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        STAGE_3_BUTTON = Button(image=pygame.image.load("assets/stage_rect.png"), pos=(600, 340), 
                            text_input="STAGE_3", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        MAIN_BUTTON = Button(image=pygame.image.load("assets/stage_rect.png"), pos=(600, 410), 
                            text_input="MAIN", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit_Rect_Small.png"), pos=(600, 480), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [STAGE_1_BUTTON, STAGE_2_BUTTON, STAGE_3_BUTTON, MAIN_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STAGE_1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stage_1()
                if STAGE_2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stage_2()
                    # if stage_flag_1 == True:
                    #     pass
                    # else:
                    #     MENU_TEXT = get_font(10).render("you must complete previous stage!", True, "#b68f40")
                    #     MENU_RECT = MENU_TEXT.get_rect(center=(950, 300))
                    #     SCREEN.blit(MENU_TEXT, MENU_RECT)
                if STAGE_3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stage_3()
                if MAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()                    
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(600, 200), 
                            text_input="STAGES", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(600, 350), 
                            text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(600, 500), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stages()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
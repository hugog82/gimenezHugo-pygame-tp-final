import pygame, sys, sqlite3
from constants import *
from player import Player
from auxiliar import *
from enemy import Enemy
from class_platform import Platform
from level_1 import *
from score import *
from bullet import *
    
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
flag = True
time_game = 50

event_time_1000_ms = pygame.USEREVENT
pygame.time.set_timer(event_time_1000_ms,1000)

event_time_shoot_2000_ms = pygame.USEREVENT +1
pygame.time.set_timer(event_time_shoot_2000_ms,5000)

clock = pygame.time.Clock()

background = pygame.image.load("Assets/bg.jpg")
background = pygame.transform.scale(background, SCREEN_SIZE)

pygame.mixer.set_num_channels(8)
pygame.mixer.music.load(IMAGE_PATH+"sounds/Street-Mayhem.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

item_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/coin.mp3")
player_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/CHILD6.mp3")
arrow_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/throw.mp3")
victory_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/victory.mp3")
game_over_sound = pygame.mixer.Sound(IMAGE_PATH+"sounds/game_over.mp3")

player = Player(name="Hugo",x=SCREEN_WIDTH/2,y=GROUND_LEVEL,speed_walk=25,speed_run=50,gravity=20,frame_rate_ms=50,move_rate_ms=50,jump_power=100,jump_height=120,p_scale=0.22)

    
enemy_list = get_enemy()
platforms_list = get_platform()
items_list = get_item()
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
    
    if time_game == 0:
        draw_text (SCREEN, str("TIME UP!"), 100, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        game_over_sound.play()
        
    elif player.energy <= 0:
        draw_text (SCREEN, str("YOU LOSE!"), 100, SCREEN_WIDTH // 2,SCREEN_HEIGHT//2)
        
    elif items_list == [] and enemy.energy <= 0:
        flag = False
        #score = player.score
        with open("score.css", "a") as archivo:
            archivo.write("Player,Score"  + "\n")
            archivo.write(str(player.name) + "," + str(player.score) + "\n")
            
    # enemies update
    # dibujar todo el nivel
                
    pygame.display.flip()
    
pygame.quit()

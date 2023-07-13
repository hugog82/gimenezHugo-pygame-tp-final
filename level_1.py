from class_platform import Platform
from item import Item
from constants import *
from auxiliar import *
from enemy import *


def get_background():
    bg = Background(0,0,SCREEN_SIZE,"assets/Background.png")
    
    return bg

path_platform = IMAGE_PATH+"tileset/forest/Tiles/{0}.png"

path_amber = IMAGE_PATH+"coin/gem_amber/gem_amber_{0}.png"
path_diamond = IMAGE_PATH+"coin/gem_diamond/gem_diamond_{0}.png"
path_moonstone = IMAGE_PATH+"coin/gem_moonstone/gem_moonstone_{0}.png"
path_ruby = IMAGE_PATH+"coin/gem_ruby/gem_ruby_{0}.png"
path_sapphire = IMAGE_PATH+"coin/gem_sapphire/gem_sapphire_{0}.png"

def get_platform ():
        
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
    
    return platforms_list


def get_item ():
        
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
  
    
    return items_list

def get_enemy():
    
    enemy_list = []
    enemy_list.append (Enemy(x=200,y=452,speed_walk=8,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))
    enemy_list.append (Enemy(x=1000,y=452,speed_walk=8,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))

    return enemy_list
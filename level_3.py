from dynamic_platf import Dynamic_platform
from item import Item
from constants import *
from auxiliar import *
from enemy import *
from background import Background


def get_background():
    bg = Background(0,0,SCREEN_SIZE,"extras/bg_3.png")
    
    return bg

path_platform = IMAGE_PATH+"tileset/space_ship/Tiles/Tile ({0}).png"

path_amber = IMAGE_PATH+"coin/gem_amber/gem_amber_{0}.png"
path_diamond = IMAGE_PATH+"coin/gem_diamond/gem_diamond_{0}.png"
path_moonstone = IMAGE_PATH+"coin/gem_moonstone/gem_moonstone_{0}.png"
path_ruby = IMAGE_PATH+"coin/gem_ruby/gem_ruby_{0}.png"
path_sapphire = IMAGE_PATH+"coin/gem_sapphire/gem_sapphire_{0}.png"


def get_dynamic_platform ():
        
    dynamic_platforms_list = []
    dynamic_platforms_list.append(Dynamic_platform(x=550,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=600,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=650,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=700,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=750,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=800,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))
    dynamic_platforms_list.append(Dynamic_platform(x=850,y=400,speed_move=10,frame_rate_ms=50,move_rate_ms=50,p_scale=0.15))

    # dynamic_platforms_list.append(Dynamic_platform(x=0,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    # dynamic_platforms_list.append(Dynamic_platform(x=50,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    # dynamic_platforms_list.append(Dynamic_platform(x=100,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    # dynamic_platforms_list.append(Dynamic_platform(x=150,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))
    # dynamic_platforms_list.append(Dynamic_platform(x=200,y=300,speed_move=0,frame_rate_ms=50,move_rate_ms=50,p_scale=0.18))

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


    return dynamic_platforms_list

def get_item ():
        
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
    
       
    return items_list

def get_enemy():
    
    enemy_list = []
    enemy_list.append (Enemy_2(x=600,y=380,speed_walk=8))
    enemy_list.append (Enemy_4(x=10,y=200,speed_walk=15))

    return enemy_list
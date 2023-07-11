from class_platform import Platform
from item import Item
from constants import *
from auxiliar import *
from enemy import *
from background import Background


def get_background():
    bg = Background(0,0,SCREEN_SIZE,"extras/bg_2.jpg")

    return bg


#levels_list = read_file("Progra y Labo I/VIDEOGAME/levels.json")

path_platform = IMAGE_PATH+"tileset/space_ship/Tiles/Tile ({0}).png"

path_amber = IMAGE_PATH+"coin/gem_amber/gem_amber_{0}.png"
path_diamond = IMAGE_PATH+"coin/gem_diamond/gem_diamond_{0}.png"
path_moonstone = IMAGE_PATH+"coin/gem_moonstone/gem_moonstone_{0}.png"
path_ruby = IMAGE_PATH+"coin/gem_ruby/gem_ruby_{0}.png"
path_sapphire = IMAGE_PATH+"coin/gem_sapphire/gem_sapphire_{0}.png"


def get_platform ():
        
    platforms_list = []
    platforms_list.append(Platform(path_platform,1,15,x=0,y=250,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=50,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=100,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=150,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=250,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=200,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=250,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=300,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=350,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=400,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=450,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=500,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=550,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=600,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=650,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=700,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=750,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=800,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=850,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=900,y=250,width=50,height=30,type=2))
    platforms_list.append(Platform(path_platform,1,15,x=950,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=1000,y=250,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=1050,y=250,width=50,height=30,type=2))
    

    platforms_list.append(Platform(path_platform,1,15,x=100,y=400,width=50,height=30,type=0))
    platforms_list.append(Platform(path_platform,1,15,x=150,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=250,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=200,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=250,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=300,y=400,width=50,height=30,type=1))
    platforms_list.append(Platform(path_platform,1,15,x=350,y=400,width=50,height=30,type=1))
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

    return platforms_list

def get_item ():
        
    items_list = []
    items_list.append(Item(path_sapphire,0,2,x=150,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=200,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=250,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=300,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=350,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=400,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=450,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=500,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=550,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=600,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=650,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=700,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=750,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=800,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=850,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=900,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=950,y=300,width=25,height=25))
    items_list.append(Item(path_ruby,0,2,x=1000,y=300,width=25,height=25))
    items_list.append(Item(path_sapphire,0,2,x=1050,y=300,width=25,height=25))
    


    items_list.append(Item(path_amber,0,2,x=150,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=200,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=250,y=450,width=25,height=25))
    items_list.append(Item(path_diamond,0,2,x=300,y=450,width=25,height=25))
    items_list.append(Item(path_amber,0,2,x=350,y=450,width=25,height=25))
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
    
       
    return items_list

def get_enemy():
    
    enemy_list = []
    enemy_list.append (Enemy_2(x=1100,y=GROUND_LEVEL,speed_walk=10,speed_run=16,gravity=8,frame_rate_ms=50,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=0.07))
    enemy_list.append (Enemy_3(x=200,y=50,speed_walk=8,speed_run=16))

    return enemy_list
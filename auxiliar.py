import pygame
import json

def draw_text (surface, text, size, x, y):
    font = pygame.font.SysFont("Verdana", size, True, True)
    text_surface = font.render(text, True, "white")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

def draw_player_energy(surface, x,y,percentage):
    BAR_LENGHT = 200
    BAR_HEIGHT = 15
    fill = (percentage/100) * BAR_LENGHT
    border = pygame.Rect(x,y,BAR_LENGHT,BAR_HEIGHT)
    fill = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surface,"green",fill)
    pygame.draw.rect(surface,"white",border,2)

def read_file (nombre_archivo:str)->list:
    '''
    - Lee un arhivo de tipo json.
    - Recibe una cadena con la extension json por parametro.
    - Retorna la lista que contiene el archivo.
    - Retorna -1 si la lista esta vacia o el path es incorrecto.
    - Retorna -2 si la extension es incorrecta.
    '''
    retorno = -1
    
    try:
        lista= []
        with open(nombre_archivo, "r") as archivo:
            dict = json.load(archivo)
            lista = dict["levels"]
            retorno = lista
    except FileNotFoundError as error_archivo_no_encontrado:
        print(error_archivo_no_encontrado)
        retorno
    except json.JSONDecodeError:
        retorno = -2
        
    return retorno



class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet (path,columns,rows,flip=False, step=1):
        list = []
        surface_image = pygame.image.load(path).convert_alpha()
        frame_witdh = int(surface_image.get_width()/columns)
        frame_height = int(surface_image.get_height()/rows)
        x = 0
        
        for row in range(rows):
            for column in range(0, columns, step):
                x = column * frame_witdh
                y = row * frame_height
                frame_surface = surface_image.subsurface(x, y, frame_witdh, frame_height)
                if (flip):
                    frame_surface = pygame.transform.flip(frame_surface, True, False)
                list.append(frame_surface)
        return list
    
    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        list = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            frame_surface = pygame.image.load(path)
            frame_width_scaled = int(frame_surface.get_rect().w * scale)
            frame_height_scaled = int(frame_surface.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                frame_surface = pygame.transform.scale(frame_surface,(w, h)).convert_alpha()
            if(scale != 1):
                frame_surface = pygame.transform.scale(frame_surface,(frame_width_scaled, frame_height_scaled)).convert_alpha() 
            if(flip):
                frame_surface = pygame.transform.flip(frame_surface,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                list.append(frame_surface)
        return list
    


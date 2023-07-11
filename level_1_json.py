import pygame
import json

# Inicializar pygame
pygame.init()

# Definir una clase para la plataforma
class Platform:
    def __init__(self, x, y, width, height, platform_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.platform_type = platform_type

# Crear una lista de plataformas
platforms_list = []
platforms_list.append(Platform(x=50,y=250,width=50,height=30,platform_type=12))
platforms_list.append(Platform(x=100,y=250,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=150,y=250,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=200,y=250,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=250,y=250,width=50,height=30,platform_type=14))
platforms_list.append(Platform(x=900,y=250,width=50,height=30,platform_type=12))
platforms_list.append(Platform(x=950,y=250,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=1000,y=250,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=1050,y=250,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=1100,y=250,width=50,height=30,platform_type=14))

platforms_list.append(Platform(x=450,y=200,width=50,height=30,platform_type=12))
platforms_list.append(Platform(x=500,y=200,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=550,y=200,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=600,y=200,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=650,y=200,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=700,y=200,width=50,height=30,platform_type=14))

platforms_list.append(Platform(x=380,y=350,width=50,height=30,platform_type=12))
platforms_list.append(Platform(x=430,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=480,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=530,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=580,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=630,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=680,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=730,y=350,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=780,y=350,width=50,height=30,platform_type=14))

platforms_list.append(Platform(x=50,y=400,width=50,height=30,platform_type=12))
platforms_list.append(Platform(x=100,y=400,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=150,y=400,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=200,y=400,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=250,y=400,width=50,height=30,platform_type=14))
platforms_list.append(Platform(x=900,y=400,width=50,height=30,platform_type=12))
platforms_list.append(Platform(x=950,y=400,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=1000,y=400,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=1050,y=400,width=50,height=30,platform_type=13))
platforms_list.append(Platform(x=1100,y=400,width=50,height=30,platform_type=14))

# Crear una lista para almacenar los datos de las plataformas
platforms_data = []

# Convertir cada objeto de plataforma a un diccionario
for platform in platforms_list:
    platform_data = {
        "x": platform.x,
        "y": platform.y,
        "width": platform.width,
        "height": platform.height,
        "platform_type": platform.platform_type
    }
    platforms_data.append(platform_data)

# Convertir la lista de plataformas a formato JSON
json_data = json.dumps(platforms_data)

# Guardar el JSON en un archivo
with open("Progra y Labo I/VIDEOGAME/platforms.json", "w") as file:
    file.write(json_data)

# Finalizar pygame
pygame.quit()
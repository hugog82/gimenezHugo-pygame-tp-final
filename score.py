import pygame

def draw_text (surface, text, size, x, y):
    font = pygame.font.SysFont("arial", size, True, True)
    text_surface = font.render(text, True, "white")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)
    
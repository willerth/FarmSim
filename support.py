import pygame
from os import walk

def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for img in img_files:
            full_path = f'path/{img}'
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    
    return surface_list
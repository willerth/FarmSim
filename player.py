import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        #movement
        self.direction = pygame.math.Vector2(0,0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_hoe': [], 'down_hoe': [], 'left_hoe': [], 'right_hoe': [],
                           'up_axe': [], 'down_axe': [], 'left_axe': [], 'right_axe': [],
                           'up_water': [], 'down_water': [], 'left_water': [], 'right_water': []}
        
        for animation in self.animations.keys():
            full_path = f'../graphics/character/{animation}'
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]

    
    def move(self, dt):
        if self.direction.magnitude(): self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        

    def update(self, dt):
        self.input()
        self.move(dt)
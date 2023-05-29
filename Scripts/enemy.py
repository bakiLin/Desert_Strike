import pygame
import random
from config import *
from os import path

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = enemy_speed
        
        self.image = pygame.image.load(path.join('img', 'enemy.png')).convert()
        self.image.set_colorkey(RED)

        self.rect = self.image.get_rect()
        self.spawn()

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT: self.kill()

    def spawn(self):
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = 10

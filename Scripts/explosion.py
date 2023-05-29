import pygame
import math
from config import *
from os import path

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.set_sprite()
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.animation_loop = 0
        self.animate()

    def set_sprite(self):
        self.animation = []
        for i in range(1, 5):
            filename = 'explosion0{}.png'.format(i)
            img = pygame.image.load(path.join('img', filename)).convert()
            img_scaled = pygame.transform.scale(img, (EXPLOSION_SIZE, EXPLOSION_SIZE))
            self.animation.append(img_scaled)

    def update(self):
        self.animate()

    def animate(self):
        self.image = self.animation[math.floor(self.animation_loop)]
        self.image.set_colorkey(BLACK)
        self.animation_loop += EXPLOSION_SPEED

        if self.animation_loop >= 4:
            self.kill()

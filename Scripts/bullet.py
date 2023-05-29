import pygame
from config import *
from explosion import *
from os import path

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.image = pygame.image.load(path.join('img', 'bullet.png')).convert()
        self.image.set_colorkey(BLUE)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.groupcollide(self.game.enemies, self.game.bullets, True, True):
            self.game.score += 1
            self.rect.centery -= EXPLOSION_OFFSET
            explosion = Explosion(self.rect.center)
            self.game.all_sprites.add(explosion)    
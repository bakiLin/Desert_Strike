import pygame
import math
from config import *
from bullet import *
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        
        self.game = game
        self.image = pygame.image.load(path.join('img', 'tank.png')).convert()
        self.image.set_colorkey(RED)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 16

        self.animation_loop = 0

        self.shoot_delay = SHOOT_DELAY
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.collide()
        self.movement()
        self.borders()

    def movement(self):
        speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: speed = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]: speed = PLAYER_SPEED
        if keys[pygame.K_SPACE]: self.shoot()
        self.rect.x += speed

    def borders(self):
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0: self.rect.left = 0

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits: 
            self.game.on = False
            self.game.over = True

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.game, self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.game.bullets.add(bullet)
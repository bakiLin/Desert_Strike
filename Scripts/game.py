from player import *
from enemy import *
from os import path

class Game():
    def __init__(self):
        self.set_base()
        self.set_groups()

        self.player = None
        self.running = True
        self.menu = True
        self.on = False
        self.over = False

        self.frames = 0
        self.spawn_rate = 120   
        self.enemy_speed = 2
        self.score = 0

        self.background = pygame.image.load('img/bg.png')
        self.background_rect = self.background.get_rect() 

        self.create_player()

    def set_base(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Turret')
        self.clock = pygame.time.Clock()
    
    def set_groups(self):
        self.all_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def new(self):
        while self.running:
            self.clock.tick(FPS)
            if self.menu: 
                self.menu_screen()
            if self.on:
                self.game_on()
            if self.over:
                self.game_over()
        pygame.quit()
        
    def menu_screen(self):
        self.screen.blit(self.background, self.background_rect)
        self.draw_text(self.screen, "Desert Strike", 70, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(self.screen, "arrow keys to move", 35, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 - 5)
        self.draw_text(self.screen, "space key to fire", 35, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + 20)
        self.draw_text(self.screen, "Press any Key to Start", 50, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            if event.type == pygame.KEYDOWN:
                self.menu = False
                self.on = True

    def game_on(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
        self.spawn_enemy()
        self.screen.blit(self.background, self.background_rect)
        self.display_text()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        self.all_sprites.update()

    def game_over(self):
        self.screen.blit(self.background, self.background_rect)
        self.draw_text(self.screen, "Game Over", 70, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(self.screen, f"your score is {self.score}", 35, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        self.draw_text(self.screen, "Press any Key to Start", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + 70)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            if event.type == pygame.KEYDOWN:
                self.over = False
                self.on = True

                for sprite in self.all_sprites: sprite.kill()
                for sprite in self.player_sprite: sprite.kill()
                for sprite in self.enemies: sprite.kill()
                for sprite in self.bullets: sprite.kill()

                self.create_player()
                self.clear_values()

    def clear_values(self):
        self.frames = 0
        self.spawn_rate = 120   
        self.enemy_speed = 2
        self.score = 0

    def create_player(self):
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.player_sprite.add(self.player)

    def spawn_enemy(self):
        self.frames += 1
        if self.frames == self.spawn_rate:
            self.create_enemy()
            self.enemy_speed += 0.1
            if self.spawn_rate != SPAWN_RATE: self.spawn_rate -= 2
            self.frames = 0

    def create_enemy(self):
        enemy = Enemy(self.enemy_speed)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font('EightBits.ttf', size)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def display_text(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.score), 70, SCREEN_WIDTH / 2,   10)
    
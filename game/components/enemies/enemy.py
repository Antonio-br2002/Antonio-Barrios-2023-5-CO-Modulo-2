import pygame
import random

from pygame.sprite import Sprite
from game.components.bullets.bullets import Bullet
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_2


class Enemy(Sprite):
    ENEMY_WIDTH = 46
    ENEMY_HEIGHT= 60
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 1000]
    Y_POS = 20
    SPEED_X = 5
    SPEED_X_ENEMY2 = 10
    SPEED_y_ENEMY2 = 2
    SPEED_y = 1
    MOV_X = { 0: 'left', 1: 'right'}
    LIST_ENEMYS = [ENEMY_1, ENEMY_2] 

    def __init__(self):
        self.choice_enemys = random.choice(self.LIST_ENEMYS)
        self.image = pygame.transform.scale(random.choice(self.LIST_ENEMYS), (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = pygame.time.get_ticks() + random.randint(500, 1000)  # Momento de próximo disparo
        
        
        if self.choice_enemys == ENEMY_2:
            self.speed_x = self.SPEED_X_ENEMY2
            self.speed_y = self.SPEED_y_ENEMY2
            #self.chose_enemys = random.choice(self.LIST_ENEMYS)

            
        
        
            

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))



    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0
            
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet.speed_y = bullet.SPEED  
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)
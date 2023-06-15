from typing import Any
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullets import Bullet
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT// 2
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500
    
    def __init__(self,spaceship_type):
        super().__init__()
        self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = spaceship_type
        self.shoot_delay = 0.5    
        self.last_shot_time = 0
             
    def update(self, user_input):
        if user_input[pygame. K_LEFT]:
            self.move_left()
        elif user_input[pygame. K_RIGHT]:
            self.move_right()
        elif user_input[pygame. K_UP]:
            self.move_up()
        elif user_input[pygame. K_DOWN]:
            self.move_down()
        elif user_input[pygame. K_SPACE]:
            self.shoot()
        
        current_time = pygame.time.get_ticks()
        if user_input[pygame.K_SPACE] and current_time - self.last_shot_time > self.shoot_delay * 1000:
            self.shoot(self.bullet_manager)
            self.last_shot_time = current_time
        
            
    def move_left(self):
        self.rect.x -= 10
        if self.rect.left <= 0:
            self.rect.right = SCREEN_WIDTH 
        
    def move_right(self):
        self.rect.x += 10
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.left = 0
        
    def move_up(self):
        if self.rect.y > self.HALF_SCREEN_HEIGHT:
            self.rect.y -= 10
        
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGHT:
            self.rect.y += 10
            
    def shoot(self, bullet_manager):
            bullet = Bullet(self)
            bullet.speed_y = -10  # Velocidad vertical hacia arriba
            bullet_manager.add_bullet(bullet)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIELD_TYPE

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.stop_time = 0
        self.is_stopped = False

    def update(self, game):
        self.add_enemy()
        if self.is_stopped:
            current_time = pygame.time.get_ticks()
            if current_time > self.stop_time:
                self.resume_enemies()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

            if enemy.rect.colliderect(game.player.rect):
                if not game.player.has_power_up or game.player.power_up_type != SHIELD_TYPE:
                    game.death_count.update()
                    game.playing = False
                    pygame.time.delay(1000)
                    break

    
    def stop_enemies(self):
        for enemy in self.enemies:
            enemy.speed_x = 0
            enemy.speed_y = 0
            enemy.shooting_time += 4000 
        self.stop_time = pygame.time.get_ticks() + 4000
        self.is_stopped = True
        
    def resume_enemies(self):
        for enemy in self.enemies:
            enemy.speed_x = Enemy.SPEED_X
            enemy.speed_y = Enemy.SPEED_y
            enemy.shooting_time -= 4000

        self.is_stopped = False

    def draw(self, screen):
      for enemy in self.enemies:
          enemy.draw(screen)

    def add_enemy(self):
      if len(self.enemies) < 3:
        enemy = Enemy()
        self.enemies.append(enemy)
    
    def reset(self):
      self.enemies = []

      
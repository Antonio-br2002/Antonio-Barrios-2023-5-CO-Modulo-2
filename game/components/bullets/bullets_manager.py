import pygame

from game.utils.constants import SHIELD_TYPE, EXPLOSION, DISPARO_MUSIC


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.explosion_pos = None
        self.explosion_time = 0
        self.disparo_sound = pygame.mixer.Sound(DISPARO_MUSIC)
    
    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)
            
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.create_explosion(enemy.rect.center)
                    game.score.update()

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_count.update()
                    game.playing = False
                    pygame.time.delay(1000)
                    break
  
        current_time = pygame.time.get_ticks()
        if self.explosion_pos is not None and current_time - self.explosion_time >= 500:
            self.explosion_pos = None

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)
            
        if self.explosion_pos is not None:
            explosion_rect = EXPLOSION.get_rect(center=self.explosion_pos)
            screen.blit(EXPLOSION, explosion_rect)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

    def create_explosion(self, position):
        self.explosion_pos = position
        self.explosion_time = pygame.time.get_ticks()

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
        self.explosion_pos = None
        self.explosion_time = 0

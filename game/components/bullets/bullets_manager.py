import pygame

class BulletsManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullest = []
        
    def update(self, game):
        for bullet in self.enemy_bullest:
            bullet.update(self.enemy_bullest)
            
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullest.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
            
    def draw(self, screen):
        for bullet in self.enemy_bullest:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullest) < 1:
            self.enemy_bullest.append(bullet)
        
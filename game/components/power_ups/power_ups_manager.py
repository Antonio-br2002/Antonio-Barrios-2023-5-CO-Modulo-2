import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.power_stop import PowerUpStopEnemies
from game.utils.constants import SPACESHIP_SHIELD

class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000
    
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(self.MIN_TIME_POWER_UP, self.MIN_TIME_POWER_UP)
        self.duration = random.randint(3, 5)
        
    def generate_power_up(self):
        power_up = random.choice([PowerUpStopEnemies(), Shield()])
        self.when_appears += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(power_up)
    
    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)

                if isinstance(power_up, PowerUpStopEnemies):
                    game.enemy_manager.stop_enemies()
                    self.power_ups.remove(power_up)
                    game.power_up_sound.play()
                else:
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
                    game.power_up_sound.play()
            

                
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.MIN_TIME_POWER_UP, now + self.MAX_TIME_POWER_UP)

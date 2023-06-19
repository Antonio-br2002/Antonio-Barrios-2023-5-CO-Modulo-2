import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import POWER_UP_STOP

class PowerUpStopEnemies(PowerUp):
    def __init__(self):
        super().__init__(POWER_UP_STOP, 'stop')
        self.image = pygame.transform.scale(self.image, (65, 75))
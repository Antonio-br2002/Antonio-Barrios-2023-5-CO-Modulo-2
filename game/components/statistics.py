import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Statistics:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    
    def __init__(self):
        self.score = 0
        self.death_count = 0
        self.highest_score = 0
        self.font = pygame.font.Font(FONT_STYLE, 30)
    
    def score_increase(self):
        self.score += 1
    
    def number_of_deaths(self):
        self.death_count += 1
    
    def score_level(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            
    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        death_count_text = self.font.render(f'Death Count: {self.death_count}', True, (255, 255, 255))
        highest_score_text = self.font.render(f'Highest Score: {self.highest_score}', True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(death_count_text, (10, 50))
        screen.blit(highest_score_text, (10, 90))
    
    def draw2(self, screen):
        separation = 40
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        death_count_text = self.font.render(f'Death Count: {self.death_count}', True, (255, 255, 255))
        highest_score_text = self.font.render(f'Highest Score: {self.highest_score}', True, (255, 255, 255))

        score_rect = score_text.get_rect(center=(self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + separation))
        death_count_rect = death_count_text.get_rect(center=(self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + separation + 40))
        highest_score_rect = highest_score_text.get_rect(center=(self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + separation + 80))

        screen.blit(score_text, score_rect)
        screen.blit(death_count_text, death_count_rect)
        screen.blit(highest_score_text, highest_score_rect)

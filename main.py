import sys
import pygame
from settings import Settings
from ship import Ship


# создание экрана игры

class AlienInvation:
    """" класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """" инициирует игру"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invation")
        self.ship = Ship(self)
        # Назначение цвета фона.
       # self.bg_color = self.settings.bg_color

    def run_game(self):
        """" запуск основного цикла игры"""
        while True:
            #отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #перересовка экрана задоного цвета
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #отображение последнего прорисованного экрана
            pygame.display.flip()


ai = AlienInvation()
ai.run_game()
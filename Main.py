import Variables
from Game_window import *
from Setting_window import *
from Setting_befor_game_window import *
from Setting_in_game import *
from Main_window import *
import pygame
from Music import *


def main():
    pygame.init()
    pygame.display.set_caption('Labyrinth')
    Variables.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Variables.SCREEN_SIZE = Variables.SCREEN_HEIGHT, Variables.SCREEN_WIDTH = [Variables.screen.get_height(),
                                                                               Variables.screen.get_width()]
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    '''Я предлагаю основной цикл реализовать в этом файле, а при обновлении приложения вызывать соответствующие 
    методы из каждого класса'''
    Variables.window = MainWindow()
    running = True
    '''Чтобы реализовать полиморфизм и при этом не делать лишних перерисовок, окно настроек и полная отрисовка игрового
    поля будет в этом методе, а частичное обновление игрового поля будет в методе update()'''
    Variables.window.first_update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            '''Реализовать методы в классах, которые будут вызываться при различных событиях'''

            if event.type == pygame.KEYDOWN:
                Variables.window.window_event(event.key)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                    #event.pos
        if Variables.CHANGE_WINDOW:
            change_window()
            Variables.CHANGE_WINDOW = False
        Variables.window.update()
        pygame.display.flip()
        clock.tick(Variables.FPS)
    pygame.quit()


def change_window():
    if Variables.name == 'Главное меню':
        Variables.window = MainWindow()
    elif Variables.name == 'Настройки':
        Variables.window = Setting()
    elif Variables.name == 'Предыгровое меню':
        Variables.window = Pre_game_setting()
    elif Variables.name == 'Игровое меню':
        Variables.window = Pre_game_setting()
    elif Variables.name == 'Игра':
        Variables.window = Pole([6, 5], 3)
    Variables.window.first_update()


if __name__ == '__main__':
    main()
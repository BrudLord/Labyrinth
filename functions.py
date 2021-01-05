from Game_window import *
from Setting_window import *
from Setting_befor_game_window import *
from Setting_in_game import *
from Main_window import *
import Variables as var


def change_window(name):
    if name == 'Главное меню':
        var.window = MainWindow()
    elif name == 'Настройки':
        var.window = Setting()
    elif name == 'Предыгровое меню':
        var.window = Pre_game_setting()
    elif name == 'Игровое меню':
        var.window = Pre_game_setting()
    elif name == 'Игра':
        var.window = Pole()
    var.window.first_update()

##MainWindow() #Pole([6, 5], 3)
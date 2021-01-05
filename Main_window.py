from Window import Pra_window
import Variables as var
import pygame
from Music import *
from functions import *

count = -1

def print_text(message, x, y, font_color=(0, 0, 0), font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text, (x, y))


class MainWindow(Pra_window):
    def __init__(self):
        pass

    def first_update(self):
        global count
        var.screen.fill((255, 255, 255))
        if count == 47:
            count = 0
        else:
            count += 1
        self.button = Button(70, 40)
        self.button2 = Button(70, 40)
        self.button3 = Button(70, 40)
        self.button4 = Button(70, 40)
        self.button5 = Button(70, 40)
        self.button6 = Button(20, 20)
        BackGround = Background('data\\' + str(count) + '.gif', [0, 0])
        var.screen.blit(BackGround.image, BackGround.rect)
        self.button.draw(20, 100, 'Играть')
        self.button2.draw(20, 150, "Испытания")
        self.button3.draw(20, 200, 'Настройки')
        self.button4.draw(20, 250, 'Профиль')
        self.button5.draw(20, 300, 'О игре')
        self.button6.draw(750, 30, '?')

    def update(self):
        global count
        var.screen.fill((255, 255, 255))
        if count == 47:
            count = 0
        else:
            count += 1
        BackGround = Background('data\\' + str(count) + '.gif', [0, 0])
        var.screen.blit(BackGround.image, BackGround.rect)
        self.button.draw(20, 100, 'Играть')
        self.button2.draw(20, 150, "Испытания")
        self.button3.draw(20, 200, 'Настройки')
        self.button4.draw(20, 250, 'Профиль')
        self.button5.draw(20, 300, 'О игре')
        self.button6.draw(750, 30, '?')


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (41, 150, 150)
        self.active_color = (9, 190, 150)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(var.screen, self.inactive_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(150)
                    if text == 'Играть':
                        change_window('Предыгровое меню')
            else:
                pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text(text, x + 5, y + 5)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.transform.scale(pygame.image.load(image_file), var.SCREEN_SIZE[::-1])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
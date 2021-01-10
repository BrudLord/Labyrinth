import pygame
import sqlite3
import keyboard


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

Flag = True
display_w = 800
display_h = 430
display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Maze')

con = sqlite3.connect('data_base.db')
cur = con.cursor()
pygame.mixer.music.load('data\\579b2fbcdd508f7.mp3')
pygame.mixer.music.set_volume(0.2)
button_sound = pygame.mixer.Sound('data\\00171.wav')
pygame.mixer.Sound.set_volume(button_sound, 0.2)

Main_flag = True
Pre_game_flag = False
game_flag = False
Settings_flag = False
Help_flag = False
About_game_flag = False
pygame.init()
COLOR_ACTIVE = pygame.Color(41, 150, 150)
COLOR_INACTIVE = pygame.Color(9, 190, 150)
FONT = pygame.font.Font(None, 32)
count = -1
advicex = True


def play():
    print(1)


def m():
    global Pre_game_flag
    global Main_flag
    global game_flag
    global Settings_flag
    global Help_flag
    global About_game_flag
    global done
    Main_flag = True
    Pre_game_flag = False
    game_flag = False
    Settings_flag = False
    Help_flag = False
    About_game_flag = False
    done = True



def p():
    global Pre_game_flag
    global Main_flag
    global game_flag
    global Settings_flag
    global Help_flag
    global About_game_flag
    Main_flag = False
    Pre_game_flag = True
    game_flag = False
    Settings_flag = False
    Help_flag = False
    About_game_flag = False


def s():
    global Pre_game_flag
    global Main_flag
    global game_flag
    global Settings_flag
    global Help_flag
    global About_game_flag
    global done
    Main_flag = False
    Pre_game_flag = False
    game_flag = False
    Settings_flag = True
    Help_flag = False
    About_game_flag = False
    done = True

def h():
    global Pre_game_flag
    global Main_flag
    global game_flag
    global Settings_flag
    global Help_flag
    global About_game_flag
    global done
    Main_flag = False
    Pre_game_flag = True
    game_flag = False
    Settings_flag = False
    Help_flag = True
    About_game_flag = False
    done = True

def a():
    global Pre_game_flag
    global Main_flag
    global game_flag
    global Settings_flag
    global Help_flag
    global About_game_flag
    Main_flag = False
    Pre_game_flag = False
    game_flag = False
    Settings_flag = False
    Help_flag = False
    About_game_flag = True


def advice():
    global advicex
    if advicex is True:
        advicex = False
        print(12)
    elif advicex is False:
        advicex = True
        print(21)


def Hot_key():
    global Flag
    if Flag == True:
        pygame.mixer.music.pause()
        Flag = False
    else:
        pygame.mixer.music.unpause()
        Flag = True


keyboard.add_hotkey('p', Hot_key)



def print_text(message, x, y, font_color=(0, 0, 0), font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


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
                pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(150)
                    if action != None:
                        action()
            else:
                pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))

        else:
            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))


        print_text(text, x + 5, y + 5)


class MainWindow:
    def __init__(self):
        pass

    def first_update(self):
        global count
        global Flag
        display.fill((255, 255, 255))
        if count == 47:
            count = 0
        else:
            count += 1
        button = Button(70, 40)
        button2 = Button(70, 40)
        button3 = Button(70, 40)
        button4 = Button(70, 40)
        button5 = Button(70, 40)
        button6 = Button(20, 20)
        BackGround = Background('data\\' + str(count) + '.gif', [0, 0])
        display.blit(BackGround.image, BackGround.rect)
        button.draw(20, 100, 'Играть', p)
        button2.draw(20, 150, "Испытания")
        button3.draw(20, 200, 'Настройки', s)
        button4.draw(20, 250, 'Профиль')
        button5.draw(20, 300, 'О игре')
        button6.draw(750, 30,  '?', h)
        pygame.display.update()


class Settings:
    def __init__(self):
        pass


    def first_update(self):
        global done
        done = False
        global advice
        button = Button(80, 40)
        button_set = Button(80, 40)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quit()
            display.fill((30, 30, 30))
            button.draw(10, 360, 'Назад в меню', m)
            button_set.draw(10, 30, 'Подсказки', advice)
            if advicex is True:
                print_text('Подсказки включены', 100, 40, (0, 200, 140), font_size=20)
            else:
                print_text('Подсказки выключены', 100, 40, (0, 200, 140), font_size=20)
            pygame.display.update()



class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Help:
    def __init__(self):
        pass


    def first_update(self):
        global done
        done = False
        button = Button(80, 40)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quit()
            display.fill((30, 30, 30))
            print_text('Цель игры - вам необходимо как можно быстрее добраться до финиша', 10, 30, (60, 140, 190), font_size=20)
            print_text('Особенности:', 10, 60, (60, 140, 190), font_size=20)
            print_text('В лабиринте присутсвтуют двери разных цветов', 10, 90, (60, 140, 190), font_size=20)
            print_text('игрок может проходить только через двери своего цвета.', 10, 120, (60, 140, 190), font_size=20)
            print_text('При проходе через дверь например,', 10, 150, (60, 140, 190), font_size=20)
            print_text('красного', 195, 150, (250, 10, 10), font_size=20)
            print_text('цвета, игрок,', 245, 150, (60, 140, 190), font_size=20)
            print_text('красного', 185, 180, (250, 10, 10), font_size=20)
            print_text('При наличии в данный момент', 10, 180, (60, 140, 190), font_size=20)
            print_text('поменяет его например на', 235, 180, (60, 140, 190), font_size=20)
            print_text('зеленый', 385, 180, (10, 250, 10), font_size=20)
            print_text('и больше не сможет проходить через дверь красного цвета', 10, 210, (60, 140, 190), font_size=20)
            print_text('Профиль:', 10, 240, (60, 140, 190), font_size=20)
            print_text('Показывает лучшее время за которое были пройдены уровни испытаний', 10, 270, (60, 140, 190), font_size=20)
            print_text('Испытания:', 10, 300, (60, 140, 190), font_size=20)
            print_text('Это сложная группа уровней которые были сделаны вручную', 10, 330, (60, 140, 190), font_size=20)
            button.draw(10, 360, 'Назад в меню', m)
            pygame.display.update()
            pygame.display.flip()


class pre_game_setting:
    def __init__(self):
        pass


    def first_update(self):
        global done
        clock = pygame.time.Clock()
        input_box1 = InputBox(10, 10, 140, 32)
        input_box2 = InputBox(10, 52, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False
        button = Button(80, 40)
        button_play = Button(80, 40)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quit()
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            display.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(display)
            button.draw(10, 100, 'Назад в меню', m)
            button_play.draw(100, 100, 'Играть', play)
            print_text('Размер лабиринта', 240, 10, (60, 140, 190), font_size=30)
            print_text('Количество цветов ', 240, 52, (60, 140, 190), font_size=30)
            print_text('Количество цветов  показывает сколько', 10, 150, (60, 140, 190), font_size=20)
            print_text('будет различных по цвету дверей в одном лабиринте', 10, 180, (60, 140, 190), font_size=20)
            print_text('------------------------------------------------------', 10, 190, (250, 140, 200), font_size=30)
            print_text('Размер лабиринта устанавливает размер игрового поля', 10, 220, (60, 140, 190), font_size=20)
            print_text('Указывается в формате xy где x длинна ,а y высота', 10, 250, (60, 140, 190), font_size=20)
            print_text('Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', 10,  280, (60, 140, 190), font_size=20)
            pygame.display.update()
            pygame.display.flip()
            clock.tick(30)





class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



def run_game():
    global count
    game = True
    main = MainWindow()
    pre = pre_game_setting()
    help = Help()
    settings = Settings()
    pygame.mixer.music.play(-1)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if Main_flag is True:
            main.first_update()
        elif Help_flag is True:
            help.first_update()
        elif Pre_game_flag is True:
            pre.first_update()
        elif Settings_flag is True:
            settings.first_update()






run_game()
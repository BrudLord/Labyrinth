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
pygame.mixer.music.load('Music\\579b2fbcdd508f7.mp3')
pygame.mixer.music.set_volume(0.2)
button_sound = pygame.mixer.Sound('Music\\00171.wav')
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
    Main_flag = False
    Pre_game_flag = False
    game_flag = False
    Settings_flag = True
    Help_flag = False
    About_game_flag = False

def h():
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
    Help_flag = True
    About_game_flag = False

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
        BackGround = Background('back\\' + str(count) + '.gif', [0, 0])
        display.blit(BackGround.image, BackGround.rect)
        button.draw(20, 100, 'Играть', p)
        button2.draw(20, 150, "Испытания")
        button3.draw(20, 200, 'Настройки')
        button4.draw(20, 250, 'Профиль')
        button5.draw(20, 300, 'О игре')
        button6.draw(750, 30,  '?')
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
            print_text('Размер лабиринта', 240, 10, (60, 140, 190), font_size=30)
            print_text('Количество цветов дверей', 240, 52, (60, 140, 190), font_size=30)
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
    pygame.mixer.music.play(-1)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if Main_flag is True:
            main.first_update()
        if Pre_game_flag is True:
            pre.first_update()




run_game()
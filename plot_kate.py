# В данном файле хранится сюжет и его обработка
import pymorphy2
import pygame
import numpy as np
from random import randint
from abc import abstractmethod

pygame.init()
pygame.font.init()

WIDTH = 500
HEIGHT = 700
f1 = pygame.font.Font('excentra.ttf', 20)

FPS = 20
# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Persona:
    def __init__(self):
        self.ege_point = 0
        self.name = 0
        self.luck = 0
        self.smart = 0
        self.pop = 0


main_character = Persona()


def draw_persona(name):
    face = pygame.image.load(name)
    screen.blit(face, (270, 250))


def ege_points():
    flag = True
    while flag:
        steps[3].run()
        steps[4].run()
        (x, y) = pygame.mouse.get_pos()
        if steps[4].button1.pressed((x, y)):
            flag = False


class Step:

    @abstractmethod
    def run(self):
        pass

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def draw(self):
        pass

    def draw_choice(self, text1, text2, text3):
        """
        Draws rectangles for choices
        """
        self.button1 = Button()
        self.button1.create_button(screen, 'pink', 100, 560, 300, 40, 10, text1, 'black')
        self.button2 = Button()
        self.button2.create_button(screen, 'pink', 100, 605, 300, 40, 10, text2, 'black')
        self.button3 = Button()
        self.button3.create_button(screen, 'pink', 100, 650, 300, 40, 10, text3, 'black')


class InsertField:
    """
    class for inserting
    """

    def __init__(self, value, x, y, width, height, screen):
        """
        init function
        :param value: value
        :param x: x position on screen
        :param y: y position on screen
        :param width: width
        :param height: height
        :param screen: surface
        """
        self.is_active = False
        self.value = str(value)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def draw(self):
        """
        drawing text on screen
        :return:
        """
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        self.blit_text(self.screen, str(self.value), (self.x + 3, self.y + 3), f1)

    def insert(self, char):
        """
        set text in field
        :param char: symbol
        :return:
        """
        if self.is_active:
            self.value = self.value[:-1]
            self.value += str(char)
            self.value += "|"

    def activate(self):
        """
        activate field
        :return:
        """
        if not self.is_active:
            self.is_active = True
            self.value += "|"

    def deactivate(self):
        """
        disactivate field
        :return:
        """
        if self.is_active:
            self.value = self.value[:-1]
            self.is_active = False

    def check_mouse(self):
        """
        check mouse position
        :return:
        """
        if self.x < pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y \
                + self.height:
            return True
        else:
            return False


class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length // len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):
        for i in range(1, 10):
            s = pygame.Surface((length + (i * 2), height + (i * 2)))
            s.fill(color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
            surface.blit(s, (x - i, y - i))
        pygame.draw.rect(surface, color, (x, y, length, height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print
                        "Some button was pressed!"
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


class Step_0(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button.pressed((x, y)):
                        finished = True

    def draw(self):
        screen.fill((255, 255, 255))
        zero_surf = pygame.image.load('0.jpg')
        screen.blit(zero_surf, (0, 100))
        self.button = Button()
        self.button.create_button(screen, 'BLUE', 100, 250, 300, 100, 50, "Play", 'BLACK')
        pygame.display.update()


class Step_1(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        screen.fill((240, 255, 255))
        text1 = "Вот-вот начнётся твоя история. Но сначала узнаем, как ты сдала ЕГЭ."
        self.blit_text(self.screen, text1, (50, 260), f1)
        pygame.display.update()


class Step_2(Step):

    def __init__(self, screen):
        self.screen = screen
        self.field1 = InsertField("", 100, 100, 200, 50, self.screen)

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return self.field1.value
                        finished = True
                    if event.key == pygame.K_BACKSPACE:
                        if self.field1.is_active and self.field1.value != "":
                            self.field1.value = self.field1.value[:-2]
                            self.field1.value += "|"

                    else:
                        if len(self.field1.value) < 15:
                            self.field1.insert(event.unicode)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.field1.check_mouse():
                        self.field1.activate()
                    else:
                        self.field1.deactivate()

            self.draw()

    def draw(self):
        screen.fill((100, 255, 255))
        text1 = "Введите имя:"
        self.blit_text(self.screen, text1, (50, 260), f1)
        self.field1.draw()
        pygame.display.update()


class Step_3(Step):

    def __init__(self, screen):
        self.screen = screen
        self.ege_mark = randint(250, 310)

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        self.ege_mark = randint(250, 310)
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        screen.fill((240, 255, 255))
        main_character.ege_point = self.ege_mark
        pygame.draw.rect(screen, 'blue', (150, 200, 200, 300))
        text1 = "Твой балл ЕГЭ:"
        self.blit_text(screen, text1, (150, 100), f1)
        self.blit_text(screen, str(self.ege_mark), (245, 350), f1)
        pygame.display.update()


class Step_4(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button3.pressed((x, y)):
                        pygame.quit()
                    elif self.button2.pressed((x, y)):
                        ege_points()
                        finished = True
                    elif self.button1.pressed((x, y)):
                        finished = True
            self.draw()

    def draw(self):
        screen.fill((240, 255, 255))
        draw_persona('main_hero.png')
        text = "Я сдала ЕГЭ: "
        self.blit_text(screen, text, (150, 100), f1)
        text1 = "Отлично! Пусть начнётся моя история."
        text2 = "Хорошо. Но я хочу пересдать ЕГЭ."
        text3 = "Я на ВМК"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_7(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        screen.fill('black')
        text = "Глава 1: первый день на Физтехе"
        pygame.draw.rect(screen, 'white', (180, 300, 200, 50))
        self.blit_text(screen, text, (180, 300), f1)
        pygame.display.update()


class Step_8(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('home.jpg')
        screen.blit(scene, (0, 0))
        pygame.display.update()


class Step_9(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('main_hero.png')
        text = "Какое доброе утро! До сих пор не верится, что я поступила на Физтех. Что ж, первая ночь в общаге прошла " \
               "спокойно, посмотрим, что для меня приготовил первый учебный день. "
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
        self.blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_10(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('main_hero.png')
        text = "Ух, сегодня целых 6 пар… Многовато. Надеюсь, я получу от них удовольствие."
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
        self.blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_11(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_11.png ')
        screen.blit(scene, (0, 0))
        pygame.display.update()


class Step_12(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        pygame.display.update()


class Step_13(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('main_hero.png')
        text = "Ух, почти успела. Вроде ничего важного не пропустила, отлично."
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
        self.blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_14(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_13.jpg')
        screen.blit(scene, (0, 0))
        text = "Привет! Я Миша. Ты же " + str(main_character.name) + "? Рад познакомиться. Мы с тобой одногруппники."
        pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
        self.blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_15(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('main_hero.png')
        text = "Привет. Взаимно!"
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
        self.blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_16(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_13.jpg')
        screen.blit(scene, (0, 0))
        text = "Как тебе лекция?"
        pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
        self.blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_17(Step):

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        finished = True
            self.draw()

    def draw(self):
        scene = pygame.image.load('zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('main_hero.png')
        text1 = "Вообще ничего не понимаю..."
        text2 = "Интересно, но пока дается с трудом."
        text3 = "Пфф.. Легкотня!"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


def step_23():
    scene = pygame.image.load('zastavka_13.jpg')
    screen.blit(scene, (0, 0))
    text = "Если что, всегда рад предложить свою помощь. Я в 333 живу, легко запомнить. приходи на чай с матаном."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_25():
    scene = pygame.image.load('zastavka_13.jpg')
    screen.blit(scene, (0, 0))
    text = "А я что-то не совсем понимаю… Я буду очень благодарен тебе, если ты поможешь мне разобраться с этой темой"
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_26():
    scene = pygame.image.load('zastavka_12.jpg')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    draw_choice()
    text1 = "Спасибо! Я приду."
    text2 = "Спасибо, но я сама попробую разобраться."
    text3 = "Отвали, без тебя справлюсь."
    # blit_text(screen, text1, (120, 570), f1)
    # blit_text(screen, text2, (120, 615), f1)
    # blit_text(screen, text3, (120, 660), f1)
    pygame.display.update()


def step_31():
    scene = pygame.image.load('zastavka_12.jpg')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    draw_choice()
    text1 = "Хорошо, я с радостью помогу!"
    text2 = "Посмотрим."
    text3 = "Это не мои проблемы."
    # blit_text(screen, text1, (120, 570), f1)
    # blit_text(screen, text3, (120, 660), f1)
    pygame.display.update()


def step_35():
    scene = pygame.image.load('zastavka_13.jpg')
    screen.blit(scene, (0, 0))
    text = "Отлично! Приходи ко мне после пар."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_35_1():
    scene = pygame.image.load('zastavka_12.jpg')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Договорились!"
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_36():
    scene = pygame.image.load('zastavka_13.jpg')
    screen.blit(scene, (0, 0))
    text = "Ну, приходи ко мне, если надумаешь. Буду рад видеть."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_36_1():
    scene = pygame.image.load('zastavka_12.jpg')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Хорошо."
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_37():
    scene = pygame.image.load('zastavka_12.jpg')
    screen.blit(scene, (0, 0))
    text = "Лекция окончена. Всем спасибо, до свидания."
    pygame.draw.rect(screen, 'white', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_38():
    scene = pygame.image.load('home.jpg')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Ух.. Какой насыщенный день. Все 6 пар отсидела, устала до ужаса."
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    # blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


# катя просто лучшая, люблю её

step0 = Step_0(screen)
step1 = Step_1(screen)
step2 = Step_2(screen)
step3 = Step_3(screen)
step4 = Step_4(screen)
step7 = Step_7(screen)
steps = [step0, step1, step2, step3, step4, step7]

steps[0].run()
steps[1].run()
steps[2].run()
main_character = Persona()
main_character.name = steps[2].field1.value
steps[3].run()
steps[4].run()
steps[5].run()

pygame.quit()

import pygame
from random import randint
from abc import abstractmethod, ABC

WIDTH = 500
HEIGHT = 700

pygame.init()
pygame.font.init()
# Шрифт
f1 = pygame.font.SysFont('arial', 20)

FPS = 20
# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Global
is_24 = False
is_25 = False
step = 0


class Persona:
    """
    Класс главного героя, хранит в себе его основные характеристики.
    """

    def __init__(self):
        self.ege_point = 0
        self.name = 0
        self.luck = 0
        self.smart = 0
        self.pop = 0


# Персонаж
main_character = Persona()


def draw_persona(name):
    """
    Функция отрисовывает главного героя
    :param name: картинка с лицом героя
    :return:
    """
    face = pygame.image.load(name)
    screen.blit(face, (270, 250))


def draw_talker(name):
    """
    Функция отрисовывает собеседника героя
    :param name: картинка с лицом собеседника
    :return:
    """
    face = pygame.image.load(name)
    screen.blit(face, (60, 300))


def ege_points():
    """
    Функция позволяет выбирать балл ЕГЭ до тех пор, пока он не устроит пользователя.
    :return:
    """
    flag_ = True
    while flag_:
        steps[3].run(step)
        steps[4].run(step)
        (x, y) = pygame.mouse.get_pos()
        if steps[4].button1.pressed((x, y)):
            flag_ = False


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    """
    Функция печатает текст на экране так, чтобы он не выходил за рамки экрана
    :param surface: поверхность, на которой должна происходить отрисовка
    :param text: текст, который нужно отрисовать
    :param pos: позиция текста
    :param font: шрифт
    :param color: цвет
    :return:
    """
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
        y += word_height  # S tart on new row.


class Step:
    """
    Интерфейсный класс одного события, от которого будут наследоваться последующие события.
    """

    @abstractmethod
    def __init__(self, screen_):
        self.screen = screen_
        self.button1 = Button()
        self.button2 = Button()
        self.button3 = Button()

    def run(self, next_step):
        """
        Основной цикл программы
        :return:
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return next_step
            self.draw()

    def draw(self):
        """
        Отрисовка экрана
        :return:
        """
        pass

    def draw_choice(self, text1, text2, text3):
        """
        Draws buttons for choices
        """
        self.button1.create_button(screen, 'pink', 100, 560, 300, 40, 10, text1, 'black')
        self.button2.create_button(screen, 'pink', 100, 605, 300, 40, 10, text2, 'black')
        self.button3.create_button(screen, 'pink', 100, 650, 300, 40, 10, text3, 'black')


class InsertField:
    """
    class for inserting
    """

    def __init__(self, value, x, y, width, height, screen_):
        """
        init function
        :param value: value
        :param x: x position on screen
        :param y: y position on screen
        :param width: width
        :param height: height
        :param screen_: surface
        """
        self.is_active = False
        self.value = str(value)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen_

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        """
        Функция печатает текст на экране так, чтобы он не выходил за рамки экрана
        :param surface: поверхность, на которой должна происходить отрисовка
        :param text: текст, который нужно отрисовать
        :param pos: позиция текста
        :param font: шрифт
        :param color: цвет
        :return:
        """
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
        set text in squares
        :param char: symbol
        :return:
        """
        if self.is_active:
            self.value = self.value[:-1]
            self.value += str(char)
            self.value += "|"

    def activate(self):
        """
        activate squares
        :return:
        """
        if not self.is_active:
            self.is_active = True
            self.value += "|"

    def deactivate(self):
        """
        disactivate squares
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
    """
    Класс создания кнопки
    """

    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        """
        Создание кнопки
        :param surface: поверхность отрисовки
        :param color: цвет кнопки
        :param x: координата верхнего левого угла кнопки
        :param y: координата верхнего левого угла кнопки
        :param length: длина кнопки
        :param height: ширина кнопки
        :param width: величина тени от кнопки
        :param text: текст на кнопке
        :param text_color: цвет текста
        :return:a
        """
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        """
        Отрисовка текста на кнопке
        :param surface: поверхность отрисовки
        :param text: текст
        :param text_color: цвет текста
        :param length: длина кнопки
        :param height: ширина кнопки
        :param x: координата верхнего левого угла кнопки
        :param y: координата верхнего левого угла кнопки
        :return:
        """
        font_size = int(length // (len(text)))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, True, text_color)
        surface.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):
        """
        Отрисовка кнопки
        :param surface: поверхность отрисовки
        :param color: цвет кнопки
        :param length: длина кнопки
        :param height: ширина кнопки
        :param x: координата верхнего левого угла кнопки
        :param y: координата верхнего левого угла кнопки
        :param width: величина тени от кнопки
        :return:
        """
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
        """
        Возвращает True, если произошло нажатие на кнопку и False в обратном случае.
        :param mouse: координаты щелчка мыши
        :return:
        """
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
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

    def __init__(self, screen_):
        self.screen = screen_
        self.button = Button()

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button.pressed((x, y)):
                        return next_step

    def draw(self):
        screen.fill((255, 255, 255))
        zero_surf = pygame.image.load('Images/zastavka0.png')
        screen.blit(zero_surf, (0, 0))

        text_0 = pygame.image.load('Images/text_0.png')
        screen.blit(text_0, (50, -10))
        self.button.create_button(screen, 'BLUE', 100, 510, 300, 100, 50, "Play", 'BLACK')
        button = pygame.image.load('Images/new_game.png')
        screen.blit(button, (50, 500))
        pygame.display.update()


class Step_1(Step, ABC):

    def draw(self):
        zastavka_1 = pygame.image.load('Images/zastavka_1.png')
        screen.blit(zastavka_1, (0, 0))
        pygame.display.update()


class Step_2(Step):

    def __init__(self, screen_):
        self.screen = screen_
        self.field1 = InsertField("", 75, 350, 350, 60, self.screen)

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main_character.name = self.field1.value
                        return next_step
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
        zastavka_2 = pygame.image.load('Images/zastavka_2.png')
        screen.blit(zastavka_2, (0, 0))
        self.field1.draw()
        pygame.display.update()


class Step_3(Step):

    def __init__(self, screen_):
        self.screen = screen_
        self.ege_mark = randint(250, 310)

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        self.ege_mark = randint(250, 310)
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return next_step
            self.draw()

    def draw(self):
        main_character.ege_point = self.ege_mark
        zastavka_3 = pygame.image.load('Images/zastavka_3.png')
        screen.blit(zastavka_3, (0, 0))
        blit_text(screen, str(self.ege_mark), (235, 430), f1)
        pygame.display.update()


class Step_4(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button3.pressed((x, y)):
                        return 0
                    elif self.button2.pressed((x, y)):
                        ege_points()
                        return 5
                    elif self.button1.pressed((x, y)):
                        return 5
            self.draw()

    def draw(self):
        zastavka_4 = pygame.image.load('Images/zastavka_4.png')
        screen.blit(zastavka_4, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "Отлично! Пусть начнётся моя история."
        text2 = "Хорошо. Но я хочу пересдать ЕГЭ."
        text3 = "Я на ВМК"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_7(Step, ABC):

    def draw(self):
        zastavka_7 = pygame.image.load('Images/nk.png')
        screen.blit(zastavka_7, (0, 0))
        text_7 = pygame.image.load('Images/text_7.png')
        screen.blit(text_7, (50, 290))
        pygame.display.update()


class Step_8(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        pygame.display.update()


class Step_9(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Какое доброе утро! До сих пор не верится, что я поступила на Физтех. Что ж, первая ночь в общаге" \
               " прошла спокойно, посмотрим, что для меня приготовил первый учебный день. "
        pygame.draw.rect(screen, 'pink', (70, 580, 500, 100))
        blit_text(screen, text, (80, 585), f1)
        pygame.display.update()


class Step_10(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Ух, сегодня целых 6 пар… Многовато. Надеюсь, я получу от них удовольствие."
        pygame.draw.rect(screen, 'pink', (70, 600, 500, 60))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()


class Step_11(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/nk.png')
        screen.blit(scene, (0, 0))
        pygame.display.update()


class Step_12(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        pygame.display.update()


class Step_13(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Ух, почти успела. Вроде ничего важного не пропустила, отлично."
        pygame.draw.rect(screen, 'pink', (100, 600, 500, 60))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()


class Step_14(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_13.png')
        screen.blit(scene, (0, 0))
        name = pygame.image.load('Images/misha.png')
        screen.blit(name, (100, 565))
        text = "Привет! Я Миша. Ты же " + str(main_character.name) + "? Рад познакомиться. "
        text2 = "Мы с тобой одногруппники."
        pygame.draw.rect(screen, 'blue', (60, 600, 350, 100))
        blit_text(screen, text, (65, 600), f1)
        blit_text(screen, text2, (65, 640), f1)
        pygame.display.update()


class Step_15(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Привет. Взаимно!"
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 60))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()


class Step_16(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_13.png')
        screen.blit(scene, (0, 0))
        name = pygame.image.load('Images/misha.png')
        screen.blit(name, (100, 565))
        text = "Как тебе лекция?"
        pygame.draw.rect(screen, 'blue', (100, 600, 300, 60))
        blit_text(screen, text, (105, 610), f1)
        pygame.display.update()


class Step_17(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button1.pressed((x, y)):
                        return 16
                    elif self.button2.pressed((x, y)):
                        main_character.smart += 1
                        return 16
                    elif self.button3.pressed((x, y)):
                        main_character.smart += 2
                        main_character.pop += 1
                        return 17
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "Вообще ничего не понимаю..."
        text2 = "Интересно, но пока дается с трудом."
        text3 = "Пфф.. Легкотня!"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_24(Step, ABC):

    def run(self, next_step):
        """
        Основной цикл программы
        :return:
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 18
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/zastavka_13.png')
        screen.blit(scene, (0, 0))
        name = pygame.image.load('Images/misha.png')
        screen.blit(name, (100, 565))
        text = "Если что, всегда рад предложить свою помощь. Я в 333 живу, легко запомнить. приходи на чай с матаном."
        pygame.draw.rect(screen, 'blue', (60, 600, 380, 100))
        blit_text(screen, text, (65, 610), f1)
        pygame.display.update()


class Step_25(Step, ABC):

    def run(self, next_step):
        """
        Основной цикл программы
        :return:
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 19
            self.draw()

    def draw(self):
        global is_25
        scene = pygame.image.load('Images/zastavka_13.png')
        screen.blit(scene, (0, 0))
        name = pygame.image.load('Images/misha.png')
        screen.blit(name, (100, 565))
        text = "А я что-то не совсем понимаю… Я буду очень благодарен тебе, если ты поможешь" \
               " мне разобраться с этой темой"
        pygame.draw.rect(screen, 'blue', (80, 600, 400, 100))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()
        is_25 = True


class Step_26(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button1.pressed((x, y)):
                        main_character.smart += 1
                        main_character.pop += 1
                        if is_25:
                            return 19
                        else:
                            return 20
                    elif self.button3.pressed((x, y)):
                        main_character.pop -= 1
                        return 24
                    elif self.button2.pressed((x, y)):
                        if is_25:
                            return 19
                        else:
                            return 22
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "Спасибо! Я приду."
        text2 = "Спасибо, но я сама попробую разобраться."
        text3 = "Отвали, без тебя справлюсь."
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_31(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button1.pressed((x, y)):
                        main_character.smart += 1
                        main_character.pop += 1
                        return 20
                    elif self.button3.pressed((x, y)):
                        main_character.pop -= 1
                        return 32
                    elif self.button2.pressed((x, y)):
                        return 22
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "Хорошо, я с радостью помогу!"
        text2 = "Посмотрим."
        text3 = "Это не мои проблемы."
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_35(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_13.png')
        screen.blit(scene, (0, 0))
        name = pygame.image.load('Images/misha.png')
        screen.blit(name, (100, 565))
        text = "Отлично! Приходи ко мне после пар."
        pygame.draw.rect(screen, 'blue', (100, 600, 400, 60))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()


class Step_35_1(Step, ABC):

    def run(self, next_step):
        """
        Основной цикл программы
        :return:
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 24
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Договорились!"
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 60))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()


class Step_36(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_13.png')
        screen.blit(scene, (0, 0))
        name = pygame.image.load('Images/misha.png')
        screen.blit(name, (100, 565))
        text = "Ну, приходи ко мне, если надумаешь. Буду рад видеть."
        pygame.draw.rect(screen, 'blue', (100, 600, 400, 40))
        blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_36_1(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Хорошо."
        pygame.draw.rect(screen, 'pink', (100, 600, 300, 60))
        blit_text(screen, text, (100, 610), f1)
        pygame.display.update()


class Step_37(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_12.jpg')
        screen.blit(scene, (0, 0))
        text = "Лекция окончена. Всем спасибо, до свидания."
        pygame.draw.rect(screen, 'white', (0, 590, 500, 60))
        blit_text(screen, text, (10, 600), f1)
        pygame.display.update()


class Step_38(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text = "Ух.. Какой насыщенный день. Все 6 пар отсидела, устала до ужаса."
        pygame.draw.rect(screen, 'pink', (100, 590, 400, 60))
        blit_text(screen, text, (100, 600), f1)
        pygame.display.update()


class Step_39(Step, ABC):

    def run(self, next_step):
        """
        Основной цикл программы
        :return:
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if main_character.smart >= 2:
                            return 27
                        else:
                            return 28
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        draw_talker('Images/sosedka.png')
        text = "Да уж, ну и денёк.. А го на нк пиво пить? Развеемся, отдохнем, познакомимся с кем-то."
        pygame.draw.rect(screen, 'blue', (60, 590, 400, 100))
        blit_text(screen, text, (65, 595), f1)
        pygame.display.update()


class Step_40_smart(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button1.pressed((x, y)):
                        main_character.pop += 1
                        return 29
                    elif self.button2.pressed((x, y)):
                        main_character.pop -= 1
                        return 32
                    elif self.button3.pressed((x, y)):
                        main_character.pop -= 1
                        main_character.smart += 1
                        return 32
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "Го, я всегда за!"
        text2 = "Не, в другой раз"
        text3 = "Не, я буду ботать"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_40_non_smart(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button1.pressed((x, y)):
                        main_character.pop -= 1
                        main_character.smart += 1
                        return 32
                    elif self.button2.pressed((x, y)):
                        main_character.pop -= 1
                        return 32
                    elif self.button3.pressed((x, y)):
                        main_character.pop -= 2
                        return 32
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/home.jpg')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "Не, я буду ботать"
        text2 = "Не, в другой раз"
        text3 = "*Молча и агрессивно смотреть*"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_43(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_43.png')
        screen.blit(scene, (0, 0))
        chel = pygame.image.load('Images/chel_1.png')
        screen.blit(chel, (100, 565))
        #        pygame.mixer.music.load('trava_u_doma.mp3')
        #        pygame.mixer.music.play()
        text = "ОТ КОРОБКИ ДО НК..."
        pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
        blit_text(screen, text, (110, 610), f1)
        pygame.display.update()


class Step_43_1(Step, ABC):

    def draw(self):
        scene = pygame.image.load('Images/zastavka_43.png')
        screen.blit(scene, (0, 0))
        chel = pygame.image.load('Images/chel_2.png')
        screen.blit(chel, (100, 565))
        text = "КТО ЧЕМПИОН???"
        pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
        blit_text(screen, text, (110, 610), f1)
        pygame.display.update()


class Step_44(Step, ABC):

    def run(self, next_step):
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if self.button1.pressed((x, y)):
                        main_character.pop += 2
                        return 32
                    elif self.button2.pressed((x, y)):
                        main_character.pop += 1
                        return 32
                    elif self.button3.pressed((x, y)):
                        main_character.pop -= 2
                        return 32
            self.draw()

    def draw(self):
        scene = pygame.image.load('Images/nk.png')
        screen.blit(scene, (0, 0))
        draw_persona('Images/main_hero.png')
        text1 = "ФАКИ ЧЕМПИОН!"
        text2 = "Факи чемпион"
        text3 = "*промолчать*"
        self.draw_choice(text1, text2, text3)
        pygame.display.update()


class Step_45(Step, ABC):
    def run(self, next_step):
        """
        Основной цикл программы
        :return:
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 0
            self.draw()

    def draw(self):
        konec = pygame.image.load('Images/konec.png')
        screen.blit(konec, (0, 0))
        pygame.display.update()


step0 = Step_0(screen)
step1 = Step_1(screen)
step2 = Step_2(screen)
step3 = Step_3(screen)
step4 = Step_4(screen)
step7 = Step_7(screen)
step8 = Step_8(screen)
step9 = Step_9(screen)
step10 = Step_10(screen)
step11 = Step_11(screen)
step12 = Step_12(screen)
step13 = Step_13(screen)
step14 = Step_14(screen)
step15 = Step_15(screen)
step16 = Step_16(screen)
step17 = Step_17(screen)
step24 = Step_24(screen)
step25 = Step_25(screen)
step26 = Step_26(screen)
step31 = Step_31(screen)
step35 = Step_35(screen)
step35_1 = Step_35_1(screen)
step36 = Step_36(screen)
step36_1 = Step_36_1(screen)
step37 = Step_37(screen)
step38 = Step_38(screen)
step39 = Step_39(screen)
step40_smart = Step_40_smart(screen)
step40_non_smart = Step_40_non_smart(screen)
step43 = Step_43(screen)
step43_1 = Step_43_1(screen)
step44 = Step_44(screen)
step45 = Step_45(screen)

steps = [step0, step1, step2, step3, step4, step7, step8, step9, step10, step11, step12, step13, step14, step15,
         step16,
         step17, step24, step25, step26, step31, step35, step35_1, step36, step36_1, step37, step38, step39,
         step40_smart, step40_non_smart, step43, step43_1, step44, step45]

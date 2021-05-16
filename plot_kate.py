# В данном файле хранится сюжет и его обработка
import pymorphy2
import pygame
import numpy as np
from random import randint

pygame.init()
pygame.font.init()

WIDTH = 500
HEIGHT = 700
f1 = pygame.font.Font('excentra.ttf', 20)

FPS = 20
# Отрисовка заставки
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
zero_surf = pygame.image.load('0.jpg')
screen.blit(zero_surf, (0, 100))

pygame.draw.rect(screen, 'BLUE', (100, 250, 300, 100))


class Persona:
    def __init__(self):
        self.ege_point = 0
        self.name = 0
        self.luck = 0
        self.smart = 0
        self.pop = 0


def realise_plot(events):
    """
    This function realises events that precede slide "choice"
    :param events: array of events
    """
    i = 0
    while i < len(events):
        events[i]()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i += 1


main_character = Persona()


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
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


def draw_persona(name):
    face = pygame.image.load(name)
    screen.blit(face, (270, 250))
 #   pygame.display.update()


def click(event_type):
    """
    The function returns the coordinates of the mouse click
    :param event_type: event - mouse click
    """
    (x, y) = event_type.pos
    return [x, y]


def choice(position):
    """
    This function analyse choice of a player.
    :param position: coordinates of the mouse click
    :return: 1/2/3 - possible choice of a player
    """
    if 100 <= position[0] <= 400 and 560 <= position[1] <= 600:
        return 1
    elif 100 <= position[0] <= 400 and 605 <= position[1] <= 645:
        return 2
    elif 100 <= position[0] <= 400 and 650 <= position[1] <= 690:
        return 3


def ege_points():
    flag = True
    while flag:
        realise_plot([step_3, step_4])
        next_step = choice(click(event))
        if next_step == 1:
            flag = False


def draw_choice():
    """
    Draws rectangles for choices
    """
    pygame.draw.rect(screen, 'pink', (100, 560, 300, 40))
    pygame.draw.rect(screen, 'pink', (100, 605, 300, 40))
    pygame.draw.rect(screen, 'pink', (100, 650, 300, 40))


def step_1():
    screen.fill((240, 255, 255))
    text1 = "Вот-вот начнётся твоя история. Но сначала узнаем, как ты сдала ЕГЭ."
    blit_text(screen, text1, (50, 260), f1)
    pygame.display.update()


def step_3():
    screen.fill((240, 255, 255))
    ege_mark = str(randint(250, 310))
#    pygame.display.update()
    main_character.ege_point = ege_mark
    pygame.draw.rect(screen, 'blue', (150, 200, 200, 300))
    text1 = "Твой балл ЕГЭ:"
    blit_text(screen, text1, (150, 100), f1)
    blit_text(screen, ege_mark, (245, 350), f1)
    pygame.display.update()


def step_2():
    screen.fill((240, 255, 255))
    text1 = "Введите свое имя: "
    blit_text(screen, text1, (150, 100), f1)
#    pygame.display.update()
    name = "marie" #FIXME должен быть инпут
    main_character.name = name
    blit_text(screen, main_character.name, (245, 350), f1)
    pygame.display.update()


def step_4():
    screen.fill((240, 255, 255))
    draw_persona('main_hero.png')
    text = "Я сдала ЕГЭ: "
    blit_text(screen, text, (150, 100), f1)
    draw_choice()
    pygame.draw.rect(screen, (240, 255, 255), (100, 650, 300, 40))
    text1 = "Отлично! Пусть начнётся моя история."
    text2 = "Хорошо. Но я хочу пересдать ЕГЭ."
    blit_text(screen, text1, (120, 570), f1)
    blit_text(screen, text2, (120, 615), f1)
    pygame.display.update()


def step_7():
    screen.fill('black')
    text = "Глава 1: первый день на Физтехе"
    blit_text(screen, text, (180, 300))
    pygame.display.update()


def step_8():
    scene = pygame.image.load('home.png')
    screen.blit(scene, (0, 0))
    pygame.display.update()


def step_9():
    scene = pygame.image.load('home.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Какое доброе утро! До сих пор не верится, что я поступила на Физтех. Что ж, первая ночь в общаге прошла " \
           "спокойно, посмотрим, что для меня приготовил первый учебный день. "
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600))
    pygame.display.update()


def step_10():
    scene = pygame.image.load('home.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Ух, сегодня целых 6 пар… Многовато. Надеюсь, я получу от них удовольствие."
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_11():
    scene = pygame.image.load('zastavka_11.png')
    screen.blit(scene, (0, 0))
    pygame.display.update()


def step_12():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    pygame.display.update()


def step_13():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Ух, почти успела. Вроде ничего важного не пропустила, отлично."
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_14():
    scene = pygame.image.load('zastavka_13.png')
    screen.blit(scene, (0, 0))
    text = "Привет! Я Миша. Ты же " + main_character.name + "? Рад познакомиться. Мы с тобой одногруппники."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_15():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Привет. Взаимно!"
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_16():
    scene = pygame.image.load('zastavka_13.png')
    screen.blit(scene, (0, 0))
    text = "Как тебе лекция?"
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_17():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    draw_choice()
    text1 = "Вообще ничего не понимаю..."
    text2 = "Интересно, но пока дается с трудом."
    text3 = "Пфф.. Легкотня!"
    blit_text(screen, text1, (120, 570), f1)
    blit_text(screen, text2, (120, 615), f1)
    blit_text(screen, text3, (120, 660), f1)
    pygame.display.update()


def step_23():
    scene = pygame.image.load('zastavka_13.png')
    screen.blit(scene, (0, 0))
    text = "Если что, всегда рад предложить свою помощь. Я в 333 живу, легко запомнить. приходи на чай с матаном."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_25():
    scene = pygame.image.load('zastavka_13.png')
    screen.blit(scene, (0, 0))
    text = "А я что-то не совсем понимаю… Я буду очень благодарен тебе, если ты поможешь мне разобраться с этой темой"
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_26():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    draw_choice()
    text1 = "Спасибо! Я приду."
    text2 = "Спасибо, но я сама попробую разобраться."
    text3 = "Отвали, без тебя справлюсь."
    blit_text(screen, text1, (120, 570), f1)
    blit_text(screen, text2, (120, 615), f1)
    blit_text(screen, text3, (120, 660), f1)
    pygame.display.update()


def step_31():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    draw_choice()
    text1 = "Хорошо, я с радостью помогу!"
    text2 = "Посмотрим."
    text3 = "Это не мои проблемы."
    blit_text(screen, text1, (120, 570), f1)
    blit_text(screen, text2, (120, 615), f1)
    blit_text(screen, text3, (120, 660), f1)
    pygame.display.update()


def step_35():
    scene = pygame.image.load('zastavka_13.png')
    screen.blit(scene, (0, 0))
    text = "Отлично! Приходи ко мне после пар."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_35_1():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Договорились!"
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_36():
    scene = pygame.image.load('zastavka_13.png')
    screen.blit(scene, (0, 0))
    text = "Ну, приходи ко мне, если надумаешь. Буду рад видеть."
    pygame.draw.rect(screen, 'blue', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_36_1():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Хорошо."
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_37():
    scene = pygame.image.load('zastavka_12.png')
    screen.blit(scene, (0, 0))
    text = "Лекция окончена. Всем спасибо, до свидания."
    pygame.draw.rect(screen, 'white', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


def step_38():
    scene = pygame.image.load('home.png')
    screen.blit(scene, (0, 0))
    draw_persona('main_hero.png')
    text = "Ух.. Какой насыщенный день. Все 6 пар отсидела, устала до ужаса."
    pygame.draw.rect(screen, 'pink', (100, 600, 300, 40))
    blit_text(screen, text, (100, 600), f1)
    pygame.display.update()


ege = np.array([step_1, step_2, step_3, step_4])
lection = np.array([step_7, step_8, step_9, step_10, step_11, step_12, step_13, step_14, step_15, step_16, step_17])

story = dict([
    ("ege", ege),
    ("lection", lection)
])

# катя просто лучшая, люблю её

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 100 <= x <= 400 and 250 <= y <= 350:
                realise_plot(story["ege"])
            next_plot = choice(click(event))
            if next_plot == 2:
                ege_points()
            else:
                continue
            realise_plot(story["lection"])
            next_plot = choice(click(event))

pygame.quit()
# В данном файле хранится сюжет и его обработка
import pygame
import numpy as np

pygame.init()
pygame.font.init()

WIDTH = 500
HEIGHT = 700
f1 = pygame.font.Font(None, 20)

FPS = 20
# Отрисовка заставки
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
zero_surf = pygame.image.load('0.jpg')
screen.blit(zero_surf, (0, 100))

pygame.draw.rect(screen, 'BLUE', (100, 250, 300, 100))
f1 = pygame.font.Font(None, 36)
text1 = f1.render('Начать игру', True, (0, 0, 0))
screen.blit(text1, (175, 285))
pygame.display.update()


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


def draw_choice():
    """
    Draws rectangles for choices
    """
    pygame.draw.rect(screen, 'pink', (100, 560, 300, 40))
    pygame.draw.rect(screen, 'pink', (100, 605, 300, 40))
    pygame.draw.rect(screen, 'pink', (100, 650, 300, 40))


def one():
    screen.fill((240, 255, 255))
    f1 = pygame.font.Font(None, 30)
    text1 = 'Вот-вот начнется ваша история. Но сначала выберите то, как вы хотите выглядеть'
    blit_text(screen, text1, (50, 50), f1)
    pygame.display.update()


def two():
    screen.fill((240, 255, 255))
    pygame.draw.rect(screen, 'black', (350, 150, 40, 40))
    text1 = f1.render('Hello', True, (0, 0, 0))
    screen.blit(text1, (50, 50))
    pygame.display.update()


def first():
    screen.fill((240, 255, 255))
    pygame.draw.rect(screen, 'black', (350, 150, 40, 40))
    draw_choice()


subj_1 = np.array([one, two])
subj_2 = subj_1
story = {
    "first": subj_1,
    "second": subj_2
}

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
                realise_plot(story["first"])
            first()
            pygame.display.update()
            next_plot = choice(click(event))
            if next_plot == 1:
                realise_plot(story["second"])

pygame.quit()

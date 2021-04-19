import pygame

pygame.init()
pygame.font.init()

WIDTH = 500
HEIGHT = 700
f1 = pygame.font.Font(None, 20)

FPS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
zero_surf = pygame.image.load('0.jpg')
screen.blit(zero_surf, (0, 100))

pygame.draw.rect(screen, 'BLUE', (100, 250, 300, 100))


def draw_choice():
    """
    Draws rectangles for choices
    :return:
    """
    pygame.draw.rect(screen, 'white', (100, 560, 300, 40))
    pygame.draw.rect(screen, 'white', (100, 605, 300, 40))
    pygame.draw.rect(screen, 'white', (100, 650, 300, 40))


def choice(x, y):
    """
    Must return a number, depending on location of the cursor. #FIXME не робит кажется
    :param x: x coordinate
    :param y: y coordinate
    :return: number of choice
    """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= x <= 400 and 560 <= y <= 600:
                # обновить экран
                return 1
            elif 100 <= x <= 400 and 605 <= y <= 645:
                # обновить экран
                return 2
            elif 100 <= x <= 400 and 650 <= 690:
                # обновить экран
                return 3


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
                screen.fill((240, 255, 255))
                pygame.draw.rect(screen, 'black', (350, 150, 40, 40))
                text1 = f1.render('Hello Привет', True, (0, 0, 0))
                screen.blit(text1, (50, 50))
                draw_choice()
                # FIXME не робит обновление координат курсора
                x, y = event.pos
                choice(x, y)
                print(choice(x, y))
                pygame.display.update()
pygame.quit()

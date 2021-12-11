import pygame
import classes

run = True
step = 0
flag = False
while run:
    step = classes.steps[step].run(step + 1)
    if step == 17:
        Flag = True
    if not step:
        run = False

pygame.quit()
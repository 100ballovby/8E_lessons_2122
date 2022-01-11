import pygame as pg
from pygame.draw import rect, circle, polygon  # функции для рисования графических объектов

FPS = 30

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
finished = False

pg.display.update()

x_cor = 0
y_cor = 100
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((0, 0, 0))  # на каждом кадре заливаю фон черным
    circle(screen, (190, 100, 195), [x_cor, y_cor], 50)  # рисую круг
    circle(screen, (50, 167, 219), [x_cor, y_cor], 60, 7)
    pg.display.update()  # обновляю экран

    if x_cor > 640:  # если круг за пределами экрана
        x_cor = 0  # вернуть его в начало (влево)
    else:  # иначе
        x_cor += 10  # изменять Х круга на 3


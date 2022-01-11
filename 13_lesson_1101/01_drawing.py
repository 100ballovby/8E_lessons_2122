import pygame as pg
from pygame.draw import rect, circle, polygon  # функции для рисования графических объектов

FPS = 30

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
finished = False

# нарисуем прямоугольник
rect(screen, (194, 153, 255), [50, 50, 100, 40])
rect(screen, (102, 0, 255), [120, 250, 315, 179], 7)
# где_рисуем, (цвет в RGB), [x, y, ширина, высота], толщина_линии

# нарисуем круг
circle(screen, (82, 117, 24), [360, 50], 50)
circle(screen, (111, 7, 24), [220, 100], 50, 7)
# где_рисуем, (цвет в RGB), [x, y], диаметр, толщина_линии

# нарисуем треугольник
polygon(screen, (200, 100, 200), [[400, 190], [550, 190], [510, 120]], 5)
# где_рисуем, (цвет в RGB), [[x1, y1], [x2, y2], [x3, y3]], толщина линии

x_cor = 280
y_cor = 175
for i in range(10):
    rect(screen, (200, 255, 200), [x_cor, y_cor, 30, 30], 4)
    circle(screen, (255, 255, 255), [x_cor + 15, y_cor + 15], 5)
    x_cor += 35
    y_cor += 30

pg.display.update()

x_cor = 0
y_cor = 100
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    pg.display.update()  # обновляю экран



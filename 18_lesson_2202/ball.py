import pygame as pg
from pygame.draw import circle, rect


FPS = 60
W = 700  # ширина экрана
H = 400  # высота экрана

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 100, 50)

sc = pg.display.set_mode((W, H))
clock = pg.time.Clock()

shot = False
mouse_x = 0
mouse_y = 0
y_shot = H

while True:
    sc.fill(WHITE)
    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        elif i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1 and not shot:
                shot = True
                mouse_x = i.pos[0]
                mouse_y = i.pos[1]
    if shot and y_shot > mouse_y:
        circle(sc, BLACK, (mouse_x, y_shot), 15)
        y_shot -= 10
        pg.display.update()
    elif shot and y_shot <= mouse_y:
        rect(sc, ORANGE, (mouse_x - 25, y_shot - 15, 50, 30))
        pg.display.update()
        pg.time.delay(1000)
        shot = False
        y_shot = H
    clock.tick(FPS)
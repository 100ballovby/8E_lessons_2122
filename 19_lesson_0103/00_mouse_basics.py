import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

WHITE = (255, 255, 255)
ORANGE = (252, 186, 3)
MINT = (50, 171, 143)
BLUE = (113, 151, 235)

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

pl_x = W // 2
pl_y = H // 2
player = pg.Rect(pl_x, pl_y, 50, 50)  # создал квадратную игровую область
player2 = pg.Rect(pl_x + 50, pl_y, 40, 40)

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

        if event.type == pg.MOUSEBUTTONDOWN:  # если нажали на кнопку мыши
            print(f'Нажата кнопка: {event.button}.')  # event.button - возвращает номер кнопки мыши (1 - ЛКМ, 2 - колесо, 3 ПКМ)
            print(f'Мышь находится в: {event.pos}')  # event.pos - кортеж координат мыши
            if player.collidepoint(event.pos):  # если положение мыши совпадает с положением квадрата
                player.x = randint(0, W)
                player.y = randint(0, H)

        if event.type == pg.MOUSEMOTION:  # если мышь двигается
            if player2.collidepoint(event.pos):  # и касается player2
                player2.x = randint(0, W)
                player2.y = randint(0, H)

    screen.fill(WHITE)
    rect(screen, ORANGE, player)  # рисую на области player оранжевый квадрат
    rect(screen, MINT, player2)

    pg.display.update()
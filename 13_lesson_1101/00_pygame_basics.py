import pygame as pg

FPS = 30  # количество кадров в секунду

# настроим окно программы
screen = pg.display.set_mode((640, 480))  # размер окна игры 640x480px
clock = pg.time.Clock()  # отвечает за сменяемость кадров в игре
finished = False  # отвечает за работу игры (когда finished - True, игра окончена)


# если нужно что-то отобразить на экране до начала работы
pg.display.update()  # обновляет кадры на экране
# главный цикл игры
while not finished:  # пока игра не окончена
    clock.tick(FPS)  # задержка
    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # если нажали на крестик в окне
            finished = True  # закончить игру

    pg.display.update()  # обновляю кадры внутри цикла



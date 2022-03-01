import pygame as pg
from pygame.draw import rect, circle, polygon

WHITE = (255, 255, 255)
RED = (255, 0, 0)

W = 1280
H = 560
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

pg.mouse.set_visible(False)  # отключает отображение курсора над экраном игры
img = pg.image.load('angry-birds.png').convert_alpha()  # загружаю картинку
img_rect = img.get_rect()  # сохраняю область отображения изображения в переменной


finished = False
while not finished:
    clock.tick(60)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    screen.fill(WHITE)
    if pg.mouse.get_focused():  # отслеживает положение мыши постоянно
        position = pg.mouse.get_pos()  # сохраняю координаты мыши в переменной
        img_rect.center = position  # центрирую изображение по курсору мыши

    # рисуем тут
    screen.blit(img, img_rect)
    pg.display.update()
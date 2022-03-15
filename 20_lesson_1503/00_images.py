import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1000
H = 1000
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('angry-birds.png').convert_alpha()  # загружаю картинку и конвертирую ее
img_rect = img.get_rect()  # превращаю изображение в объект
center = W // 2, H // 2  # стартовые координаты картинки
img_rect.center = center  # центрирую картинку в стартовых координатах
speed = 10

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    screen.blit(img, img_rect)
    pg.display.update()

    img_rect.x += speed  # сдвигаю х-координату картинки вправо
    if img_rect.left <= 5 or img_rect.right >= W - 5:  # если левый край картинки скрылся за пределами экрана
        speed *= -1
        img = pg.transform.flip(img, True, False)  # отражаю изображение по горизонтали
        # flip(что_вращать, по_иксу, по_игреку)

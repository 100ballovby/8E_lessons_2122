import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1000
H = 1000
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('angry-birds.png').convert_alpha()
img_rect = img.get_rect()
center = W // 2, H // 2
img_rect.center = center
angle = 0
size = 1

# делаю копию изображения
img_copy = img
img_rect_copy = img_rect
img_rect_copy.center = center

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                angle += 10
            if event.key == pg.K_q:
                angle -= 10
            img_copy = pg.transform.rotate(img, angle)  # вращаю изображение
            # rotate(что_вращать, угол_вращения)

    img_rect_copy = img_copy.get_rect()
    img_rect_copy.center = center

    screen.fill((255, 255, 255))
    rect(screen, (255, 0, 0), img_rect, 1)  # рисую квадрат вокруг оригинального изображения
    rect(screen, (0, 255, 0), img_rect_copy, 1)  # рисую квадрат вокруг копии
    screen.blit(img_copy, img_rect_copy)
    pg.display.update()

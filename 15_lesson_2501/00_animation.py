import pygame as pg
from pygame.draw import rect

x = 200
y = 200
change_x = 0  # скорость изменения положения объекта
change_y = 0  # скорость изменения положения объекта
speed = 5
pause = False  # пауза в игре

pg.font.init()  # активируем возможность писать текстом на экране
font_style = pg.font.SysFont(name='Helvetica',
                             size=20, bold=True)  # настраиваю шрифт

s = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

pg.display.update()
finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку на клавиатуре
            print(f'Нажали кнопку {pg.key.name(event.key)}')
            if event.key == pg.K_DOWN:  # если нажали на стрелку вниз
                change_y += speed  # увеличиваем игрек (идем вниз)
                change_x = 0  # отключаем движение по иксу
            elif event.key == pg.K_UP:  # если нажали на стрелку вверх
                change_y -= speed  # уменьшаем игрек (идем вверх)
                change_x = 0  # отключаем движение по иксу
            elif event.key == pg.K_LEFT:  # если нажали на стрелку
                change_y = 0  # отключаем движение по игреку
                change_x -= speed  # уменьшаем икс (движение влево)
            elif event.key == pg.K_RIGHT:  # если нажали на стрелку
                change_y = 0  # отключаем движение по игреку
                change_x += speed  # увеличиваем икс (движение вправо)
            elif event.key == pg.K_ESCAPE:
                change_y = 0
                change_x = 0

    x += change_x  # заставляю объект двигаться по иксу
    y += change_y  # заставляю объект двигаться по игреку

    '''
    if (x > 640) or (x < 0) or (y > 480) or (y < 0):  # если объект ушел за пределы экрана
        # останавливаем объект и ставим его посередине
        change_y = 0
        change_x = 0
        x = 320
        y = 240
        text = font_style.render(
            'Игра окончена. Чтобы продолжить, нажмите стрелку.',
            True, (255, 255, 255)
                                 )  # генерирую текст
        
        s.blit(text, [100, 100])  # отображаю текст на экране в координатах 100, 100
    '''
    s.fill((0, 0, 0))
    rect(s, (191, 67, 87), [x, y, 20, 20])
    pg.display.update()

import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randrange

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

MINT = (77, 255, 213)
RED = (255, 107, 77)
pl_x = W // 2 - 25
pl_y = H // 2 - 25
block = 50
motion = 'stop'

enemy_x = round(randrange(0, W - block) * 10) // 10
enemy_y = round(randrange(0, H - block) * 10) // 10

player = pg.Rect([pl_x, pl_y, block, block])
enemy = pg.Rect([enemy_x, enemy_y, block, block])

score = 0
pg.font.init()  # чтобы можно было писать текст
score_font = pg.font.SysFont('comicsans', 20)

finished = False
pause = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pause = True
    while pause:
        screen.fill((255, 255, 255))
        value = score_font.render('Press C to replay', True, (0, 0, 0))
        screen.blit(value, [W // 2, H // 2])
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finished = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    pause = False



    screen.fill((255, 255, 255))
    rect(screen, MINT, player)
    rect(screen, RED, enemy)

    value = score_font.render(f'Your score {score}', True, (0, 0, 0))
    screen.blit(value, [0, 0])
    pg.display.update()

    keys = pg.key.get_pressed()  # отслеживаю нажатия на кнопки
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.x -= 10
    elif keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.x += 10
    elif keys[pg.K_UP] or keys[pg.K_w]:
        player.y -= 10
    elif keys[pg.K_DOWN] or keys[pg.K_s]:
        player.y += 10

    if player.colliderect(enemy):
        print('hit')
        enemy.x = round(randrange(0, W - block) * 10) // 10
        enemy.y = round(randrange(0, H - block) * 10) // 10
        score += 1

    if player.x >= W - block:
        player.x = W - block
    elif player.x <= 0:
        player.x = 0
    elif player.y >= H - block:
        player.y = H - block
    elif player.y <= 0:
        player.y = 0


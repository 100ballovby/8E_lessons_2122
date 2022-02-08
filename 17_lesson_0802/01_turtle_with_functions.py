from turtle import *
from random import randint, choice


def draw_square(turt, color, x, y, length):
    turt.goto(x, y)  # перейти в х, у, переданные через параметры
    turt.down()  # опустить перо
    turt.color(color)  # выбрать цвет из параметра
    for i in range(4):  # повторить 4 раза
        t.fd(length)  # идти вперед на 100 точек
        t.rt(90)  # повернуть вправо на 90 градусов
    turt.up()  # поднять перо (перестать рисовать)

t = Turtle()  # создаю саму черепашку (она рисует)
t.shape('turtle')  # задаю форму черепашки
t.up()

colors = ['red', 'green', 'blue', 'yellow', 'violet', 'orange']
for i in range(15):
    x = randint(-400, 400)
    y = randint(-400, 400)
    col = choice(colors)
    draw_square(t, col, x, y, 50)

done()  # чтобы окно не закрывалось

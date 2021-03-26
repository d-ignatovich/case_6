"""Case-study Тесселяция
Разработчики:
Игнатович Д. (60%), Миллер А. (), Пойлова Е. ()

""" 
color = ['красный', "синий", "зеленый", "желтый", "оранжевый", "пурпурный", "розовый"]
def main():
    print("Допустимые цвета заливки:"+"\n"+" красный"+"\n"+" синий"+"\n"+" зеленый"+'\n'+" желтый"+'\n'+" оранжевый"+"\n"+" пурпурный"+"\n"+" розовый")
    s = input("Пожалуйста, введите цвет: ")
    while True:
        if s.lower() in color:
            k = input("Пожалуйста, введите цвет: ")
            p(k)
        else:
            print("'" + s + "'" + "не является верным значением.", end='')
            t = input("Пожалуйста, повторите попытку: ")
            s = t
            continue
def p(k):
    while True:
        if k.lower() in color:
            print("Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ")
            exit()
        else:
            print("'" + k + "'" + "не является верным значением.", end="")
            t = input(" Пожалуйста, повторите попытку: ")
            k = t
            continue
main()

import turtle
import math

def hexagon (c, d):
    turtle.down()
    turtle.left(30)
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(d)
        turtle.left(60)
    turtle.end_fill()
    turtle.right(30)
    turtle.up()
    return''

def color (n, i):
    for e in range(0, n):
        if (i % 2) == 1:
            if (e % 2) == 0:
                c = 'yellow'
            else:
                c = 'red'
        else:
            if (e % 2) == 1:
                c = 'yellow'
            else:
                c = 'red'
        print(hexagon(c, d))
        turtle.forward(500/n)

turtle.reset()
turtle.screensize(500, 500)
turtle.width(2)
n = int(input())
d = 500 / n / math.sqrt(3) #
turtle.up()
turtle.color('black')

while True:
    try:
        get_num_hexagons = int(input('Введите количество шестиугольников: '))
        if 4 <= get_num_hexagons <= 20:
           break
        else:
            print('Введите число от 4 до 20')
    except ValueError:
        print('Неверный формат')
print(get_num_hexagons)

for i in range(0, n//2):
    turtle.setposition(-250 + (250 / n), 250 - 2 * d - 3 * d * i)
    print(color(n, i))
    turtle.setposition(-250, 250 - 3.5 * d - (3 * d) * i)
    print(color(n, i))
if (n % 2) != 0:
    turtle.setposition(-250 + (250 / n), 250 - 2 * d - 3 * d * (n//2))
    print(color(n, n//2))
turtle.hideturtle()
turtle.done()



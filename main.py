"""Case-study Тесселяция
Разработчики:
Игнатович Д. (60%), Миллер А. (), Пойлова Е. ()

""" 
color = ['красный', "синий", "зеленый", "желтый", "оранжевый", "пурпурный", "розовый"]
def main():
    print("Допустимые цвета заливки:"+"\n"+" красный"+"\n"+" синий"+"\n"+" зеленый"+'\n'+" желтый"+'\n'+" оранжевый"+"\n"+" пурпурный"+"\n"+" розовый")
    color1 = input("Пожалуйста, введите первый цвет: ")
    while True:
        if color1.lower() in color:
            color1=color1
            color2 = input("Пожалуйста, введите второй цвет: ")
            p(color2)
            break
        else:
            print("'" + color1 + "'" + "не является верным значением.", end='')
            t = input("Пожалуйста, повторите попытку: ")
            color1 = t
            continue
def p(color2):
    while True:
        if color2.lower() in color:
            color2=color2
            break
        else:
            print("'" + color2 + "'" + "не является верным значением.", end="")
            t = input(" Пожалуйста, повторите попытку: ")
            color2 = t
            continue
main()

def num_hexagons():
    while True:
        try:
            get_num_hexagons = int(input('Введите количество шестиугольников: '))
            if 4 <= get_num_hexagons <= 20:
                return (get_num_hexagons)
            break
            else:
                print('Введите число от 4 до 20')
        except ValueError:
            print('Неверный формат')

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

def color_hexagon (n, i):
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
        turtle.forward(500/get_num_hexagons)


turtle.reset()
turtle.screensize(500, 500)
turtle.width(2)
d = 500 / get_num_hexagons / math.sqrt(3) #
turtle.up()
turtle.color('black')

for i in range(0, get_num_hexagons//2):
    turtle.setposition(-250 + (250 / get_num_hexagons), 250 - 2 * d - 3 * d * i)
    print(color_hexagon (get_num_hexagons, i))
    turtle.setposition(-250, 250 - 3.5 * d - (3 * d) * i)
    print(color_hexagon (get_num_hexagons, i))
if (n % 2) != 0:
    turtle.setposition(-250 + (250 / get_num_hexagons), 250 - 2 * d - 3 * d * (get_num_hexagons//2))
    print(color_hexagon (get_num_hexagons, get_num_hexagons//2))
turtle.hideturtle()
turtle.done()



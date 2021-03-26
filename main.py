"""Case-study Тесселяция
Разработчики:
Игнатович Д. (60%), Миллер А. (), Пойлова Е. ()

""" 
color_lists = ['красный', "синий", "зеленый", "желтый", "оранжевый", "пурпурный", "розовый"]
def color():
    
    color = input("Пожалуйста, введите цвет: ")
    while True:
        if color.lower() in color_lists:
            return color
            break
        else:
            print("'" + color + "'" + "не является верным значением.", end='')
            color = input("Пожалуйста, повторите попытку: ")
            continue

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

import turtle
import math
print("Допустимые цвета заливки:"+"\n"+" красный"+"\n"+" синий"+"\n"+" зеленый"+'\n'+" желтый"+'\n'+" оранжевый"+"\n"+" пурпурный"+"\n"+" розовый")
color_1 = color()
color_2 = color()
get_num_hexagons = num_hexagons()
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



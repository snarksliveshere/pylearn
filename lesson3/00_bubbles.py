# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1920, 1080)
radius = 50


def create_circle(point, step, color = sd.COLOR_YELLOW):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color, 1)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# for v in range(3):
#     point = sd.get_point(100, 100)
#     r = radius + 5 * v
#     create_circle(point, r)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

# Нарисовать 10 пузырьков в ряд
# for x in range(10):
#     xx = 100 + x*100
#     point = sd.get_point(xx, 100)
#     create_circle(point, 5)


# Нарисовать три ряда по 10 пузырьков
# for y in range(3):
#     for x in range(10):
#         xx = 100 + x * 100
#         point = sd.get_point(xx, 100 + y*100)
#         create_circle(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

# for v in range(100):
#     rp = sd.random_point()
#     sd.random_color()
#     create_circle(rp, 5, sd.random_color())

sd.pause()

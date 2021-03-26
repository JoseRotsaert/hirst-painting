# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 25)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

color_list = [(236, 35, 108),  (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46),
              (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97),
              (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23),
              (21, 188, 230), (238, 169, 157), (162, 210, 182)]

# 10 lines & 10 rows
# dot size = 20 & space between dots = 50

turtle_module.colormode(255)
tim = turtle_module.Turtle()
screen = turtle_module.Screen()

tim.setheading(225)
tim.pu()
tim.fd(250)
tim.setheading(0)

tim.speed("fastest")


tp = tim.pos()
tp_x = tp[0]
tp_y = tp[1]
print(tp_x)
print(tp_y)

for y in range(10):
    for x in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    tim.setx(tp_x)
    tp_y += 50
    tim.sety(tp_y)

tim.ht()

screen.exitonclick()





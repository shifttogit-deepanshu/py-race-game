# # import colorgram
# #
# # colors = []
# #
# # for color in colorgram.extract('image.jpg',10):
# #     colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
#
# import turtle
# import random
#
# dh = turtle.Turtle()
#
# screen = turtle.Screen()
#
# screen.colormode(255)
#
# color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]
#
# def random_color():
#     color = random.choice(color_list)
#     return color
#
#
# def generate_dot():
#     dh.penup()
#     dh.dot(20,random_color())
#     dh.forward(20)
#
#
# for x in range(10):
#     generate_dot()
#
# while dh.xcor()==200 and dh.ycor()==200:
#     for y in range(0,10):
#         for x in range(0,10):
#             generate_dot()
#         dh.setpos(0,y)
#
# screen.exitonclick()
import turtle
import random

screen = turtle.Screen()

red = turtle.Turtle()
green = turtle.Turtle()
orange = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
purple = turtle.Turtle()

red.shape("turtle")
green.shape("turtle")
orange.shape("turtle")
blue.shape("turtle")
yellow.shape("turtle")
purple.shape("turtle")

red.color("red")
green.color("green")
orange.color("orange")
blue.color("blue")
yellow.color("yellow")
purple.color("purple")

red.penup()
green.penup()
orange.penup()
blue.penup()
yellow.penup()
purple.penup()

def set_turtles():
    red.setpos(red.width() - screen.window_width() / 2, -screen.window_height()/2 +100)
    green.setpos(red.width() - screen.window_width() / 2, -screen.window_height()/2 +200)
    orange.setpos(red.width() - screen.window_width() / 2, -screen.window_height()/2 +300)
    blue.setpos(red.width() - screen.window_width() / 2, -screen.window_height()/2 +400)
    yellow.setpos(red.width() - screen.window_width() / 2, -screen.window_height()/2 +500)
    purple.setpos(red.width() - screen.window_width() / 2, -screen.window_height()/2 +600)



def run_turtle():
    red.forward(random.randint(0,10))
    green.forward(random.randint(0,10))
    orange.forward(random.randint(0,10))
    blue.forward(random.randint(0,10))
    yellow.forward(random.randint(0,10))
    purple.forward(random.randint(0,10))


def result(tur):
    if player==tur:
        print(f"you won! {tur} won the race")
    else:
        print(f"you lose! {tur} won the race")


player = screen.textinput("Choose", "choose your player")


set_turtles()

flag =0

while flag==0:
    run_turtle()
    if red.xcor() >= screen.window_width()/2-100:
        flag=1
        result("red")
    if green.xcor() >= screen.window_width()/2-100:
        flag=1
        result("green")
    if orange.xcor() >= screen.window_width()/2-100:
        flag=1
        result("orange")
    if blue.xcor() >= screen.window_width()/2-100:
        flag=1
        result("blue")
    if yellow.xcor() >= screen.window_width()/2-100:
        flag=1
        result("yellow")
    if purple.xcor() >= screen.window_width()/2-100:
        flag=1
        result("purple")


screen.exitonclick()
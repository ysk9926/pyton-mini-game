import turtle as t
import random
import time


def bye():
    t.bye()
    
s = t.Screen()
s.onkey(bye, "q")
s.listen()


def right():
    if player.xcor() < 200:
        player.fd(15)

def left():
    if player.xcor() > -200:
        player.fd(-15)

t.bgcolor("black")
t.setup(520, 700)

player = t.Turtle()
player.shape("square")
player.shapesize(1, 5)
player.color("white")

player.up()
player.speed(0)
player.goto(0, -270)


ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("tomato")

ball_xspeed = 2
ball_yspeed = 2

t.listen()
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")

game_on = True
life=3

t.up()
t.ht()
t.goto(0, 300)
count = 0
Lv=1

draw = t.Turtle()
draw.color("white")
draw.up()
draw.speed(0)
draw.ht()
draw.goto(0, 250)

cm2 = 50

t.color('white')
t.write(f"life : {life}", False, "center", ("", 20))
draw.write(f"Lv : {Lv}", False, "center", ("", 20))

while game_on:
    count += 1
    new_x = ball.xcor()+ball_xspeed
    new_y = ball.ycor()+ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        ball_yspeed *= -1

    if ball.ycor() < -340:
        life -= 1
        t.clear()
        t.write(f"life : {life}", False, "center", ("", 20))
        time.sleep(0.5)
        ball.goto(0, 100)
        ball_xspeed *= -1
        ball_yspeed *= -1

        if life == 0:
            game_on=False
            t.goto(0, 0)
            t.write("Game Over!", False, "center", ("", 20))

    if player.distance(ball) < cm2 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1

    if count > 1000 and Lv == 1:
        Lv = 2
        draw.clear()
        draw.write(f"Lv : {Lv}", False, "center", ("", 20))
        if ball_xspeed == -2:
            ball_xspeed = -3
        elif ball_xspeed == 2:
            ball_xspeed = 3

        if ball_yspeed == -2:
            ball_yspeed = -3
        elif ball_yspeed == 2:
            ball_yspeed = 3

    elif count > 1900 and Lv == 2:
        Lv = 3
        draw.clear()
        draw.write(f"Lv : {Lv}", False, "center", ("", 20))
        if ball_xspeed == -3:
            ball_xspeed = -5
        elif ball_xspeed == 3:
            ball_xspeed = 5

        if ball_yspeed == -3:
            ball_yspeed = -4
        elif ball_yspeed == 3:
            ball_yspeed = 4

    elif count > 3000 and Lv == 3:
        Lv = 4
        draw.clear()
        draw.write(f"Lv : {Lv}", False, "center", ("", 20))
        if ball_xspeed == -5:
            ball_xspeed = -6
        elif ball_xspeed == 5:
            ball_xspeed = 6

        if ball_yspeed == -5:
            ball_yspeed = -6
        elif ball_yspeed == 5:
            ball_yspeed = 6

        player.shapesize(1, 6)
        cm2 = 60

    elif count > 4000 and Lv == 4:
        Lv = 5
        draw.clear()
        draw.write(f"Lv : {Lv}", False, "center", ("", 20))
        if ball_xspeed == -6:
            ball_xspeed = -7
        elif ball_xspeed == 6:
            ball_xspeed = 7

        if ball_yspeed == -6:
            ball_yspeed = -7
        elif ball_yspeed == 6:
            ball_yspeed = 7

        player.shapesize(1, 7)
        cm2 = 70

    elif count > 5000 and Lv == 5:
        Lv = 6
        draw.clear()
        draw.write(f"Lv : {Lv}", False, "center", ("", 20))

        ball.shapesize(1.0)

        player.shapesize(1, 6)
        cm2 = 60

t.done()

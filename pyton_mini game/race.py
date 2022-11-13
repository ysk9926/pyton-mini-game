import turtle as t
import random

t.up()
t.speed(0)
t.goto(0, 220)
t.write("Race Game", False, "center", ("", 35))

t.goto(-500, 190)
t.down()
t.color("gray")
t.begin_fill()
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(500)
    t.right(90)
t.end_fill()

t.color("black")
t.up()
t.goto(330,200)
t.down()
t.goto(330,-350)

start_line = [150, 90, 30, -30, -90, -150, -210, -270]
ball_color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white" ]

for i in range(7):
    t.up()
    t.goto(-400, start_line[i]-30)
    t.color("white")
    t.down()
    t.goto(400, start_line[i]-30)
    
balls = []
for i in range(8):
    new_ball = t.Turtle()
    new_ball.up()
    new_ball.shape("circle")
    new_ball.color(ball_color[i])
    new_ball.goto(-370,start_line[i])
    new_ball.write(i+1)
    new_ball.goto(-350, start_line[i])
    balls.append(new_ball)
    

    
user_choice = int(t.textinput("Ball Race", "choice number"))
t.up(   )
t.goto(0, -350)
t.color("black")
t.write(f"your batting {user_choice}th ball", False, "center", ("", 30))

game_over = False
while not game_over:
    for i in balls:
        rand_speed = random.randint(1, 10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            game_over = True
        
max_xcor = 0
winner = 0
for i in range(len(balls)):
    if balls[i].xcor() > max_xcor:
        max_xcor = balls[i].xcor()
        winner = i+1
        
t.goto(0,0)

if user_choice == winner:
    t.write("You Win", False, "center", ("", 30))
else:
    t.write(f"Lose winner is {winner} ", False, "center",("", 30))
    
    
t.done()

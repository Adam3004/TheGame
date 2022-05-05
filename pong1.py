import time
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.color('white')
paddle_b.shape('square')
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.color('white')
ball.shape('square')
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=("Courier", 24, 'normal'))

endPen = turtle.Turtle()
endPen.speed(2)
endPen.color('white')
endPen.penup()
endPen.hideturtle()
endPen.goto(0, 0)


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# End of the game
def end_of_game(score_a, score_b):
    ball.clear()
    pen.clear()
    if score_a > score_b:
        endPen.write(f"Player A won {score_a} to {score_b}", align='center', font=("Courier", 40, 'normal'))
    else:
        endPen.write(f"Player B won {score_b} to {score_a}", align='center', font=("Courier", 40, 'normal'))
    time.sleep(5)
    wn.bye()


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Change ball's movement
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        if score_a == 5:
            paddle_b.clear()
            paddle_a.clear()
            end_of_game(score_a, score_b)
        else:
            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=("Courier", 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        if score_b == 5:
            paddle_b.clear()
            paddle_a.clear()
            end_of_game(score_a, score_b)
        else:
            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=("Courier", 24, 'normal'))

    # Paddle and ball collision
    if ((paddle_a.ycor() + 50) > ball.ycor() > (paddle_a.ycor() - 50)) and (
            paddle_a.xcor() < ball.xcor() < paddle_a.xcor() + 20):
        ball.setx(paddle_a.xcor() + 20)
        ball.dx *= -1

    elif (paddle_a.xcor() + 10 > ball.xcor() > paddle_a.xcor() - 10) and (
            paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor()):
        ball.sety(paddle_a.ycor() + 60)
        ball.dy *= -1

    elif (paddle_a.xcor() + 10 > ball.xcor() > paddle_a.xcor() - 10) and (
            paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor()):
        ball.sety(paddle_a.ycor() - 60)
        ball.dy *= -1

    if ((paddle_b.ycor() + 50) > ball.ycor() > (paddle_b.ycor() - 50)) and (
            paddle_b.xcor() > ball.xcor() > paddle_b.xcor() - 20):
        ball.setx(paddle_b.xcor() - 20)
        ball.dx *= -1

    elif (paddle_b.xcor() + 10 > ball.xcor() > paddle_b.xcor() - 10) and (
            paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor()):
        ball.sety(paddle_b.ycor() + 60)
        ball.dy *= -1

    elif (paddle_b.xcor() + 10 > ball.xcor() > paddle_b.xcor() - 10) and (
            paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor()):
        ball.sety(paddle_b.ycor() - 60)
        ball.dy *= -1

    # Blocade paddles on the screen
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

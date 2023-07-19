import turtle
import winsound
import functools

wn = turtle.Screen()
wn.title("Pong Game by @MBS")
wn.bgcolor("black")
wn.setup(width=1000, height=700)
wn.tracer(0)


# First Paddle
first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape("square")
first_paddle.color("white")
first_paddle.shapesize(stretch_wid=5, stretch_len=1)
first_paddle.penup()
first_paddle.goto(-450, 0)

# Second Paddle
second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape("square")
second_paddle.color("white")
second_paddle.shapesize(stretch_wid=5, stretch_len=1)
second_paddle.penup()
second_paddle.goto(450, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.dx = 0.25
ball.dy = -0.25

# Score

score_a = 0
score_b = 0

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 28, "normal"))

# Key Pressing Method 
wn.listen()
key_w = False
key_s = False
key_up = False
key_down = False

def first_paddle_up():
    global key_w
    key_w = True
    if key_down:
        # Move first paddle up and second paddle down
        y = first_paddle.ycor()
        y += 20
        first_paddle.sety(y)
        y = second_paddle.ycor()
        y -= 20
        second_paddle.sety(y)
    elif key_up:
        # Move both paddles up
        y = first_paddle.ycor()
        y += 20
        first_paddle.sety(y)
        y = second_paddle.ycor()
        y += 20
        second_paddle.sety(y)
    else:
        # Move only first paddle up
        y = first_paddle.ycor()
        y += 20
        first_paddle.sety(y)

def first_paddle_down():
    global key_s
    key_s = True
    if key_up:
        # Move first paddle down and second paddle up
        y = first_paddle.ycor()
        y -= 20
        first_paddle.sety(y)
        y = second_paddle.ycor()
        y += 20
        second_paddle.sety(y)
    elif key_down:
        # Move both paddles down
        y = first_paddle.ycor()
        y -= 20
        first_paddle.sety(y)
        y = second_paddle.ycor()
        y -= 20
        second_paddle.sety(y)
    else:
        # Move only first paddle down
        y = first_paddle.ycor()
        y -= 20
        first_paddle.sety(y)

def second_paddle_up():
    global key_up
    key_up = True
    if key_s:
        # Move second paddle up and first paddle down
        y = second_paddle.ycor()
        y += 20
        second_paddle.sety(y)
        y = first_paddle.ycor()
        y -= 20
        first_paddle.sety(y)
    elif key_w:
      # Move both paddles up 
      y = second_paddle.ycor()
      y += 20 
      second_paddle.sety(y) 
      y = first_paddle.ycor() 
      y += 20 
      first_paddle.sety(y) 
    else:
      # Move only second paddle up 
      y = second_paddle.ycor() 
      y += 20 
      second_paddle.sety(y) 

def second_paddle_down():
    global key_down
    key_down = True
    if key_w:
      # Move second paddle down and first paddle up 
      y = second_paddle.ycor() 
      y -= 20 
      second_paddle.sety(y) 
      y = first_paddle.ycor() 
      y += 20 
      first_paddle.sety(y) 
    elif key_s:
      # Move both paddles down 
      y = second_paddle.ycor() 
      y -= 20 
      second_paddle.sety(y) 
      y = first_paddle.ycor() 
      y -= 20 
      first_paddle.sety(y) 
    else:
      # Move only second paddle down 
      y = second_paddle.ycor() 
      y -= 20 
      second_paddle.sety(y) 

def on_key_release(event):
    global key_w, key_s, key_up, key_down
    if event.keysym == 'w':
      key_w = False 
    elif event.keysym == 's':
      key_s = False 
    elif event.keysym == 'Up':
      key_up = False 
    elif event.keysym == 'Down':
      key_down = False 

wn.onkeypress(first_paddle_up, "w")
wn.onkeypress(first_paddle_down, "s")
wn.onkeypress(second_paddle_up, "Up")
wn.onkeypress(second_paddle_down, "Down")
wn.listen()
wn.getcanvas().bind("<KeyRelease-w>", on_key_release)
wn.getcanvas().bind("<KeyRelease-s>", on_key_release)
wn.getcanvas().bind("<KeyRelease-Up>", on_key_release)
wn.getcanvas().bind("<KeyRelease-Down>", on_key_release)




# Main Loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 
    
    # Border Checking
    if ball.ycor() > 335:
        ball.sety(335)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        
    if ball.ycor() < -335:
        ball.sety(-335)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        
    if ball.xcor() > 490:
        ball.goto(0,0)        
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 28, "normal"))
        
        
    if ball.xcor() < -490:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 28, "normal"))

    # Paddle and Ball Collisions
    if (ball.xcor() > 435 and ball.xcor() < 445) and (ball.ycor() < second_paddle.ycor() + 40 and ball.ycor() > second_paddle.ycor() -40):
        ball.setx(435)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        
    if (ball.xcor() < -435 and ball.xcor() > -445) and (ball.ycor() < first_paddle.ycor() + 40 and ball.ycor() > first_paddle.ycor() -40):
        ball.setx(-435)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)



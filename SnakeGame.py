import turtle,time,random,winsound
#set up the screen
win = turtle.Screen()
win.title("snake game")
win.bgcolor('#90ee90')
win.setup(width=630,height=630)
win.tracer(0)
#Snake Head
head = turtle.Turtle()
head.speed(1)
head.shape("square")
head.right(45)
head.shapesize(1.50,1.50 )
head.color("seagreen")
head.penup()
head.goto(0, 100)
head.direction = "stop"
def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 20)
 
    if head.direction == "right":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x + 20)
 
    if head.direction == "left":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x - 20)
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")
delay=0.09
# Snake food
food = turtle.Turtle()
food.speed(1)
food.shape("circle")
food.color("#CD5C5C")
food.penup()
food.shapesize(1,1)
food.goto(0, 0)
score=0
# score
high_score = 0
pen = turtle.Turtle()
pen.speed(1)
pen.shape("square")
pen.color("#fafafa")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

segments = []
line=turtle.Turtle()
line.penup()
line.goto(-300,-300)
line.pensize(3)
line.color('seagreen')
line.pendown()
line.goto(-300,300)
line.goto(300,300)
line.goto(300,-300)
line.goto(-300,-300)
line.ht()
# Main game loop
while True:
    win.update()
    move()
    time.sleep(delay)
    if head.distance(food) < 15:
        delay-=0.001
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        score = score+10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}".format(score,high_score), align="center", font=("Courier", 24, "bold"))
        new_segment = turtle.Turtle()
        new_segment.speed(1)
        new_segment.shape("square")
        new_segment.right(45)
        new_segment.shapesize(1.20,1.20)
        new_segment.color("seagreen")
        new_segment.penup()
        segments.append(new_segment)
        winsound.Beep(1200,50)
    # move the end segment in reverse order
    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
     
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    # Check for head collision
    end=0
    segend=list(segments)
    if len(segments) > 0:
        del segend[0]
    
    for segment in segend:
        if segment.distance(head) < 10:
            end=1
            segment.color('red','red')
            win.update()
            break;
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            win.update()
            end=1
    if end==1:
        winsound.Beep(2000,500)
        time.sleep(0.8)
        food.ht()
        win.update()
        break
for segn in range(len(segments)-1,-1,-1):
    win.update()
    segments[segn].ht()
    time.sleep(0.1)
head.ht()
win.update()
head.goto(0, 0)
pen.clear()
head.write(" GAME  OVER  ",align="center", font=("monospace", 50, "normal"))
head.goto(0, -50)
head.write("   SCORE: {}   ".format(score),align="center", font=("monospace", 40, "normal")) 

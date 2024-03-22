import turtle
import time
import random 


delay = 0.15

#score
score = 0
high_score = 0

#set up the screen
windo = turtle.Screen()
windo.title("Snake game by @inandinisoni")
windo.bgcolor("black")
windo.setup(width=600, height=600)
windo.tracer(0)


#  snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)


segments = []
 
# pen
pen =turtle.Turtle()
pen.speed()
pen.color("light blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0   High Score : 0",align = "center", font=("courier",15,"normal"))




#functions
def go_up():
    if head.direction!="down":
        head.direction = "up"

def go_down():
     if head.direction!="up":
        head.direction = "down"

def go_left():
     if head.direction!="right":
        head.direction = "left"

def go_right():
     if head.direction!="left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor() #his function is used to return the turtle's y coordinate of the current position of turtle
        head.sety(y + 20) #This method is used to set the turtle's second coordinate to y, leaving the first coordinate unchanged

    if head.direction == "down":
        y = head.ycor() 
        head.sety(y - 20) 

    if head.direction == "left":
        x = head.xcor() 
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor() 
        head.setx(x + 20) 


#keyboard bindings
windo.listen()
windo.onkeypress(go_up, "Up")
windo.onkeypress(go_down, "Down")
windo.onkeypress(go_left, "Left")
windo.onkeypress(go_right, "Right")


#main game loop
while True:
    windo.update()

    #check for collison with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)
        
        #clear the segments list
        segments.clear()

        #reset score
        score = 0
        pen.clear()
        pen.write("score: {} High Score: {}".format(score, high_score), align = "center", font=("courier",15,"normal"))

        #reset the delay 
        delay = 0.15

        
    #check for collison with food
    if head.distance(food) < 20:
        #move food to random spot on screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001

        #increase the store
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score: {} High Score: {}".format(score, high_score), align = "center", font=("courier",15,"normal"))

    # move end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
#move segment zero to where head is
    if len(segments) > 0:
        x =head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    move() #calling the function

    #check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop" 

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
        
            #clear the segments list
            segments.clear()

            #reset score
            score = 0
            pen.clear()
            pen.write("score: {} High Score: {}".format(score, high_score), align = "center", font=("courier",15,"normal"))

            #reset the delay 
            delay = 0.15

    time.sleep(delay)



windo.mainloop()
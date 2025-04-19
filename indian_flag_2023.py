import turtle
#screen size
turtle.setup(800,750)
#main program code 
t = turtle.Turtle()

t.speed(0)

t.pencolor("orange")
t.fillcolor("orange")
t.begin_fill()
t.up()
t.goto(-180,110)
t.down()
for i in range(2):
    t.forward(375)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()


t.up()
t.goto(0,0)
t.down()

#ashok chakra 
t.pencolor("blue")
t.circle(50)

for i in range(16):
    t.goto(0,50)
    t.right(80)
    t.forward(50)
    t.left(90)
    t.circle(50 ,14)
for i in range(1):
    t.circle(50)

t.pencolor("green")
t.fillcolor("green")
t.begin_fill()

t.up()
t.goto(-180,-90)
t.down()
t.right(24)
for i in range(2):
    t.forward(375)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.pencolor("black")
t.up()
t.goto(-180,190)
t.down()
t.right(180)
t.forward(40)
t.left(90)
t.forward(561)
t.left(90)
t.forward(40)
t.left(90)
t.forward(561)
t.end_fill()

t.up()
t.goto(-320 , -400)
t.down()
t.right(90)

t.fillcolor("brown")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.left(90)
    t.forward(28)
    t.left(90)
t.end_fill()


t.penup()  # Lift the pen
t.goto(200, -200)  # Move to the starting coordinates
t.pendown()  # Lower the pen

# Write text using the write() function
text = "Happy Independence Day!"
t.write(text, align="center", font=("Helvetica", 20, "normal"))
t.forward(100)

turtle.done()






    

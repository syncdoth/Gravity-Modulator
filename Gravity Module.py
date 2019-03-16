import turtle

#d= vi*t + a*t**2

#vf = vi + a*t

#vf**2 = vi**2 + 2*a*d

#d = (vi+vf)*t/2

turtle.setworldcoordinates(0,0,1000,1000)
turtle.tracer(False)

draw = turtle.Turtle()
draw.up()
draw.hideturtle()
draw.goto(0,500)
draw.down()
draw.begin_fill()
for _ in range(2):
    draw.forward(200)
    draw.right(90)
    draw.forward(500)
    draw.right(90)
draw.end_fill()

draw.up()
draw.goto(0,0)
draw.down()
draw.width(10)

for _ in range(4):
    draw.forward(1000)
    draw.left(90)
draw.up()
#draw.goto(100, 950)
#draw.write("velocity: ", font=("Arial", 15), align ="center")
#draw.setx(600)
#draw.write("time elapsed: ", font=("Arial", 15), align ="center")

turtle.addshape("piston.gif")
piston = turtle.Turtle()
piston.shape("piston.gif")
piston.up()
piston.goto(-60,550)

ball = turtle.Turtle()
ball.up()
ball.shape("circle")
ball.shapesize(3,3)
ball.goto(45,546)
turtle.update()

writing = turtle.Turtle()
writing.up()
writing.hideturtle()
writing.goto(500,800)
writing.write("Gravity Moduator", font=("Arial", 50), align ="center")
writing.sety(writing.ycor()-70)
writing.write("press enter to begin:", font=("Arial", 50), align ="center")


m_piston = 1
m_ball = 1
g=-980
vix=0
viy=0
time=0

i=0
r=0
def updatescreen():
    global vix, viy, time, i, F, r

    writing.clear()
    if i==0:
        setforce = turtle.textinput("Physics Engine","set force (in Newtons, max 3000): ")
        if setforce == "":
            setforce = turtle.textinput("Physics Engine","set force (in Newtons, max 3000): ")
        else:
            setforce = float(setforce)
            F=setforce
            i=1
    a=100*F/(m_piston + m_ball)
    
    if ball.xcor()<200 and vix >= 0:
        piston.setx(piston.xcor()+vix/100)
        vix += a/100
        
    if not ball.xcor()<200:
        viy += g/100

    if ball.ycor()<=55 and viy <0:
        viy = -viy/2

    if ball.xcor()>=945 and vix > 0:
        vix = -vix/2

    if ball.xcor()<=245 and vix < 0:
        vix = -vix/2

    ball.setx(ball.xcor()+vix/100)
    ball.sety(ball.ycor()+viy/100)
    turtle.update()
    if r == 0:
        print(r)
        turtle.ontimer(updatescreen, 1)
        
def reset():
    global r
    r =1
    i=0
    piston.goto(-60,550)
    ball.goto(45,546)
    vix=0
    viy=0
    time=0

    writing.goto(500,800)
    writing.write("Gravity Moduator", font=("Arial", 50), align ="center")
    writing.sety(writing.ycor()-70)
    writing.write("press enter to begin:", font=("Arial", 50), align ="center")

    turtle.update()

    

turtle.onkeypress(updatescreen,"Return")
turtle.onkeypress(reset, "space")

turtle.listen()
turtle.done()

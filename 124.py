import turtle as trtl
import random
#variables for maze
width = 20
squares = 10
angle = 90
wn = trtl.Screen()
wn.bgcolor("black")
#turtle setup
drawer = trtl.Turtle()
mazedude = trtl.Turtle()
mazedude.color("white")
drawer.speed(0)
drawer.ht()
drawer.pensize(10)
drawer.color("blue")
def wallspace():
    test2 = random.randint(1,3)
    if test2 > 2:
        drawer.penup()
        drawer.forward(25)
        drawer.pendown()
    else:
        drawer.forward(25)
def barrier():
    if counter1 > 4:
        test = random.randint(1,2)
        if test > 1:
            drawer.left(90)
            drawer.forward(width)
            drawer.right(180)
            drawer.forward(width)
            drawer.left(90)
def barrier2():
    if counter1 > 20:
        test = random.randint(1,4)
        if test > 3:
            drawer.left(90)
            drawer.forward(width)
            drawer.right(180)
            drawer.forward(width)
            drawer.left(90)


def up():
    mazedude.forward(5)
def down():
    mazedude.forward(-5)
def left():
    mazedude.left(90)
def right(): 
    mazedude.right(90)

#make maze
counter1 = 0
while counter1 < (squares*4):
    length = (15+(counter1*width))
    drawer.forward(length/8)
    barrier2()
    wallspace()
    drawer.forward(length/10)
    barrier2()
    wallspace()
    drawer.forward(length/11)
    wallspace()
    barrier2()
    drawer.forward(length/10)
    wallspace()
    barrier()
    drawer.forward(length/12)
    wallspace()
    barrier()
    drawer.forward(length/12)
    wallspace()
    drawer.forward(length/10)
    barrier()
    wallspace()
    drawer.left(angle)
    counter1 += 1
   



wn = trtl.Screen()

wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")

wn.listen()

wn.mainloop()


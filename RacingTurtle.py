import turtle as t
import random



sc=t.Screen()
sc.setup(height=500,width=600)#khiung man hinh
pen=t.Turtle(visible=False)#an nut 
pen.penup()#dat but
pen.speed(28)
pen.goto(-250,200)
#ve ben tren cung
for i in range(21):
    pen.write(i)
    pen.forward(25)

x=-250
pen.goto(-250,200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x+(i+1)*25,200)

tatca_rua =[]
vitri_y=[160,100,40,-20]
colors = ['red', 'green', 'blue', 'black']
for rua in range(0,4):
    ruas=t.Turtle(shape="turtle")
    ruas.penup()
    ruas.goto(x=-250,y=vitri_y[rua])
    ruas.color(colors[rua])
    for i in range(5):
        ruas.left(72)

tatca_rua.append(ruas)

def random_walk(ruas):
    global run
    for turtle in ruas:
        turtle.forward(random.randint(1, 10))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False

run = True
while run:
    random_walk(tatca_rua)
sc.exitonclick()





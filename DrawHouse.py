from turtle import *

#toc do
speed(7)

#grass
bgcolor("green")

#sky
penup()
goto(-400,-100)
pendown()
color("deepskyblue")
begin_fill()


for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

#tree

penup()
goto(175,-15)
pendown()
pensize(0.5)
color("black","brown")
begin_fill()
for i in range (2):
    forward(30)
    right(90)
    forward(90)
    right(90)
end_fill()

penup()
goto(145,-15)
pendown()
pensize(0.5)
color("black","forest green")
begin_fill()
for i in range(3):
    forward(90)
    left(120)
end_fill()
penup()
goto(155,50)
pendown()
pensize(0.5)
color("black","forest green")
begin_fill()
for i in range(3):
    forward(70)
    left(120)
end_fill()

penup()
goto(165,100)
pendown()
pensize(0.5)
color("black","forest green")
begin_fill()
for i in range(3):
    forward(50)
    left(120)
end_fill()

#sun 
penup()
goto(110,198)
pendown()
color("yellow")
begin_fill()
circle(30)
end_fill()

#cloud
penup()
goto(-200,200)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()

penup()
goto(-250,200)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()


penup()
goto(-220,180)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()

penup()
goto(-230,210)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()

#house
penup()
goto(-210,0)
pendown()
pensize(1)
color("black","blue")
begin_fill()

for i in range (2):
    forward(120)
    right(90)
    forward(150)
    right(90)
end_fill()
#window
penup()
goto(-170,-80)
pendown()
pensize(0.5)
color("black","green")
begin_fill()

for i in range (2):
    forward(40)
    right(90)
    forward(70)
    right(90)

end_fill()


#roof ngoi' nha
penup()
goto(-210,0)
pendown()
pensize(0.5)
color("black","light pink")
begin_fill()
for i in range(3):
    forward(120)
    left(120)
end_fill()

#mat chieu cua ngoi nha
penup()
goto(-90,-150)
pendown()
pensize(1)
color("black","yellow")
begin_fill()


left(30)
forward(80)
left(60)
forward(150)
left(120)
forward(80)

end_fill()

#mat chieu cua mai ngoi nha
penup()
goto(-90,0)
pendown()
pensize(1)
color("black","orange")
begin_fill()

backward(80)
right(90)
forward(120)
left(90)
forward(80)

end_fill()

#cua so nho
penup()
goto(-50,-30)
pendown()
pensize(1)
color("black","red")
begin_fill()

for i in range(4):
    forward(20)
    right(90)
    
end_fill()













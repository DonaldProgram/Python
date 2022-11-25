import turtle

window = turtle.Screen()
turtle.fillcolor("tomato")
turtle.begin_fill()
turtle.pendown()



for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.penup()
turtle.forward(100)

turtle.pendown()
for i in range(3):
    turtle.forward(80)
    turtle.left(120)

turtle.penup()
turtle.forward(80)

turtle.pendown()
for i in range(3):
    turtle.forward(60)
    turtle.left(120)

turtle.penup()
turtle.forward(60)

turtle.pendown()
for i in range(3):
    turtle.forward(40)
    turtle.left(120)

turtle.penup()
turtle.forward(40)

turtle.pendown()
for i in range(3):
    turtle.forward(20)
    turtle.left(120)

turtle.penup()
turtle.forward(20)




turtle.end_fill()
window.exitonclick()

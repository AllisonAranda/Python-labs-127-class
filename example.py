import turtle
wn = turtle.Screen()

flower = turtle.Turtle()
flower.color("lightblue")

for i in range(36):
    flower.forward(100)
    flower.left(140)
    flower.forward(10)
    flower.right(90)
    flower.forward(10)
    flower.left(135)
    flower.forward(100)

wn.exitonclick()
 

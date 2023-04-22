#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: February 16,2022
#This program draws a flower

import turtle
wn = turtle.Screen()

flower = turtle.Turtle()
flower.color("lightblue")

for i in range(36):
    flower.forward(100)
    flower.left(145)
    flower.forward(10)
    flower.right(90)
    flower.forward(10)
    flower.left(135)
    flower.forward(100)

wn.exitonclick()
 

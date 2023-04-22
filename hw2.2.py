#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: February 13,2022
#This program drawa an octagon

import turtle
wn = turtle.Screen()

octagon = turtle.Turtle()
octagon.color("blue")

for i in range(8):
    octagon.forward(100)
    
    octagon.left(450/10)


wn.exitonclick()

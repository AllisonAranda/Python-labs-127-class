#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 16,2022
#This program prints

import turtle

string=input("Enter something:")

al=turtle.Turtle()

for c in string:
    if c == "F":
        al.forward(50)
    elif c == "L":
        al.left(90)
    elif c == "R":
        al.right(90)
    elif c == "^":
        al.penup()
    elif c == "v":
        al.pendown()
    elif c == "B":
        al.backward(50)
    elif c == "S":
        al.stamp()
    elif c == "1":
        al.left(45)
    elif c == "r":
        al.right(45)
    elif c == "p":
        al.pencolor("purple")

        
        
        

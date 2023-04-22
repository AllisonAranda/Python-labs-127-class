#Allison Aranda
#Email:allison.aranda48@myhunter.cuny.edu
#Date:  April 27,2022

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,359,1)
  trey.right(a)

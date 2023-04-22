#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: February 28,2022
#This program prints out a shade  


import turtle				

turtle.colormode(255)		#Allows colors to be given as 0...255
ballon = turtle.Turtle()		
ballon.shape("turtle")		#Make it turtle shaped
ballon.backward(100)		#Move her backwards, to give more space to draw


for i in range(0,255,10):
     ballon.forward(10)		#Move forward
     ballon.pensize(i)		#Set the drawing size to be i (larger each time)
     ballon.color(0,0,i)
     #R,G,B

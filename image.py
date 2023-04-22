#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: February 28,2022
#This program prints out a shade  #Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: February 28,2022
#This program prints out a image in blue color

import matplotlib.pyplot as plt
import numpy as np
mess = input("Enter name of the input file")
out = input("Enter name of the output file")

img = plt.imread(mess)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0
img2[:,:,0] = 0          #Set the blue channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave(out, img2)  #Save the image we created to the file: reds.png

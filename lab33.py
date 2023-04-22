#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 30,2022
#This program prints an image

import matplotlib.pyplot as plt
import numpy as np

img= input("Enter image file name:")
output= input("Enter output file:")

al= plt.imread(img)

height = al.shape[0] 
width = al.shape[1]

#new img

img2= al[height//2:, :width//2]



#plt.imshow(img2)
#plt.show()
plt.imsave(output,img2)

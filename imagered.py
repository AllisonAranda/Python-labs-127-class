#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 09,2022
#This program prints out

import matplotlib.pyplot as plt
import numpy as np

num=int(input("Enter size"))
file=input("Enter output file:")

img=np.ones((num,num,3))
img[::2,:,1:] = 0


plt.imsave(file, img)

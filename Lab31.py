#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 28,2022
#This program prints shelter population over time

import matplotlib.pyplot as plt
import pandas as pd

file = input("Enter name of input file:")
outputfile= input("Enter name of output file:")

al= pd.read_csv(file)
   
al["Fraction Children"]=al["Total Children in Shelter"]/al["Total Individuals in Shelter"]

al.plot(x="Date of Census" , y="Fraction Children")

fig=plt.gcf()
fig.savefig(outputfile)
            

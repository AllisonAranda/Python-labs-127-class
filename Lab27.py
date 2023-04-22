#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 21,2022
#This program prints


import matplotlib.pyplot as plt
import pandas as pd
b = input("Enter borough name:")
file = input("Enter output file name:")

#Open the CSV file and store in pop
pop = pd.read_csv("nycHistPop.csv",skiprows=5)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[b]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(file)

#plt.show()

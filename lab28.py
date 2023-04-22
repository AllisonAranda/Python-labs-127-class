#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 21,2022
#This program prints


import matplotlib.pyplot as plt
import pandas as pd

b = input("Enter borough name:")
pop = pd.read_csv("nycHistPop.csv",skiprows=5)

print("Average population:",pop[b].max())
print("Maximum population:",pop[b].mean())



  

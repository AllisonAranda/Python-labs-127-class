#Allison Aranda
#Email: allison.aranda48@myhunter.cuny.edu
#Date:  April 07,2022

import pandas as pd

enter=input("Enter CSV file name:")

file=pd.read_csv(enter)



print("Top three contributing factors for collisions:")

#CONTRIBUTING FACTOR VEHICLE 1
print(file["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])



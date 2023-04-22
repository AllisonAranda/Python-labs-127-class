#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 30,2022
#This program prints

import pandas as pd

file = input("Enter file name")
search= input("Enter attribute")

tickets = pd.read_csv(file)		


print("The 10 worst offenders are:")
print(tickets[search].value_counts()[:10]) 

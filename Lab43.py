#Allison Aranda
#Email: allison.aranda48@myhunter.cuny.edu
#Date:  April 11,2022

import pandas as pd

enter=input("Enter CSV file name:")
file=pd.read_csv(enter)
output=input("Enter output file")

themap=folium.Map(location=[0,0])
folium.Marker(location=[0,0], popup="").add_to(themap)

themap.save(outfile="thMap.html")

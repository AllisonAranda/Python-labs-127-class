#Allison Aranda
#Email:allison.aranda48@myhunter.cuny.edu
#Date:  April 26,2022

import folium
import pandas as pd
def getData():
    theinput=input ("Enter the CV file name: ")
    df=pd. read_csv (theinput)
    return (df)

def getColumnNames():
    NameLON=input ('enter the name of longitude: ')
    NameLAT=input ('enter the name of lattitude: ')
    return (NameLON ,NameLAT)

def getLocale():
    theLat=input ("Enter the current Latitude")
    theLon=input ("Enter the current Longitude")
    return ((theLat) , (theLon) )

def computeDist (x1, y1, x2, y2) :
    d=00
    d= ((x1-x2) **2) + ( (y1-y2) **2)
    return (d)

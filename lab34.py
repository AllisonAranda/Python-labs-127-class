#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 30,2022
#This program prints an image

names=input("Please enter your list of names:")

names=names.split("; ")

for i in names:
    print(i.split(", ")[1],i.split(", ")[0])


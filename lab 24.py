#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 16,2022
#This program prints

list=input("Enter nouns:")

Numb=list.count(" ")+1

print(Numb)

plural=list.count("s ")

print(plural)

if list[-1] == "s":
    plural=plural+1

print(plural/Numb)


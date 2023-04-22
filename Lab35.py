#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 30,2022
#This program prints

hour=int(input("Enter hour (in 24 hour time):"))

if hour < 12:
    print("Good Morning")
elif hour >= 12 and hour<17:
    print("Good Afternoon")
else:
    print("Good Evening")

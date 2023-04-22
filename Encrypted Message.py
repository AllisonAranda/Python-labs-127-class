#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: February 25,2022
#This program prints out a encrypted message


mess = input("enter a word")
print(mess)

for i in mess:
    print(chr((ord(i)-97+13)%26+97),end="")
      

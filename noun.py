#Name: Allison
#Email: allison.aranda48@myhunter.cuny.edu
#Date: March 09,2022
#This program prints out

template="If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."

noun=input("Enter a noun:")
verb1=input("Enter a verb:")
verb2=input("Enter another verb:")

template = template.replace("NOUN", noun)

template = template.replace("VERB1", verb1)
template = template.replace("VERB2", verb2)

print(template)

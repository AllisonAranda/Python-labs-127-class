#Allison Aranda
#Email:allison.aranda48@myhunter.cuny.edu
#Date:  May 04,2022

ADDI $s0, $zero, 50 #set s0 to 10
ADDI $s1, $zero, 5  #use to decrement counter, $s0
AGAIN: SUB $s0, $s0, $s1
BEQ $s0, $zero, DONE
J AGAIN
DONE:  #To break out of the loop

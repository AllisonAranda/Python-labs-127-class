#Allison Aranda
#Email: allison.aranda48@myhunter.cuny.edu
#Date:  April 11,2022

def computeFare(zone, ticketType):
    computeFare = ""
    
    if zone == 1 and ticketType== "peak":
        fare = 8.75
    elif zone == 1 and ticketType== "off-peak":
        fare = 6.25
    elif (zone == 2 or zone==3) and ticketType== "peak":
        fare = 10.25
    
    elif (zone == 2 or zone==3) and ticketType== "off-peak":
        fare = 7.50
    elif zone == 4 and ticketType== "peak":
        fare = 12
    elif zone == 4 and ticketType== "off-peak":
        fare = 8.75
    elif (zone == 5 or zone==6 or zone==7) and ticketType== "peak":
        fare = 13.50
    elif (zone == 5 or zone==6 or zone==7) and ticketType== "off-peak":
        fare = 9.75
    elif zone >=8:
        return(-1)
    

    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
             

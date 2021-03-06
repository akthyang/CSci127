#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  Alicia Yang

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""

     while monthNum < 1 or monthNum > 12:
         monthNum = int(input("This is an invalid number. Please enter a value from 1 to 12: "))
     if monthNum == 1:
         monthString = "January"
     if monthNum == 2:
         monthString = "February"
     if monthNum == 3:
         monthString = "March"
     if monthNum == 4:
         monthString = "April"
     if monthNum == 5:
         monthString = "May"
     if monthNum == 6:
         monthString = "June"
     if monthNum == 7:
         monthString = "July"
     if monthNum == 8:
         monthString = "August"
     if monthNum == 9:
         monthString = "September"
     if monthNum == 10:
         monthString = "October"
     if monthNum == 11:
         monthString = "November"
     if monthNum == 12:
         monthString = "December"

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   

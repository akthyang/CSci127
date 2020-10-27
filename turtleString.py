#Modified by:  !YourNameHere!
#Email:      !YourEmailHere!
#A program that uses command strings to control turtle drawing

import turtle

#assign name to turtle
tess = turtle.Turtle()
#the graphics window
myWin = turtle.Screen()

#ask user for input
commands = input("Please enter a command string: ")

#list out the commands
for ch in commands:
    #perform action indicated by character
    if ch == 'F':
        tess.forward(50) #moves forward 50 steps
    elif ch == 'L':
        tess.left(90) #moves left 90
    elif ch == 'R':
        tess.right(90) #moves right 90
    elif ch == '^':
        tess.penup() #lifts pen
    elif ch == 'v':
        tess.pendown() #lowers pen
    elif ch == 'B':
        tess.backward(50) #moves backwards
    elif ch == 'S':
        tess.stamp() #makes a stamp
    elif ch == 'D':
        tess.dot() #stamps a dot
    elif ch == 'p':
        tess.color('purple') #turns purple
    elif ch == 'g':
        tess.color('green') #turns green
    elif ch == 'b':
        tess.color('blue') #turns blue
    else: #for any other characters orint error
        print("Error: do not know command:", c)

print("See graphics window for image")
myWin.exitonclick() #close window when clicked



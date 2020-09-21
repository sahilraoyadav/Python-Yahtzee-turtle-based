""" Program name: Yahtzee
    Allows the user to roll dices and freeze the dices.
"""
# Imports random and turtle
import random
import turtle
# Creates a Turtle and Screen
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
""" List of List for Dice Parameters for 5 dices. Lists the parameter in the order of
[turtle,x,y,width(no height because it is a square),line color, fill color, random number 1 to 6]"""
dice_parameter = [[turtle,-280,145,100,"black","white",random.randint(1,6)],
                  [turtle,-280,0,100,"black","white",random.randint(1,6)],
                  [turtle,-280,-145,100,"black","white",random.randint(1,6)],
                  [turtle,180,145,100,"black","white",random.randint(1,6)],
                  [turtle,180,0,100,"black","white",random.randint(1,6)]]
"""List of List for Button Parameters for 2 dices.Lists the parameter in the order of
[turtle,x,y,height,width,line color,fill color,text]"""
button_parameter = [[turtle,-280,-250,250,60,"black","gray","Roll"],
                    [turtle,75,-250,250,60,"black","gray","New Roll"]]
"""Draws a rectangle using turtle and X&Y coordinates and width & height and line color (lcolor) and fill color (fcolor) and text"""
def drawRectangle(turtle,x,y,width,height,lcolor,fcolor,text = None):
    my_turtle.up()
    #goes to x and y to draw rectangle
    my_turtle.goto(x,y)
    my_turtle.color(lcolor,fcolor)
    my_turtle.down()
    my_turtle.begin_fill()
    # Makes the dice using for loop
    for dicemaker in range(2):
        my_turtle.forward(width)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
    my_turtle.end_fill()
    #Draws the text
    if text:
        turtle.penup()
        turtle.goto(x+(width/2),y)
        turtle.write(text,font=("TimesNewRoman",30),align="center")
#Dras dots using turtle and X&Y coordinates and number of dots
def drawDots(turtle,x,y,ndots):
    #Sets the color of dots to black and hides the turtle 
    turtle.color("black")
    turtle.hideturtle()
    #If number of dots = 1
    if ndots == 1:
        # Draws one dot using for loop and X&Y coordinates
        for i in range(1):
            my_turtle.penup()
            my_turtle.goto(x+50,y+50)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            
    #If number of dots = 2
    if ndots == 2:
        # Draws two dot using for loop and X&Y coordinates
        for i in range(1):
            my_turtle.penup()
            my_turtle.goto(x+25,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+75,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
    #If number of dots = 3
    if ndots == 3:
        # Draws three dot using for loop and X&Y coordinates
        for i in range(1):
            my_turtle.penup()
            my_turtle.goto(x+25,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+50,y+50)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+75,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
    #If number of dots = 4
    if ndots == 4:
        # Draws four dot using for loop and X&Y coordinates
        for i in range(1):
            my_turtle.penup()
            my_turtle.goto(x+25,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+25,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+75,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+75,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
    #If number of dots = 5
    if ndots == 5:
        # Draws five dot using for loop and X&Y coordinates
        for i in range(1):
            my_turtle.penup()
            my_turtle.goto(x+25,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+25,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+50,y+50)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.penup()
            my_turtle.goto(x+75,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+75,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
    #If number of dots = 6
    if ndots == 6:
        # Draws six dot using for loop and X&Y coordinates
        for i in range(1):
            my_turtle.penup()
            my_turtle.goto(x+25,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+25,y+50)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+25,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.penup()
            my_turtle.goto(x+75,y+25)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.goto(x+75,y+50)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
            my_turtle.penup()
            my_turtle.goto(x+75,y+75)
            my_turtle.pendown()
            my_turtle.dot(10)
            my_turtle.penup()
"""drawDie uses the drawRectangle() function and the drawDots() function to draw a die at (x, y) with the width, pen color, fill color, and
number of dots."""              
def drawDie(turtle,x,y,width,lcolor,fcolor,ndots):
    drawRectangle(turtle,x,y,width,width,lcolor,fcolor)
    drawDots(turtle,x,y,ndots)
""" isWithin return True if the point(x,y) is within the rectangle clicked. The function takes in parameters such as upperLeftX, upperLeftY, width,
height,x,y"""
def isWithin(upperLeftX,upperLeftY,width,height,x,y):
    #checks to see if the click is within the X and Y bounds of the rectangle
    #Return True if in bounds for X and Y or False if not.
    if upperLeftX<x<upperLeftX+width:
        if upperLeftY<y<upperLeftY+height:
            return True
        else:
            return False
    else:
        return False

"""mouseClick listens for when the user clicks the mouse button and then provides the x and y coordinates of where the mouse point is located on the turtle window."""
def mouseClick(x,y):
    """ Iterates through the list of button_parameter to determine if a button is clicked.
        If a button is clicked then it calls buttonClick() function passing the button index"""
    for i in range(len(button_parameter)):
        #Sets b as button_parameter list
        b = button_parameter[i]
        #Checks to see if the click is within the dimension parameter for the buttons. If in the parameter then it calls the buttonClick funtion.
        if isWithin(b[1],b[2],b[3],b[4],x,y):
            buttonClicked(i)
    """ Iterates through the list of dice_parameter to determine if a dice is clicked.
        If a button is clicked then it calls diceClicked() function passing the die index"""
    for i in range(len(dice_parameter)):
        #Sets d as dice_parameter
        d= dice_parameter[i]
        #Checks to see if the click is within the dimension parameter for the die. If in the parameter then it calls the dieClick funtion.
        if isWithin(d[1],d[2],d[3],d[3],x,y):
            dieClicked(i)
""" dieClicked takes in the index number of die within the list of dice and then it changes the background color of the die.
    If the die is white then it will make it green or vice versa."""
def dieClicked(index):
    # Checks to see if the dice color is white
    if dice_parameter[index][5] == "white":
        #if color is white and the die is clicked then turn its color to green
        dice_parameter[index][5] = "green"
    else:
        # Changes the color of the die from green to white, if the die is clicked green. 
        dice_parameter[index][5] = "white"
    # redraws the dies using drawDie() function and dice_parameter list
    drawDie(turtle,dice_parameter[index][1],
            dice_parameter[index][2],
            dice_parameter[index][3],
            dice_parameter[index][4],
            dice_parameter[index][5],
            dice_parameter[index][6])
    turtle.update()
""" buttonClicked takes in the index number of buttons within the list of buttons parameters as argument.
    If the button is clicked then it will either do a new roll or roll the dice which are white"""
def buttonClicked(index):
    if index == 1:
        for i in range(len(dice_parameter)):
            #if the New Roll button is pressed then the green turns to white. The next for statement does the reDraw of the dice and sets the die to random number between 1 to 6.
            if dice_parameter[i][5] == "green":
                dice_parameter[i][5] = "white"
    for i in range(len(dice_parameter)):
            #if the dice is white and the roll or newRoll button is called then it assigns random numbers between 1 and 6 to the dice.
            if dice_parameter[i][5] == "white":
                dice_parameter[i][6] = random.randint(1,6)
            #Redraws the dice using dice_parameters
            drawDie(*dice_parameter[i])
def main():
    # Setus up the screen dimension and sets the background color
    my_turtle.ht()
    my_screen.setup(700,600,0,0)
    my_screen.bgcolor("blue")
    my_screen.tracer(0)
    #sets up the listener for mouse clicks 
    my_screen.onclick(mouseClick,1,True)
    # Draws the dice using dice parameters
    for i in dice_parameter:
        drawDie(*i)
    # Draws the button using button parameters
    for i in button_parameter:
        drawRectangle(*i)
    turtle.update()
    turtle.mainloop()
main()

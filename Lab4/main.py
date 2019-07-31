# Diego Garza
# Assignemnt X
# Date Due

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) and sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
turtle.screensize(200, 200, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#FF0000")
myPen.speed(10)
# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
#turtle.delay(100)

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n equals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
def goto_origin(myPen):
    myPen.home()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    # Can also be done with a for loop - Can you rewrite this function as such?
    myPen.begin_fill()
    # 0 deg.
    for i in range(4):
    	myPen.forward(intDim)
    	myPen.left(90)


    # myPen.forward(intDim)
    # myPen.left(90)
    # # 90 deg.
    # myPen.forward(intDim)
    # myPen.left(90)
    # # 180 deg.
    # myPen.forward(intDim)
    # myPen.left(90)
    # # 270 deg.
    # myPen.forward(intDim)
    # myPen.left(90)

    myPen.end_fill()  

# Here is an example of how to draw a box using the box function      
# Comment these two lines out when you draw your own images
# box(500)
# turtle.done()
 
# Challenge functions (2 bonus pts each) 
# def save_image(): # saves the screen to an image/vector file

# You have a function for boxes, can you make functions for circles and triangles?
# def circle(intRadius):
myPen.color("#FFA500")
myPen.speed(500)
def circle(intRadius):
	myPen.begin_fill()
	myPen.right(90)
	myPen.forward(200)
	myPen.left(90)
	for i in range(359):
		myPen.forward(intRadius)
		myPen.left(89)
	myPen.end_fill()

# circle(350)

myPen.color("#0000FF")
myPen.speed(10)
def triangle(intLength): #This can be an equilateral triangle, or not
	myPen.begin_fill()
	myPen.left(180)
	for i in range(3):
		myPen.forward(intLength)
		myPen.left(120)
	myPen.end_fill()
# triangle(500)
# turtle.done()

# turtle.bye()
# turtle.Turtle._screen = None
# turtle.TurtleScreen._RUNNING = True

# myPen = turtle.Turtle()


# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the 
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):
	# color_unicode_list = (open(path, "r")).readline()
	# print(color_unicode_list)
	

	big_list = []
	for i in (open(path, "r")):
		big_list.append(i)
	color_unicode_list = big_list[0]
	colors = color_unicode_list.split(",")
	print(colors)


	all_pixels = []
	for k in (range(1,len(big_list))):
		all_pixels.append(big_list[k])
		for j in len(all_pixels[1]):
			

	print(all_pixels)

	line1 = all_pixels[1]	




    # raise NotImplementedError
load_art('art/banana.txt')

# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
	raise NotImplementedError

# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask the if they would like to draw a different piece until they quit the program.

#Supposed to be ==
if __name__ != '__main__':
    # sample for loading art and calling draw
    pallet_1, pixels_1 = load_art('art/banana.txt')
    draw(pallet_1, pixels_1)
    # You need this to prevent the window from closing after drawing
    turtle.done()
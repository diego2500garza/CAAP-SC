# Diego Garza
# Assignemnt X
# Date Due

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) and sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
turtle.screensize(2000, 2000, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#FF0000")
myPen.speed(10)
boxSize = 10
# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
#turtle.delay(100)

# setting out box sizes to the n sq pixels per box

 

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
    myPen.penup()
    myPen.forward(intDim)
    myPen.pendown()
    #print("ONE DONE") TEST - check if one box has printed
# Here is an example of how to draw a box using the box function      
# Comment these two lines out when you draw your own images
# box(boxSize)
# turtle.done()
 
# Challenge functions (2 bonus pts each) 
# def save_image(): # saves the screen to an image/vector file

# You have a function for boxes, can you make functions for circles and triangles?
# def circle(intRadius):
def circle(intRadius):
	myPen.begin_fill()
	for i in range(360*2):
		myPen.forward(intRadius/120/2)
		myPen.left(1/2)
	myPen.end_fill()
	myPen.penup()
	myPen.forward(intRadius)
	myPen.pendown()
	#print("ONE DONE") TEST - check if one circle has printed

def triangle(intLength): #This can be an equilateral triangle, or not
	myPen.begin_fill()
	for i in range(3):
		myPen.forward(intLength)
		myPen.left(120)
	myPen.end_fill()
	myPen.penup()
	myPen.forward(intLength)
	myPen.pendown()
	#print("ONE DONE") TEST - check if one triangle has printed



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
	buge_list = (open(path, "r"))
	huge_list = buge_list.read().splitlines()
	
	big_list = []
	for i in huge_list:
		Code = i.split(",") #makes list into list. this is so OP
		big_list.append(Code)
	pallet = big_list[0]
	#print(pallet) TEST - can it print pallet correctly

	# pallet = random.split(',') #pallet is first line
	pixels = big_list[1:] #pixels is the rest
	# print(pixels)
	return pallet, pixels

# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
	choice = eval(input("What type of pixel?\n1) - Square\n2) - Triangle\n3) - Circle\n"))
	if choice == 1:
		pixel = box
	elif choice == 2:
		pixel = triangle
	elif choice == 3:
		pixel = circle
	for i in range(len(pixels)): #start going for each line
		for j in range(len(pixels)): #start going for each pixel in each line
			pixel_code = int(pixels[i][j]) #pixel_code is going to make the value of that cell to an integer
			pixel_color = pallet[pixel_code] # sets color to the corresponding pallet color code
			myPen.color(pixel_color) #reset myPen.color
			pixel(boxSize) #do that pixel
			#print(pixel_color) TEST - check if color pallete is right
		
		myPen.right(90) #turn downwards
		myPen.penup()
		myPen.forward(boxSize) #go downwards
		myPen.right(90) #turn to the left
		myPen.forward((len(pixels[i])*boxSize)) #go to the left
		myPen.left(180) #rotate back to look forward/right
		myPen.pendown()
		#print("GOOD") TEST - if it can go through one iteration


# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask the if they would like to draw a different piece until they quit the program.

if __name__ == '__main__':
    # sample for loading art and calling draw
    def choice():
	    choice = eval(input("\n1) - Banana\n2) - Mario\n3) - Pac-Man Ghost\n4) - Space Invaders\n5) - Mario Mushroom\n6) - Smile meme\n7) - Texas\n8) - Spider-Man!!!\n"))
	    if choice == 1:
	    	return "art/banana.txt"
	    elif choice == 2:
	    	return "art/mario.txt"
	    elif choice == 3:
	    	return "art/pacman.txt"
	    elif choice == 4:
	    	return "art/space.txt"
	    elif choice == 5:
	    	return "art/shroom.txt"
	    elif choice == 6:
	    	return "art/smile.txt"
	    elif choice == 7:
	    	return "art/texus.txt"
	    elif choice == 8:
	    	return "art/spider.txt"
	    #print(path) TEST -  to see if path is correct

    def again():
	    again = input("Would you like to draw something else?\nYes) - 1\nNo) - 2\n")
	    try:
	    	again == int(again)
	    except ValueError:
	    	exit(1)
	    if int(again) == 1:
	    	turtle.resetscreen()
	    	do_it()
	    elif int(again) == 2:
	    	exit(1)
	    	turtle.done()
    def do_it():
    	pallet_1, pixels_1 = load_art(choice())
    	turtle.tracer(500)
    	draw(pallet_1, pixels_1)
    	again()
    do_it()
    # You need this to prevent the window from closing after drawing
    turtle.done()
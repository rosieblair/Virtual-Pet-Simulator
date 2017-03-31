#virtualPet.py
	# By: Rosemary Blair
	# This program allows a user to care for a virtual pet.
	# The objective is to keep your pet happy, or else it will die.

from graphics import *
import time
import random

# Initialize global variables for pet's needs.
hunger = 0
fatigue = 0
stress = 0
day = 0

# This is the function that changes pet display image in response to its stats.
def changePicture(win):

	global hunger
	global fatigue
	global stress

	# These are the coordinates for the pet image display in the window.
	imgCenter = Point(162,180)
	
	# Each gif file is 250x250 pixels.
	default = Image(imgCenter,"default.gif")
	mild = Image(imgCenter,"mild.gif")
	spicy = Image(imgCenter,"spicy.gif")
	thaihot = Image(imgCenter,"thaihot.gif")
	death = Image(imgCenter,"gameOver.gif")

	# Update the display file to the pet's stats.
	if hunger > 99 or fatigue > 99 or stress > 99:
		Image.draw(death,win)
	elif hunger > 74 or fatigue > 74 or stress > 74:
		Image.draw(thaihot,win)
	elif hunger > 49 or fatigue > 49 or stress > 49:
		Image.draw(spicy,win)
	elif hunger > 24 or fatigue > 24 or stress > 24:
		Image.draw(mild,win)
	elif hunger > 0 or fatigue > 0 or stress > 0:
		Image.draw(default,win)


# This is the function that registers a 'button' click to satisfy a need.
# The 'button' is simulated by a user click in a bounded region of the window.
def buttonPress(win):
	
	global hunger
	global fatigue
	global stress

	mouseClick = win.checkMouse()
	# If the user clicks a 'button' that day...
	if mouseClick != None:
		# Evaluate the x-value to determine the user's input.
		x = mouseClick.getX()

		# If the x-value of the click coordinate falls in range of a button...
		if 244.0 < x < 291.0:
			# Evaluate its y-value to determine which button was chosen.
			y = mouseClick.getY()

			# These are the y-coordinates of the three potential buttons.
			# When a button is clicked, the corresponding stat decreases by 10.
			if 347.0 < y < 374.0:
				hunger -= 10
			elif 387.0 < y < 419.0:
				fatigue -= 10
			elif 427.0 < y < 454.0:
				stress -= 10


# This is the function that updates our variables as the user runs the game.
# Our updating variables are the day count and the stat levels.
def alive(win):

	global hunger
	global fatigue
	global stress
	global day
	
	day += 1

	# Random integers are added onto each stat once a day.
	addHunger = random.randint(1, 10)
	addFatigue = random.randint(1, 10)
	addStress = random.randint(1, 10)

	hunger += addHunger
	fatigue += addFatigue
	stress += addStress

	buttonPress(win)

	# These are the bounds that ensure stat levels fall between range 0-100.
	if hunger < 0:
		hunger = 0
	if hunger > 100:
		hunger = 100

	if fatigue < 0:
		fatigue = 0
	if fatigue > 100:
		fatigue = 100

	if stress < 0:
		stress = 0
	if stress > 100:
		stress = 100

	# Ensure that the day number display is centered in the window.
	if day < 10:
		dayNumber = Text(Point(172, 37), day)
	else:
		dayNumber = Text(Point(176, 37), day)


	# These are bars that display updated values of the pet's stats each day.
	# Scale the bars to correspond to the pet's stat value.
	fx2 = (3/2) * hunger
	feedLevel1 = Point(83, 350)
	feedLevel2 = Point((fx2 + 83), 370)
	feedLevel = Rectangle(feedLevel1, feedLevel2)
	feedLevel.setFill('Red')
	feedLevel.draw(win)

	rx2 = (3/2) * fatigue
	restLevel1 = Point(83, 390)
	restLevel2 = Point((rx2 + 83), 410)
	restLevel = Rectangle(restLevel1, restLevel2)
	restLevel.setFill('Blue')
	restLevel.draw(win)

	px2 = (3/2) * stress
	playLevel1 = Point(83, 430)
	playLevel2 = Point((px2 + 83), 450)
	playLevel = Rectangle(playLevel1, playLevel2)
	playLevel.setFill('Green')
	playLevel.draw(win)

	# Displays the day number in the window.
	dayNumber.draw(win)

	# Control the game's update speed.
	# Each day lasts five seconds in real-time.
	time.sleep(5)

	# Remove day number and stat level bars with each new day.
	# This avoids overlapping of text or objects as each value changes.
	dayNumber.undraw()
	feedLevel.undraw()
	restLevel.undraw()
	playLevel.undraw()

	changePicture(win)


# This is the function that contains the main control loop and creates GUI.
def main():

	# Before opening the graphic window, introduce the game.
	print ()
	print("Welcome to the Virtual Shelter!")
	print("Press 'Enter' to continue.")

	enter1 = input()

	# Print a simple set of instructions to the user.
	print("The goal of this game is to keep your new pet happy.")
	print("You can do this by satisfying its hunger, fatigue, and stress.")
	print("These stats increase with every new day.")
	print("You can tend to one stat per day, by pressing its matching button.")
	print("Press 'Enter' to continue.")

	enter2 = input() 

	# The user creates a name for the virtual pet.
	print("What would you like to name your new pet?")

	name = input()

	# Creates the window with the user's inputted pet name.
	win = GraphWin("My Virtual Pet", 320, 500)
	petName = Text(Point(160, 18), name)
	petName.draw(win)

	# Display the day number in the window.
	dayCount = Text(Point(157, 37), "Day ")
	dayCount.draw(win)

	# Display the different stats the user's pet has.
	hungerCount = Text(Point(56, 360), "Hunger  ")
	hungerCount.draw(win)

	fatigueCount = Text(Point(57, 400), "Fatigue  ")
	fatigueCount.draw(win)

	stressCount = Text(Point(55, 440), "Stress  ")
	stressCount.draw(win)

	# Draw bars to provide an outline of the stat bar levels in the window.
	feedBar1 = Point(83, 350)
	feedBar2 = Point(233, 370)
	feedBar = Rectangle(feedBar1, feedBar2)
	feedBar.draw(win)

	restBar1 = Point(83, 390)
	restBar2 = Point(233, 410)
	restBar = Rectangle(restBar1, restBar2)
	restBar.draw(win)

	playBar1 = Point(83, 430)
	playBar2 = Point(233, 450)
	playBar = Rectangle(playBar1, playBar2)
	playBar.draw(win)

	# Create 'buttons' to be clicked by the user.
	feedButton1 = Point(245, 348)
	feedButton2 = Point(290, 373)
	feedButton = Oval(feedButton1, feedButton2)
	feedButton.draw(win)
	feedCommand = Text(Point(269,361), "Feed")
	feedCommand.draw(win)

	restButton1 = Point(245, 388)
	restButton2 = Point(290, 413)
	restButton = Oval(restButton1, restButton2)
	restButton.draw(win)
	restCommand = Text(Point(268,401), "Rest")
	restCommand.draw(win)

	playButton1 = Point(245, 428)
	playButton2 = Point(290, 453)
	playButton = Oval(playButton1, playButton2)
	playButton.draw(win)
	playCommand = Text(Point(268,441), "Play")
	playCommand.draw(win)

	# Display the default image of the pet.
	default = Image(Point(162,180),"default.gif")
	Image.draw(default,win)

	# Control the game's update speed.
	time.sleep(5)

	# As long as the pet's stats have not reached the maximum value,
	# run the alive function to update the game as the user plays.
	while hunger < 100 and fatigue < 100 and stress < 100:
		alive(win)

	# When the alive function is no longer called, the user's pet has died.
	dayCount.undraw()
	# Inform user that his pet has died.
	youDied = Text(Point(160, 37), "Is Dead")
	youDied.draw(win)
	death = Image(Point(162,180),"gameOver.gif")
	Image.draw(death,win)
	# Fill all the stat level bars to black.
	feedBar.setFill('Black')
	restBar.setFill('Black')
	playBar.setFill('Black')

	# Wait for the user to click to exit the window.
	win.getMouse()

main()

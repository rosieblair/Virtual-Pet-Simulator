#virtualPet.py
	#by: Rosemary Blair
	#final project - CSC 2301
	#this program allows a user to care for a virtual pet
	#the objective is to keep your pet happy, or else it will die:(

from graphics import *
import time
import random

#setting global values for pet's needs
hunger = 0
fatigue = 0
stress = 0
day = 0

#function that changes pet image in response to need level
def changePicture(win):

	global hunger
	global fatigue
	global stress

	#coordinates for pet image
	imgCenter = Point(162,180)
	
	default = Image(imgCenter,"default.gif")
	mild = Image(imgCenter,"mild.gif")
	spicy = Image(imgCenter,"spicy.gif")
	thaihot = Image(imgCenter,"thaihot.gif")
	death = Image(imgCenter,"gameOver.gif") #death is imminent

	#set the pet image corresponding to severity of its needs
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


#function that registers a 'button' click to satisfy a need
def buttonPress(win):
	
	global hunger
	global fatigue
	global stress

	mouseClick = win.checkMouse()
	#if the user clicks a 'button' that day...
	if mouseClick != None:
		x = mouseClick.getX()

		#if the x-value falls in range of a button...
		if 244.0 < x < 291.0:
			y = mouseClick.getY()

			#checks which button was pressed by the click's y-value
			if 347.0 < y < 374.0:
				hunger -= 10
			elif 387.0 < y < 419.0:
				fatigue -= 10
			elif 427.0 < y < 454.0:
				stress -= 10


#function that updates pets stats and time as user runs game
def alive(win):

	global hunger
	global fatigue
	global stress
	global day
	
	day += 1

	addHunger = random.randint(1, 10)
	addFatigue = random.randint(1, 10)
	addStress = random.randint(1, 10)

	hunger += addHunger
	fatigue += addFatigue
	stress += addStress

	buttonPress(win)

	#bounds to ensure need levels fall between range 0-100
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

	if day < 10:
		dayNumber = Text(Point(172, 37), day)
	else:
		dayNumber = Text(Point(176, 37), day)


	#bar displays for need levels
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

	dayNumber.draw(win)

	time.sleep(5)

	dayNumber.undraw()
	feedLevel.undraw()
	restLevel.undraw()
	playLevel.undraw()

	changePicture(win)


#function that sets up GUI and contains main control loop
def main():

	print ()
	print("Welcome to the Virtual Shelter!")
	print("Press 'Enter' to continue.")

	enter1 = input()

	print("The goal of this game is to keep your new pet happy.")
	print("You can do this by satisfying its hunger, fatigue, and stress.")
	print("These stats increase with every new day.")
	print("You can tend to one stat per day, by pressing its matching button.")
	print("Press 'Enter' to continue.")

	enter2 = input() 

	print("What would you like to name your new pet?")

	name = input()

	win = GraphWin("My Virtual Pet", 320, 500)
	petName = Text(Point(160, 18), name)
	petName.draw(win)

	dayCount = Text(Point(157, 37), "Day ")
	dayCount.draw(win)

	hungerCount = Text(Point(56, 360), "Hunger  ")
	hungerCount.draw(win)

	fatigueCount = Text(Point(57, 400), "Fatigue  ")
	fatigueCount.draw(win)

	stressCount = Text(Point(55, 440), "Stress  ")
	stressCount.draw(win)

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

	default = Image(Point(162,180),"default.gif")
	Image.draw(default,win)

	time.sleep(5)

	#start game
	while hunger < 100 and fatigue < 100 and stress < 100:
		alive(win)

	#game over
	dayCount.undraw()
	youDied = Text(Point(160, 37), "Is Dead")
	youDied.draw(win)
	death = Image(Point(162,180),"gameOver.gif")
	Image.draw(death,win)
	feedBar.setFill('Black')
	restBar.setFill('Black')
	playBar.setFill('Black')

	win.getMouse()

main()
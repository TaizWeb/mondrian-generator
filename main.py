import random
import os.path

# Defining constant variables
HEIGHT = 800
WIDTH = 800
MINHEIGHT = 200
MINWIDTH = 200

# randomColor: Returns a random color
def randomColor():
	if random.random() > .67: # if the art should be colored
		colorChance = random.random() # determining the color used
		if colorChance < .33:
			return "red"
		elif colorChance > .67:
			return "blue"
		else:
			return "yellow"
	else:
		return "white"

# splitBoth: splits a rectangle horizontally and vertically
def splitBoth(x, y, width, height, rectangleList):
	horizontalSplit = round(random.random() * width)
	verticalSplit = round(random.random() * height)
	mondrian(x, y, horizontalSplit, verticalSplit, rectangleList)
	mondrian(x + horizontalSplit, y, width - horizontalSplit, verticalSplit, rectangleList)
	mondrian(x, y + verticalSplit, horizontalSplit, height - verticalSplit, rectangleList)
	mondrian(x + horizontalSplit, y + verticalSplit, width - horizontalSplit, height - verticalSplit, rectangleList)

# splitVertical: Splits a rectangle vertically
def splitVertical(x, y, width, height, rectangleList):
	verticalSplit = round(random.random() * height)
	mondrian(x, y, width, verticalSplit, rectangleList)
	mondrian(x, y + verticalSplit, width, height - verticalSplit, rectangleList)

# splitHorizontal: Splits a rectangle horizontally
def splitHorizontal(x, y, width, height, rectangleList):
	horizontalSplit = round(random.random() * width)
	mondrian(x, y, horizontalSplit, height, rectangleList)
	mondrian(x + horizontalSplit, y, width - horizontalSplit, height, rectangleList)

# mondrian: Generates rectangles based on rules to create mondrian art
def mondrian(x, y, width, height, rectangleList):
	if width > WIDTH / 2 and height > HEIGHT / 2:
		splitBoth(x, y, width, height, rectangleList)
	elif width > WIDTH / 2:
		splitHorizontal(x, y, width, height, rectangleList)
	elif height > HEIGHT / 2:
		splitVertical(x, y, width, height, rectangleList)
	else:
		if random.random() > .33:
			if width > MINWIDTH and height > MINHEIGHT:
				splitBoth(x, y, width, height, rectangleList)
			elif width > MINWIDTH:
				splitHorizontal(x, y, width, height, rectangleList)
			elif height > MINHEIGHT:
				splitVertical(x, y, width, height, rectangleList)
			else:
				rectangleList.append(generateRect(x, y, width, height, randomColor()))
		else:
			rectangleList.append(generateRect(x, y, width, height, randomColor()))

# generateRect: Returns a rect html tag with defined color and dimensions
def generateRect(x, y, width, height, color):
	if color == 'blue':
		rgb = "rgb(0,0,255)"
	elif color == 'red':
		rgb = "rgb(255,0,0)"
	elif color == 'yellow':
		rgb = "rgb(255,255,0)"
	else:
		rgb = "rgb(255,255,255)"

	return "<rect x='" + str(x) + "' y='" + str(y) + "' width='" + str(width) + "' height='" + str(height) + "' style='fill:"+rgb+";stroke-width:3;stroke:rgb(0,0,0)'/>"

# generateHTML: Writes the html file with mondrian art
def generateHTML():
	top = """
<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
	<svg width='800' height='800'>
"""
	rectangleList = []
	rectangles = mondrian(0, 0, WIDTH, HEIGHT, rectangleList)
	middle = ""
	for rectangle in rectangleList:
		middle += str(rectangle)

	bottom = """
</svg>
</body>
</html>
"""

	if os.path.exists("index.html"):
		f = open("index.html", "w+")
		f.write(top + middle + bottom)
		f.close()
	else:
		open("index.html", "a").close()
		generateHTML()

generateHTML()


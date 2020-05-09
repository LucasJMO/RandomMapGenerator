from turtle import *
import turtle
import time
# So if I'm going to be testing this map creation algorithm I'm going to need to actually be able to see the maps it produces
# Ideally this should be pretty simple, the goal is just iterate through a grid, if the 

def drawMap(grid):
	for i in range(0, len(grid)):
		for k in range(0, len(grid[i])):
			penup()
			if grid[i][k] & 0b1000: # So every spot on the grid contains a number between 0b0000 and 0b1111
				goto(15*k,15*(0-i)) # 0bABCD, A = left, B = top, C = right, D = bottom
				right(90)		    # So each if statements checks a particular digit and draws in that line if the digit is a 1
				pendown()
				forward(15)
				penup()
				left(90)
			if grid[i][k] & 0b0100:
				goto(15*k,15*(0-i))
				pendown()
				forward(15)
				penup()
			if grid[i][k] & 0b0010:
				goto(15*(k+1),15*(0-i))
				right(90)
				pendown()
				forward(15)
				penup()
				left(90)
			if grid[i][k] & 0b0001:
				goto(15*k,15*(-1-i))
				pendown()
				forward(15)
				penup()
	#time.sleep(5)
	#ts = turtle.getscreen()
	#ts.getcanvas().postscript(file="map.eps")
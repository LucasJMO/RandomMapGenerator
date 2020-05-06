import rooms #This is a bunch of room templates

def createMap(grid):
	print(len(grid))
	print(len(grid[0]))

createMap(rooms.grid50x50)



# Each room is an X by X grid, represented by a 2 dimensional array
# Each index of the array contains a binary number between 0 and 15, inclusive
# Each binary digit of a cell specifies which cell borders are solid and which are open
# 1st digit = left, 2nd digit = top, 3rd digit = right, 4th digit = bottom
# room6x6 as described above, would look like this
#
#  ______ 
# |      |
# |      |
# |      |
# |      |
# |      |
# |______|
#
# An empty 6x6 room

# Square footage
# 1x1 = 5
# 2x2 = 20
# 3x3 = 45
# 4x4 = 80
# 5x5 = 125
# 6x6 = 180
# 7x7 = 245

# Algorithm
# Start with grid of size X by X
# Partition the grid into rooms with stronger weightings on rooms of average size
#	10% very small
#	20% slightly smaller than average
#	40% average
# 	20% slightly bigger than average
#	10% very big

# Select a room layout of appropriate size for each room

# Add number of room exits between 1 and 4 inclusive, each room must be accessible from each other room
# could represent completed grid as weighted map? Where weak connection represents adjacent rooms and strong connection represents rooms which share a doorway
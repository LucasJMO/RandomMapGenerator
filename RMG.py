room1 = [[0b1100,0b0100,0b0100,0b0100,0b0100,0b0110],
         [0b1000,0b0000,0b0000,0b0000,0b0000,0b0010],
         [0b1000,0b0000,0b0000,0b0000,0b0000,0b0010],
         [0b1000,0b0000,0b0000,0b0000,0b0000,0b0010],
         [0b1000,0b0000,0b0000,0b0000,0b0000,0b0010],
         [0b1001,0b0001,0b0001,0b0001,0b0001,0b0011]]

print(room1)

# Each room is an X by X grid, represented by a 2 dimensional array
# Each index of the array contains a binary number between 0 and 15, inclusive
# Each binary digit of a cell specifies which cell borders are solid and which are open
# 1st digit = left, 2nd digit = top, 3rd digit = right, 4th digit = bottom
# room1 as described above, would look like this
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
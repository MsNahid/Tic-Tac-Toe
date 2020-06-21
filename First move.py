# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:17:29 2020

@author: mssna
"""
#input and replace
line = input("Enter cells: ")
cells = line.replace("_", " ")

# print grids
def print_grids():
    print(9 * "-")
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print(9 * "-")
print_grids()

def replacement(x, y):
    if x == 1 and y == 1:
        return 6
    elif x == 2 and y == 1:
        return 7
    elif x == 3 and y == 1:
        return 8
    elif x == 1 and y == 2:
        return 3
    elif x == 2 and y == 2:
        return 4
    elif x == 3 and y == 2:
        return 5
    elif x == 1 and y == 3:
        return 0
    elif x == 2 and y == 3:
        return 1
    return 2

# handle coordinates input
x = None
y = None
while(True):
    move = input("Enter the coordinates: ")
    coordinates = move.split()
    first = coordinates[0]
    second = None
    if not first.isdigit():
        print("You should enter numbers!")
        continue
    else:
        second = coordinates[1]
        if not second.isdigit():
            print("You should enter numbers!")
            continue
    x = int(first)
    y = int(second)
    if(x >= 4 or y >= 4 or x <= 0 or y <= 0):
        print("Coordinates should be from 1 to 3!")
        continue
    if cells[replacement(x, y)] != " ":
        print("This cell is occupied! Choose another one!")
        continue
    break

#final stage and fill the move
# fill with move
move_postion = replacement(x, y)
cells = cells[:move_postion] + "X" + cells[move_postion + 1:]
print_grids()



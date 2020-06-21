# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:13:00 2020

@author: mssna
"""


# write your code here
cells = input("Enter cells: ")

#print structure
print(9 * "-")
print(f'| {cells[0]} {cells[1]} {cells[2]} |')
print(f'| {cells[3]} {cells[4]} {cells[5]} |')
print(f'| {cells[6]} {cells[7]} {cells[8]} |')
print(9 * "-")

#row
first_row = str(cells[0] + cells[1] + cells[2])
second_row = str(cells[3] + cells[4] + cells[5])
third_row = str(cells[6] + cells[7] + cells[8])

#column
first_column = str(cells[0] + cells[3] + cells[6])
second_column = str(cells[1] + cells[4] + cells[7])
third_column = str(cells[2] + cells[5] + cells[8])

#diagonal
diagonal1 = str(cells[0] + cells[4] + cells[8])
diagonal2 = str(cells[6] + cells[4] + cells[2])

check = [first_row, second_row, third_row, first_column, second_column, third_column, diagonal2, diagonal1]

x = "XXX"
o = "OOO"

if x in check and o in check:
    print("Impossible")
elif x in check:
    print("X wins")
elif o in check :
    print("O wins")
elif "_" not in cells:
    print("Draw")
elif cells.count('X') >= cells.count('O') + 2 or cells.count('O') >= cells.count('X') + 2:
    print("Impossible")
else:
    print("Game not finished")







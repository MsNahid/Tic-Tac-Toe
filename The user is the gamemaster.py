# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:09:13 2020

@author: mssna
"""
# write your code here
obj = input("Enter cells: ")
print("---------")
one=""
for i in range(0, 3):
    one += obj[i]
    one += " "
print("| "+ one + "|")
two = ""
for i in range(3,6):
    two += obj[i]
    two += " "
print("| "+ two + "|")
three = ""
for i in range(6,9):
    three += obj[i]
    three += " "
print("| "+ three + "|")
print("---------")
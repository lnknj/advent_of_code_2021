#!/usr/bin/python3
import io
from math import floor

def sortByColumns(lines, col):
    zeros = []
    ones = []
    for line in lines:
        if line[col] == "1":
            ones.append(line)
        else:
            zeros.append(line)
    return zeros, ones

def filterCO2(lines, col):
    if len(lines) == 1:
            return lines
    zeros, ones = sortByColumns(lines, col)
    del(lines)
    if len(zeros) <= len(ones):
        return filterCO2(zeros, col + 1)
    else:
        return filterCO2(ones, col + 1)
     

def filterOxygen(lines, col):
    if len(lines) == 1:
        return lines
    zeros, ones = sortByColumns(lines, col)
    del(lines)
    if len(zeros) > len(ones):
        return filterOxygen(zeros, col + 1)
    else:
        return filterOxygen(ones, col + 1)
       
input = open("input.txt", "r")
lines = input.readlines()
input.close()

oxygenRating = int(filterOxygen(lines, 0)[0], 2)
co2Rating = int(filterCO2(lines, 0)[0], 2)

print("The oxygen rating is: " + str(oxygenRating))
print("The CO2 rating is: " + str(co2Rating))
print("The final result is: " + str(oxygenRating * co2Rating))
    
        

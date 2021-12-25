#!/usr/bin/python3
import io
from math import floor

linecount = 0
bitcount = [0,0,0,0,0,0,0,0,0,0,0,0]

input = open("input.txt", "r")

for line in input:
    linecount += 1
    for index, digit in enumerate(line):
        if digit == "1":
          bitcount[index] += 1

input.close()
print(bitcount)

# python numbers are weird
smallestMajority = floor(linecount / 2)
γRate = ""
εRate = ""
for numberOfOnes in bitcount:
    if numberOfOnes >= smallestMajority:
        γRate = γRate + "1"
        εRate = εRate + "0"
    else:
        γRate = γRate + "0"
        εRate = εRate + "1"

print(γRate)
print(int(γRate, 2))
print(εRate)
print(int(εRate, 2))
print("There were " + str(linecount) + " lines in the input.")
print("Number of ones for each position: " + str(bitcount))
print(int(εRate, 2) * int(γRate, 2))


import time
from util import read_stripped_lines

X = 1
Y = 0

def main():
    pipeMap = read_stripped_lines('input/day10test.text')
    startCoordinates = findStart(pipeMap)
    print(startCoordinates)

def showArea(coordinates, pipeMap):
    topbuffer = 0
    bottombuffer = 0
    leftbuffer = 0
    rightBuffer = 0

    if coordinates[Y] > 0: topBuffer = 1
    if coordinates[Y] < len(pipeMap)-1: bottombuffer = 1
    if coordinates[X] > 0: leftbuffer = 1
    if coordinates[X] < len(pipeMap[coordinates[Y]]): rightBuffer = 1

    for rowIndex in range(coordinates[Y] - topBuffer, coordinates[Y] + bottombuffer):
        print(pipeMap[rowIndex])


def findStart(pipeMap):
    for rowIndex, row in enumerate(pipeMap):
        for columnIndex, char in enumerate(row):
            if char == 'S':
                return (rowIndex, columnIndex)

main()
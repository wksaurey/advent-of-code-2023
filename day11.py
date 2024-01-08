from util import read_stripped_grid, manhattanDistance
import time

galaxy = read_stripped_grid('input/day11test.text')

def main():
    printGalaxy()

def expandGalaxy():
    # check column first
    # then check row
    columnEmpty = True
    for columnIndex, column in enumerate(galaxy):
        rowEmpty = True
        for rowIndex, char in enumerate(column):
            if char == '#':
                rowEmpty = False
                columnEmpty = False
                break

def printGalaxy():
    for line in galaxy:
        for char in line:
            print(char, end='')
        print()

if __name__ == '__main__':
    main()
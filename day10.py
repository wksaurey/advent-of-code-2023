import time
from util import read_stripped_lines

Y = 0
X = 1
coors = 0
steps = 1

pipeMap = read_stripped_lines('input/day10test.text')
lastMove = 'A'
reachedEnd = False

def main():
    totalSteps = 0
    coordinates = findStart()
    showArea(coordinates)
    queue = [[coordinates, 0]]
    # todo: create queuet to check every possible combination until it either dead-ends or finds the 'S'
    while not reachedEnd:
        info = queue.pop(0)
        totalSteps = info[steps]
        coordinates = getNextCoordinates(coordinates)
        showArea(coordinates)
        totalSteps += 1
        queue.append([coordinates, totalSteps])
    print(f'Total steps: {totalSteps}')
    
def getNextCoordinates(coordinates):
    global lastMove
    global reachedEnd
    topbuffer = 0
    bottombuffer = 0
    leftbuffer = 0
    rightbuffer = 0

    if coordinates[Y] > 0: topbuffer = 1
    if coordinates[Y] < len(pipeMap)-1: bottombuffer = 1
    if coordinates[X] > 0: leftbuffer = 1
    if coordinates[X] < len(pipeMap[coordinates[Y]]): rightbuffer = 1

    if lastMove == 'N': topbuffer = 0
    if lastMove == 'S': bottombuffer = 0
    if lastMove == 'E': rightbuffer = 0
    if lastMove == 'W': rightbuffer = 0

    if topbuffer:
        pipe = pipeMap[coordinates[Y]-topbuffer][coordinates[X]]
        if 'S' in getConnections(pipe):
            lastMove = 'S'
            return [coordinates[Y]-topbuffer, coordinates[X]]
    if bottombuffer:
        pipe = pipeMap[coordinates[Y]+bottombuffer][coordinates[X]]
        if 'N' in getConnections(pipe):
            lastMove = 'N'
            return [coordinates[Y]+bottombuffer, coordinates[X]]
    if leftbuffer:
        pipe = pipeMap[coordinates[Y]][coordinates[X]-leftbuffer]
        if 'E' in getConnections(pipe):
            lastMove = 'E'
            return [coordinates[Y], coordinates[X]-leftbuffer]
    if rightbuffer:
        pipe = pipeMap[coordinates[Y]][coordinates[X]+rightbuffer]
        if 'W' in getConnections(pipe):
            lastMove = 'W'
            return [coordinates[Y], coordinates[X]+rightbuffer]
    else:
        # check for S
        reachedEnd = True
        showArea(coordinates)


def getConnections(pipe):
    if pipe == '|': return ('N', 'S')
    elif pipe == 'J': return ('N', 'W')
    elif pipe == 'L': return ('N', 'E')
    elif pipe == '7': return ('S', 'W')
    elif pipe == 'F': return ('S', 'E')
    elif pipe == '-': return ('E', 'W')
    elif pipe == '.': return ('A', 'A')
    else: print('The pipe {pipe} is unknown')

def showArea(coordinates):
    topbuffer = 0
    bottombuffer = 0
    leftbuffer = 0
    rightbuffer = 0

    if coordinates[Y] > 0: topbuffer = 1
    if coordinates[Y] < len(pipeMap)-1: bottombuffer = 1
    if coordinates[X] > 0: leftbuffer = 1
    if coordinates[X] < len(pipeMap[coordinates[Y]]): rightbuffer = 1

    print(f'Coordinates: {coordinates}')
    print('~~~')
    for rowIndex in range(coordinates[Y] - topbuffer, coordinates[Y] + bottombuffer+1):
        print(pipeMap[rowIndex][coordinates[X]-leftbuffer: coordinates[X]+rightbuffer+1])
    print('~~~\n')


def findStart():
    for rowIndex, row in enumerate(pipeMap):
        for columnIndex, char in enumerate(row):
            if char == 'S':
                return (rowIndex, columnIndex)

main()
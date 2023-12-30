from util import read_stripped_lines

parts = read_stripped_lines('input/day3.text')
gearOne = None
gearTwo = None

def main():
    gearRatioSum = 0
    for lineIndex, line in enumerate(parts):
        for index, char in enumerate(line):
            global gearOne
            global gearTwo
            if gearOne != None and gearTwo != None:
                print(f'Gear ratio of {gearOne} and {gearTwo} is {gearOne*gearTwo}')
                gearRatioSum += (gearOne * gearTwo)
            gearOne = None
            gearTwo = None
            if char != '*':
                continue

            # print 3x3 around * for debug
            topBuffer = 1
            bottomBuffer = 1
            leftBuffer = 3
            rightBuffer = 3
            if lineIndex < topBuffer:
                topBuffer = 0
            if len(parts)-1 - lineIndex < bottomBuffer:
                bottomBuffer = 0
            if index < leftBuffer:
                leftBuffer = index
            if len(line)-1 - index < rightBuffer:
                rightBuffer = index-len(line)-1
            print('\n+-------+')
            for tempLineIndex in range(lineIndex-topBuffer, lineIndex+bottomBuffer+1):
                print(f'|{parts[tempLineIndex][index-leftBuffer:index+rightBuffer+1]}|')
            print('+-------+')


            # check left
            if index != 0:
                num = getNum(lineIndex, index-1)
                if num != None:
                    setGear(num)

            # check right
            if index+1 < len(line):
                num = getNum(lineIndex, index+1)
                if num != None:
                    setGear(num)

            # check top 3
            if lineIndex != 0:
                startbuffer = 0
                endbuffer = 0
                if index != 0:
                    startbuffer = 1
                if index+1 < len(line):
                    endbuffer = 1
                for tempIndex in range(index-startbuffer, index+endbuffer+1):
                    num = getNum(lineIndex-1, tempIndex)
                    if num != None:
                        setGear(num)
                        # check if two numers on top is possible
                        if parts[lineIndex-1][tempIndex+1].isdigit():
                            break
                    

            # check bottom 3
            if lineIndex != len(line)-1:
                startbuffer = 0
                endbuffer = 0
                if index != 0:
                    startbuffer = 1
                if index+1 < len(line):
                    endbuffer = 1
                for tempIndex in range(index-startbuffer, index+endbuffer+1):
                    num = getNum(lineIndex+1, tempIndex)
                    if num != None:
                        setGear(num)
                        # check if two numers on top is possible
                        if parts[lineIndex+1][tempIndex+1].isdigit():
                            break

    print(f'Sum: {gearRatioSum}')


def getNum(lineIndex, index):
    if lineIndex < 0 or lineIndex >= len(parts):
        return None
    if index < 0 or index >= len(parts[lineIndex]):
        return None
    if not parts[lineIndex][index].isdigit():
        return None

    startIndex = index
    while(startIndex > 0):
        if not parts[lineIndex][startIndex-1].isdigit():
            break
        startIndex -= 1

    endIndex = index
    while(endIndex < len(parts[lineIndex])-1):
        if not parts[lineIndex][endIndex+1].isdigit():
            break
        endIndex += 1

    return int(parts[lineIndex][startIndex:endIndex+1])

def setGear(num):
    global gearOne
    global gearTwo
    if gearOne == None:
        gearOne = num
        print(f'Gear One: {num}')
    elif gearTwo == None:
        gearTwo = num
        print(f'GearTwo: {num}')
    else:
        print('More than two gears were found')

main()
from util import read_stripped_lines

parts = read_stripped_lines('input/day3.text')
print(parts)
gearOne = None
gearTwo = None

def main():
    partNumberSum = 0
    for lineIndex, line in enumerate(parts):
        numLength = 0
        for index, char in enumerate(line):
            if numLength != 0:
                numLength -= 1
                continue
            if char != '*':
                continue

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

            # TODO: update up and down
            # check top 3
            if lineIndex != 0:
                startbuffer = 0
                endbuffer = 0
                if index != 0:
                    startbuffer = 1
                if index+1 < len(line):
                    endbuffer = 1
                isPartNumber = False
                for tempIndex in range(index-startbuffer, index+numLength+endbuffer):
                    if parts[lineIndex-1][tempIndex] != '.' and not parts[lineIndex-1][tempIndex].isdigit():
                        isPartNumber = True
                        print(f'{partNumber} is touching {parts[lineIndex-1][tempIndex]}')
                        partNumberSum += partNumber
                        break
                if(isPartNumber):
                    isPartNumber = False
                    continue
                
            # check down along length
            if lineIndex != len(line)-1:
                startbuffer = 0
                endbuffer = 0
                if index != 0:
                    startbuffer = 1
                if index+numLength < len(line):
                    endbuffer = 1
                for tempIndex in range(index-startbuffer, index+numLength+endbuffer):
                    if parts[lineIndex+1][tempIndex] != '.' and not parts[lineIndex+1][tempIndex].isdigit():
                        print(f'{partNumber} is touching {parts[lineIndex+1][tempIndex]}')
                        partNumberSum += partNumber
                        break

    print(f'Sum: {partNumberSum}')


def getNum(lineIndex, index):
    if lineIndex < 0 or lineIndex >= len(parts):
        return None
    if index < 0 or index >= len(parts[lineIndex]):
        return None
    if not parts[lineIndex][index].isdigit():
        return None

    startIndex = index
    while(startIndex > 0):
        if parts[lineIndex][startIndex-1].isdigit():
            startIndex -= 1

    endIndex = index
    while(endIndex < len(parts[lineIndex])):
        if parts[lineIndex][endIndex+1].isdigit():
            endIndex += 1

    return int(parts[lineIndex][startIndex:endIndex+1])

def setGear(num):
    if gearOne == None:
        gearOne = num
        print(f'Gear One: {num}')
    elif gearTwo == None:
        gearTwo = num
        print(f'GearTwo: {num}')
    else:
        print('More than two gears were found')

main()
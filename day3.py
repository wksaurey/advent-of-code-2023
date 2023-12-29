from util import read_stripped_lines

parts = read_stripped_lines('input/day3.text')
print(parts)

partNumberSum = 0
for lineIndex, line in enumerate(parts):
    numLength = 0
    for index, char in enumerate(line):
        if numLength != 0:
            numLength -= 1
            continue
        if not char.isdigit():
            continue
        # get num length
        numLength = 1
        while(index+numLength < len(line) and line[index+numLength].isdigit()):
            numLength += 1
        partNumber = int(line[index:index+numLength])

        # check left
        if index != 0:
            if line[index-1]!= '.' and not line[index-1].isdigit():
                print(f'{partNumber} is touching {line[index-1]}')
                partNumberSum += partNumber
                continue

        # check right
        if index+numLength < len(line):
            if line[index+numLength] != '.' and not line[index+numLength].isdigit():
                print(f'{partNumber} is touching {line[index+numLength]}')
                partNumberSum += partNumber
                continue

        # check up along length
        if lineIndex != 0:
            startbuffer = 0
            endbuffer = 0
            if index != 0:
                startbuffer = 1
            if index+numLength < len(line):
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

from util import read_stripped_lines
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

calibrations = read_stripped_lines('input/day1.text')
total = 0
for calibration in calibrations:
    print(f'Calibration: {calibration}')
    for index, char in enumerate(calibration):
        if char.isdigit():
            first = char
            print(f'First: {first}')
            break
        # check for spelled out numbers
        startIndex = index
        endIndex = index + 1
        possibleNumbers = numbers
        newNumbers = []
        first = None
        while(len(possibleNumbers) >= 1):
            for number in possibleNumbers:
                if(calibration[startIndex:endIndex] == number[0:endIndex - startIndex]):
                    if len(number) == endIndex - startIndex:
                        first = str(numbers.index(number)+1)
                        print(f'First: {first}')
                        break
                    newNumbers.append(number)
            if(first): 
                break
            possibleNumbers = newNumbers
            newNumbers = []
            endIndex += 1
        if(first):
            break
        
    print(f'Reversed Calibration: {calibration[::-1]}')
    reversedCalibration = calibration[::-1]
    for index, char in enumerate(reversedCalibration):
        if char.isdigit():
            second = char
            print(f'Second: {second}')
            break
        # check for reversed spelled out numbers
        startIndex = index
        endIndex = index + 1
        possibleNumbers = numbers
        newNumbers = []
        second = None
        while(len(possibleNumbers) >= 1):
            for number in possibleNumbers:
                number = number[::-1]
                if(reversedCalibration[startIndex:endIndex] == number[0:endIndex - startIndex]):
                    if len(number) == endIndex - startIndex:
                        second = str(numbers.index(number[::-1])+1)
                        print(f'Second: {second}')
                        break
                    newNumbers.append(number[::-1])
            if(second): 
                break
            possibleNumbers = newNumbers
            newNumbers = []
            endIndex += 1
        if(second):
            break

    # combine first and second
    value = int(first+second)
    print(f'End Value: {value} \n')
    total += value

print(f'Total: {total}')
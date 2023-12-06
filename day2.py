possibleValues = {'red': 12, 'green': 13, 'blue': 14}
totalIdSum = 0

for line in open('input/day2.text'):
    line = line.replace('Game ', '').replace(',', '').replace(';', '')
    line = line.split(':')
    gameid = int(line[0])
    valueInfo = line[1].split()
    valuePairs = []
    isValue = True
    for index, element in enumerate(valueInfo):
        if(isValue):
            valuePairs.append((element, valueInfo[index+1]))
            isValue = False
        else:
            isValue = True        
    gamePossible = True
    for valuePair in valuePairs:
        color = valuePair[1]
        value = int(valuePair[0])
        if value > possibleValues[color]:
            gamePossible = False
            print(f'{value} is too large for color {color}')
            break
    if(gamePossible):
        totalIdSum += gameid 
    print(f'Sum of Possible Game IDs: {totalIdSum}')
    #print(valuePairs)
    #print(gameid)

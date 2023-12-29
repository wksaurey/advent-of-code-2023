totalPowerSum = 0

for line in open('input/day2.text'):
    line = line.replace(',', '').replace(';', '')
    line = line.split(': ')[1]
    valueInfo = line.split()
    valuePairs = []
    isValue = True
    for index, element in enumerate(valueInfo):
        if(isValue):
            valuePairs.append((element, valueInfo[index+1]))
            isValue = False
        else:
            isValue = True        
    maxValues = {'red': 0, 'green': 0, 'blue': 0}
    for valuePair in valuePairs:
        color = valuePair[1]
        value = int(valuePair[0])
        if value > maxValues[color]:
            print(f'{color}: {value} is larger than {maxValues[color]}')
            maxValues[color] = value
    linePower = maxValues['red'] * maxValues['green'] * maxValues['blue'] 
    totalPowerSum += linePower
    print(f'Sum of Possible Game IDs: {totalPowerSum}')
    #print(valuePairs)
    #print(gameid)

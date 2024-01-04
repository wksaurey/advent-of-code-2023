import time
from util import read_stripped_lines

def main():
    starttime = time.time()
    dataSets = [list(map(int, set.split())) for set in read_stripped_lines('input/day9.text')]
    print(dataSets)

    extrapolatedSum = 0
    for dataSet in dataSets:
        derivatives = getDerivatives(list(reversed(dataSet)))
        extrapolatedValue = getExtrapolatedValue(derivatives)
        print(f'Extrapolated Value: {extrapolatedValue}')
        extrapolatedSum += extrapolatedValue
    print(f'Extrapolated Sum: {extrapolatedSum}')
    endtime = time.time()
    print(f'Run in {endtime-starttime} seconds')

def getExtrapolatedValue(derivatives):
    for index, derivative in enumerate(reversed(derivatives)):
        if index == 0:
            lastValue = derivative[-1]
            continue
        derivative.append(derivative[-1] + lastValue)
        lastValue = derivative[-1]
    return derivatives[0][-1]

def getDerivatives(dataSet):
    derivatives = [dataSet]
    while(True):
        derivative = []
        for index, value in enumerate(derivatives[-1]):
            if index == 0:
                continue
            derivative.append(value - derivatives[-1][index-1])
        if(isLastDerivative(derivative)):
            break
        derivatives.append(derivative)
    return derivatives


def isLastDerivative(values):
    lastDerivative = True
    for value in values:
        if value != 0:
            lastDerivative = False
            break
    return lastDerivative

main()
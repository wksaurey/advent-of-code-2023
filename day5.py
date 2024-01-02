def main():
    seeds = getSeeds()
    conversions = getConversions()

    START = 0
    RANGE = 1
    DELTA = 2

    for conversionIndex, conversionValues in enumerate(conversions):
        print(f'Current Conversion: {conversionValues}')
        print(f'Initial Seeds: {seeds}')
        for seedIndex, seedRange in enumerate(seeds):
            for conversionRange in conversionValues:
                if seedRange[START] >= conversionRange[START] and seedRange[START] + seedRange[RANGE]-1 <= conversionRange[START] + conversionRange[RANGE]-1:
                    seeds[seedIndex][START] = seedRange[START]+conversionRange[DELTA]


    print(f'Closest Location: {min(seeds)}')

def getSeeds(): 
    seeds = []
    with open('input/day5test.text') as file:
        line = file.readline()
        seedValues = list(map(int, line.split(':')[1].strip().split()))
        for seedIndex, seedValue in enumerate(seedValues):
            if seedIndex % 2 != 0 :
                continue
            seeds.append([seedValue, seedValues[seedIndex+1]])
    return seeds

def getConversions():
    conversions = []
    with open('input/day5test.text') as file:
        for line in file:
            if line == '\n':
                continue
            if ':' in line:
                if 'map' in line:
                    conversions.append([])
            else:
                values = list(map(int, line.strip().split()))
                conversions[-1].append([values[1], values[2], values[0]-values[1]])
    return conversions

main()
import time
filename = 'input/day5.text'

def main():
    starttime = time.time()
    seeds = getSeeds()
    conversions = getConversions()

    START = 0
    RANGE = 1
    DELTA = 2

    for conversionIndex, conversionValues in enumerate(conversions):
        print(f'Current Conversion: {conversionValues}')
        print(f'Initial Seeds: {seeds}')
        print('', end='')
        for seedIndex, seedRange in enumerate(seeds):
            for conversionRange in conversionValues:
                # start of conversion range is in seed range (not ends)
                if conversionRange[START] > seedRange[START] and conversionRange[START] < seedRange[START] + seedRange[RANGE]-1:
                    seeds[seedIndex] = [seedRange[START], conversionRange[START]-seedRange[START]]
                    seeds.append([conversionRange[START], seedRange[RANGE] - seeds[seedIndex][RANGE]])
                # end of conversion range is in seed range (not ends)
                if conversionRange[START] + conversionRange[RANGE]-1 > seedRange[START] and conversionRange[START] + conversionRange[RANGE]-1 < seedRange[START] + seedRange[RANGE]-1:
                    seeds[seedIndex] = [seedRange[START], conversionRange[START] + conversionRange[RANGE] - seedRange[START]]
                    seeds.append([conversionRange[START] + conversionRange[RANGE], seedRange[RANGE] - seeds[seedIndex][RANGE]])
                # whole range is bounded by conversion range, so update the whole range
                if seeds[seedIndex][START] >= conversionRange[START] and seeds[seedIndex][START] + seeds[seedIndex][RANGE]-1 <= conversionRange[START] + conversionRange[RANGE]-1:
                    seeds[seedIndex][START] = seedRange[START]+conversionRange[DELTA]
                    break

        print(f'Changed Seeds: {seeds}')
        print()


    minLocation = seeds[0][START]
    for seedRange in seeds:
        minLocation = min(minLocation, seedRange[START])
    print(f'Closest Location: {minLocation}')
    endtime = time.time()
    print(f'Run in {endtime-starttime} seconds')

def getSeeds(): 
    seeds = []
    with open(filename) as file:
        line = file.readline()
        seedValues = list(map(int, line.split(':')[1].strip().split()))
        for seedIndex, seedValue in enumerate(seedValues):
            if seedIndex % 2 != 0 :
                continue
            seeds.append([seedValue, seedValues[seedIndex+1]])
    return seeds

def getConversions():
    conversions = []
    with open(filename) as file:
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
>>>>>>> refs/remotes/origin/main

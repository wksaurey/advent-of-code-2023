seeds = []
conversions = []
with open('input/day5.text') as file:
    for line in file:
        if line == '\n':
            continue
        if ':' in line:
            if 'map' in line:
                conversions.append([])
            else:
                seeds = list(map(int, line.split(':')[1].strip().split()))
        else:
            values = list(map(int, line.strip().split()))
            conversions[-1].append([values[0]-values[1], values[1], values[1]+values[2]-1])
# print(conversions)

DELTA = 0
START = 1
END = 2

for conversionIndex, conversionValues in enumerate(conversions):
    print(f'Current Conversion: {conversionValues}')
    for seedIndex, seed in enumerate(seeds):
        for conversionValue in conversionValues:
            if seed >= conversionValue[START] and seed <= conversionValue[END]:
                seeds[seedIndex] = seed + conversionValue[DELTA]
                print(f'{seed} converted to {seeds[seedIndex]}')
    print(f'Seeds: {seeds}')

print(f'Closest Location: {min(seeds)}')
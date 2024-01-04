import time
from util import read_stripped_lines
import math

def main():
    starttime = time.time()
    commands = read_stripped_lines('input/day8.text')
    instructions = commands[0]
    nodeInfo = commands[2:]
    nodes = {}
    for index, node in enumerate(nodeInfo):
        node = node.split(' = ')
        name = node[0]
        children = node[1].replace('(', '').replace(')', '').replace(' ', '').split(',')
        nodes[name] = children

    # find all nodes ending with A
    destinations = []
    for node in nodes:
        if node[2] == 'A':
            destinations.append(node)

    print(destinations)
    pathLengths = []
    for destIndex, dest in enumerate(destinations):
        stepCount = 0
        while(destinations[destIndex][2] != 'Z'):

            index = stepCount % len(instructions)
            if instructions[index] == 'L':
                instruction = 0
            elif instructions[index] == 'R':
                instruction = 1
            else:
                print('Something is wrong')

            stepCount += 1
            destinations[destIndex] = nodes[destinations[destIndex]][instruction]
            # print(destinations[destIndex])

        print(f'Path {len(pathLengths)+1}: {stepCount}')
        pathLengths.append(stepCount)

    print(f'Path Lengths: {pathLengths}')
    while(len(pathLengths) > 1):
        pathLengths.append(lcm(pathLengths.pop(), pathLengths.pop()))
    print(f'Total Steps: {pathLengths[0]}')
    endtime = time.time()
    print(f'Run in {endtime-starttime} seconds')

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

main()
import time
from util import read_stripped_lines

commands = read_stripped_lines('input/day8test.text')
instructions = commands[0]
nodeInfo = commands[2:]
nodes = {}
dest = ''
for index, node in enumerate(nodeInfo):
    node = node.split(' = ')
    name = node[0]
    children = node[1].replace('(', '').replace(')', '').replace(' ', '').split(',')
    nodes[name] = children
    if index == 0:
        dest = name

print(dest)
stepCount = 0
while(dest != 'ZZZ'):
    index = stepCount % len(instructions)
    if instructions[index] == 'L':
        instruction = 0
    elif instructions[index] == 'R':
        instruction = 1
    else:
        print('Something is wrong')

    stepCount += 1

    dest = nodes[dest][instruction]
    print(dest)
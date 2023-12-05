from util import read_stripped_lines
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

calibrations = read_stripped_lines('input/day1.text')
total = 0
for calibration in calibrations:
    print(calibration)
    for char in calibration:
        if char.isdigit():
            first = char
            break
    for char in reversed(calibration):
        if char.isdigit():
            second = char
            break
    value = int(first+second)
    print(value)
    total += value

print(f'Total: {total}')
import math


total = 0
with open('input.txt', 'r') as f:
    for line in f:
        print(f'Total thus far: {total}')
        fuel_requirement = math.floor(int(line) / 3) - 2
        print(f'This module {int(line)} fuel requirement: {fuel_requirement}')
        total += fuel_requirement
print(total)

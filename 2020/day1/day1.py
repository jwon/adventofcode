from itertools import combinations

with open('input.txt') as f:
    for x,y in combinations((int(line.strip()) for line in f), 2):
        if x+y == 2020:
            print(f'{x}+{y}=2020; {x}*{y}={x*y}')

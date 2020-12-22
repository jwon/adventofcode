from itertools import combinations

with open('input.txt') as f:
    for x,y,z in combinations((int(line.strip()) for line in f), 3):
        if x+y+z == 2020:
            print(f'{x}+{y}+{z}=2020; {x}*{y}*{z}={x*y*z}')

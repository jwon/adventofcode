from itertools import accumulate, cycle

seen = {}
with open('inputs/1.txt', 'r') as f:
    for i in accumulate(map(int, cycle(f))):
        if i in seen:
            print(i)
            break
        seen[i] = True

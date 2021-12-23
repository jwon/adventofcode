from collections import defaultdict


grid = defaultdict(lambda: defaultdict(dict))
with open('input.txt') as f:
    for line in f:
        on_off, remains = line.strip().split(' ')
        on_off = on_off == 'on'
        cuboid = {}
        skip = False
        for dimension in remains.split(','):
            d_min, d_max = dimension.split('..')
            axis, d_min = d_min.split('=')
            d_min = int(d_min)
            d_max = int(d_max)
            if all(-50 <= a <= 50 for a in [d_min, d_max]):
                cuboid[axis] = (int(d_min), int(d_max)+1)
            else:
                print('out of bounds!', line)
                skip = True
                break
        if skip:
            continue
        for i in range(*cuboid['x']):
            for j in range(*cuboid['y']):
                for k in range(*cuboid['z']):
                    if on_off:
                        grid[i][j][k] = 1
                    else:
                        if k in grid[i][j]:
                            del grid[i][j][k]

total = 0
for i in grid:
    for j in grid[i]:
        total += len(grid[i][j])

print(total)

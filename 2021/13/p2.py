points = set()
folds = []
with open('input.txt') as f:
    for line in f:
        if ',' in line:
            points.add(tuple(int(i) for i in line.strip().split(',')))
        elif 'fold along' in line:
            if 'y=' in line:
                folds.append((None, int(line.strip().split('y=')[1])))
            elif 'x=' in line:
                folds.append((int(line.strip().split('x=')[1]), None))

print(points)
print(folds)
                
for idx, (x_fold, y_fold) in enumerate(folds):
    folded_points = set()
    if x_fold is None:  # horizontal fold
        for x, y in points:
            if y < y_fold:
                folded_points.add((x, y))
            else:  # need to reflect
                new_y = y_fold - (y - y_fold)
                folded_points.add((x, new_y))
    elif y_fold is None:  # vertical fold
        for x, y in points:
            if x < x_fold:
                folded_points.add((x,y))
            else:  # need to reflect
                new_x = x_fold - (x - x_fold)
                folded_points.add((new_x, y))
    points = folded_points
    print(f'After fold #{idx+1}: {len(points)}')

# graph it
x_max = 0
y_max = 0
for x_pos, y_pos in points:
    if x_pos > x_max:
        x_max = x_pos
    if y_pos > y_max:
        y_max = y_pos
grid = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]
for x_pos, y_pos in points:
    grid[y_pos][x_pos] = '#'

for row in grid:
    print(*row)
    
    

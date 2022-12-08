grid = []
visible = 0
with open('input.txt', 'r') as f:
    for line in f:
        grid.append([int(i) for i in line.strip()])

NUM_ROWS = len(grid)
for x in range(NUM_ROWS):
    NUM_COLUMNS = len(grid[x])
    if x == 0 or x == NUM_ROWS-1:
        visible += NUM_COLUMNS
    else:
        row = grid[x]
        # print(row)
        for y in range(NUM_COLUMNS):
            if y == 0 or y == NUM_COLUMNS-1:
                visible += 1
            else:
                height = row[y]
                # print(height)
                left_shorter = [True if row[idx] < height else False for idx in range(y)]
                right_shorter = [True if row[idx] < height else False for idx in range(y+1, NUM_COLUMNS)]
                top_shorter = [True if grid[idx][y] < height else False for idx in range(x)]
                bottom_shorter = [True if grid[idx][y] < height else False for idx in range(x+1, NUM_ROWS)]
                # print(left_shorter + ['THIS'] + right_shorter)
                # print(top_shorter + ['THIS'] + bottom_shorter)
                if all(left_shorter) or all(right_shorter) or all(top_shorter) or all(bottom_shorter):
                    # print('visible!')
                    visible += 1

print(visible)

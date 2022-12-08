grid = []
with open('input.txt', 'r') as f:
    for line in f:
        grid.append([int(i) for i in line.strip()])


def calc_viewing_distance(height, trees):
    viewing_distance = 0
    for i in trees:
        if i < height:
            viewing_distance += 1
        elif i >= height:
            # print(f'height: {height} trees: {trees} viewing_distance: {viewing_distance + 1}')
            return viewing_distance + 1
    # print(f'height: {height} trees: {trees} viewing_distance: {viewing_distance}')
    return viewing_distance


highest_scenic_score_seen = 0
NUM_ROWS = len(grid)
for x in range(NUM_ROWS):
    NUM_COLUMNS = len(grid[x])
    if x == 0 or x == NUM_ROWS-1:
        continue
    else:
        row = grid[x]
        # print(row)
        for y in range(NUM_COLUMNS):
            if y == 0 or y == NUM_COLUMNS-1:
                continue
            else:
                height = row[y]
                # print(height)
                left_viewing_distance = calc_viewing_distance(height, reversed(row[:y]))
                right_viewing_distance = calc_viewing_distance(height, row[y+1:])
                top_viewing_distance = calc_viewing_distance(height, reversed([grid[idx][y] for idx in range(x)]))
                bottom_viewing_distance = calc_viewing_distance(height, [grid[idx][y] for idx in range(x+1, NUM_ROWS)])

                scenic_score = left_viewing_distance * right_viewing_distance * top_viewing_distance * bottom_viewing_distance
                # print(f'scenic_score: {scenic_score}')
                if scenic_score > highest_scenic_score_seen:
                    highest_scenic_score_seen = scenic_score

print(highest_scenic_score_seen)

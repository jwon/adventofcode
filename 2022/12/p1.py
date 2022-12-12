from queue import PriorityQueue
import sys

grid = []
start_row_idx = None
start_col_idx = None
end_row_idx = None
end_col_idx = None

with open(sys.argv[1], 'r') as f:
    for raw_line in f:
        row = []
        for i in raw_line.strip():
            if i == 'S':
                start_row_idx = len(grid)
                start_col_idx = len(row)
                row.append(ord('a'))
            elif i == 'E':
                end_row_idx = len(grid)
                end_col_idx = len(row)
                row.append(ord('z'))
            else:
                row.append(ord(i))
        grid.append(row)

max_row = len(grid)
max_col = len(grid[0])
min_row = 0
min_col = 0

for row in grid:
    print(*row)
print(f'START: row: {start_row_idx} col: {start_col_idx}')
print(f'END: row: {end_row_idx} col: {end_col_idx}')


def dijkstra(grid, start_row_idx, start_col_idx):
    costs = [[float('inf') for _ in row] for row in grid]
    costs[start_row_idx][start_col_idx] = 0

    q = PriorityQueue()
    q.put((0, (start_row_idx, start_col_idx)))

    visited = set()

    while not q.empty():
        _, (curr_row, curr_col) = q.get()
        visited.add((curr_row, curr_col))
        adjacent = []
        max_possible_elevation = grid[curr_row][curr_col]+1
        if curr_col-1 >= min_col and grid[curr_row][curr_col-1] <= max_possible_elevation:  # left
            adjacent.append((curr_row, curr_col-1))
        if curr_col+1 < max_col and grid[curr_row][curr_col+1] <= max_possible_elevation:  # right
            adjacent.append((curr_row, curr_col+1))
        if curr_row-1 >= min_row and grid[curr_row-1][curr_col] <= max_possible_elevation: # up
            adjacent.append((curr_row-1, curr_col))
        if curr_row+1 < max_row and grid[curr_row+1][curr_col] <= max_possible_elevation:  # down
            adjacent.append((curr_row+1, curr_col))

        for next_row, next_col in adjacent:
            old_cost = costs[next_row][next_col]
            new_cost = costs[curr_row][curr_col] + 1
            if new_cost < old_cost:
                q.put((new_cost, (next_row, next_col)))
                costs[next_row][next_col] = new_cost

    return costs


distances = dijkstra(grid, start_row_idx, start_col_idx)
for row in distances:
    print(*row)

print(distances[end_row_idx][end_col_idx])

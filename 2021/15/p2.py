from queue import PriorityQueue


with open('input.txt') as f:
    cavern = [[int(i) for i in line.strip()] for line in f]

full_cavern = [[((level-1+i+j) % 9)+1 for i in range(5) for level in row] for j in range(5) for row in cavern]

max_row = len(full_cavern)
max_col = len(full_cavern[0])
min_row = 0
min_col = 0

# for row in full_cavern:
#     print(*row, sep='')

def dijkstra(grid, start_row, start_col):
    costs = [[float('inf') for _ in row] for row in grid]
    costs[start_row][start_col] = 0

    q = PriorityQueue()
    q.put((0, (start_row, start_col)))

    visited = set()
    while not q.empty():
        _, (curr_row, curr_col) = q.get()
        visited.add((curr_row, curr_col))
        adjacent = []
        if curr_col-1 >= min_col:  # left
            adjacent.append((curr_row, curr_col-1))
        if curr_col+1 < max_col:  # right
            adjacent.append((curr_row, curr_col+1))
        if curr_row-1 >= min_row:  # up
            adjacent.append((curr_row-1, curr_col))
        if curr_row+1 < max_row:  # down
            adjacent.append((curr_row+1, curr_col))
        for next_row, next_col in adjacent:
            if (next_row, next_col) not in visited:
                old_cost = costs[next_row][next_col]
                new_cost = costs[curr_row][curr_col] + grid[next_row][next_col]
                if new_cost < old_cost:
                    q.put((new_cost, (next_row, next_col)))
                    costs[next_row][next_col] = new_cost

    return costs

distances = dijkstra(full_cavern, 0, 0)
# for row in distances:
#     print(*row)

print(distances[max_row-1][max_col-1])

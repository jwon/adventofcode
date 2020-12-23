grid = []
grid_width = None

def print_grid():
    for row in grid:
        for x in row:
            if x:
                print('#', end='')
            else:
                print('.', end='')
        print('')


if __name__ == '__main__':
    with open('input.txt') as f:
        for line in f:
            row = []
            for char in line.strip():
                if char == '#':
                    row.append(True)
                else:
                    row.append(False)
            grid.append(row)
    grid_width = len(grid[0])

    # print_grid()

    current_row_position = 0
    tree_count = 0
    for row in grid[1:]:
        current_row_position = (current_row_position + 3) % grid_width
        if row[current_row_position]:
            tree_count += 1

    print(tree_count)

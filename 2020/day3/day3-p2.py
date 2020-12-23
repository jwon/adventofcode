def print_grid(grid):
    for row in grid:
        for x in row:
            if x:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def init_grid():
    grid = []
    with open('input.txt') as f:
        for line in f:
            row = []
            for char in line.strip():
                if char == '#':
                    row.append(True)
                else:
                    row.append(False)
            grid.append(row)
    return grid


def count_trees(grid, right_amount, down_amount):
    grid_width = len(grid[0])
    current_row_position = 0
    current_column_position = 0
    tree_count = 0

    while True:
        current_column_position = current_column_position + down_amount
        if current_column_position >= len(grid):
            return tree_count
        current_row_position = (current_row_position + right_amount) % grid_width
        if grid[current_column_position][current_row_position]:
            tree_count += 1


if __name__ == '__main__':
    grid = init_grid()
    # print_grid()

    slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
            ]
    result = 1
    for (right_amount, down_amount) in slopes:
        result *= count_trees(grid, right_amount, down_amount)
    print(result)

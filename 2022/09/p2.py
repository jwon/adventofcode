from collections import namedtuple
# import os


Position = namedtuple('Position', ['x', 'y'])
knots = [Position(0, 0) for _ in range(10)]
visited = {knots[-1]}
with open('input.txt', 'r') as f:
    for motion in f:
        direction, count = motion.strip().split(' ')
        for i in range(int(count)):
            for idx, knot in enumerate(knots):
                if idx == 0:  # move head
                    if direction == 'R':
                        knots[idx] = Position(knot.x+1, knot.y)
                    elif direction == 'U':
                        knots[idx] = Position(knot.x, knot.y-1)
                    elif direction == 'L':
                        knots[idx] = Position(knot.x-1, knot.y)
                    elif direction == 'D':
                        knots[idx] = Position(knot.x, knot.y+1)
                    else:
                        print(f'cannot move head. direction unknown: {direction}')
                else:  # move other knots
                    follow_knot = knots[idx-1]
                    diff_x = follow_knot.x - knot.x
                    diff_y = follow_knot.y - knot.y
                    if abs(diff_x) > 1 or abs(diff_y) > 1:
                        x_direction = 0 if diff_x == 0 else int(diff_x/abs(diff_x))
                        y_direction = 0 if diff_y == 0 else int(diff_y/abs(diff_y))
                        knots[idx] = Position(knot.x + x_direction, knot.y+y_direction)

                if idx == len(knots)-1:
                    visited.add(knots[idx])

            # os.system('clear')
            # print(f'MOTION: {direction} {i+1} of {count}')
            # print(f'Current Knot Index: {idx}')
            # [print(f'{j}: {knots[j]}') for j in range(len(knots))]
            # grid = [['.' for _ in range(26)] for _ in range(26)]
            # for j, knot in enumerate(knots):
            #     if grid[knot.y+15][knot.x+12] == '.':
            #         grid[knot.y+15][knot.x+12] = str(j)
            # for row in grid:
            #     print(''.join(row))
            # print("VISITED")
            # visited_grid = [['.' for _ in range(26)] for _ in range(26)]
            # for knot in visited:
            #     visited_grid[knot.y+15][knot.x+12] = '#'
            # for row in visited_grid:
            #     print(''.join(row))
            # input()

print(len(visited))

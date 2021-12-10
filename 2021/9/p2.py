from math import prod


with open('input.txt') as f:
    heightmap = [[int(height) for height in line.strip()] for line in f]
    x_max = len(heightmap[0])
    y_max = len(heightmap)
    x_min = 0
    y_min = 0

# print(*heightmap, sep='\n')

def is_low_point(heightmap, x_pos, y_pos):
    adjacent_heights = []
    if x_pos-1 >= x_min:
        adjacent_heights.append(heightmap[y_pos][x_pos-1])
    if x_pos+1 < x_max:
        adjacent_heights.append(heightmap[y_pos][x_pos+1])
    if y_pos-1 >= y_min:
        adjacent_heights.append(heightmap[y_pos-1][x_pos])
    if y_pos+1 < y_max:
        adjacent_heights.append(heightmap[y_pos+1][x_pos])

    height = heightmap[y_pos][x_pos]
    return all(height < adjacent_height for adjacent_height in adjacent_heights)

# for y_pos in range(len(heightmap)):
#     for x_pos in range(len(heightmap[y_pos])):
#         if is_low_point(heightmap, x_pos, y_pos):
#             print(f'heightmap[{y_pos}][{x_pos}] = {heightmap[y_pos][x_pos]}')

low_points = [(x_pos, y_pos) for y_pos in range(len(heightmap)) for x_pos in range(len(heightmap[y_pos])) if is_low_point(heightmap, x_pos, y_pos)]

def find_basin_size(x_pos, y_pos, checked=[[None]*x_max for _ in range(y_max)]):
    # print(f'x: {x_pos} y: {y_pos}')
    if x_pos < x_min:
        return 0
    elif y_pos < y_min:
        return 0
    elif x_pos >= x_max:
        return 0
    elif y_pos >= y_max:
        return 0
    elif checked[y_pos][x_pos]:
        return 0
    elif heightmap[y_pos][x_pos] == 9:
        return 0
    else:
        checked[y_pos][x_pos] = True
        return 1 + find_basin_size(x_pos+1, y_pos, checked=checked) + find_basin_size(x_pos-1, y_pos, checked=checked) + find_basin_size(x_pos, y_pos+1, checked=checked) + find_basin_size(x_pos, y_pos-1, checked=checked)

print(prod(sorted(find_basin_size(x_pos, y_pos) for x_pos, y_pos in low_points)[-3:]))

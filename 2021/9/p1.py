with open('input.txt') as f:
    heightmap = [[int(height) for height in line.strip()] for line in f]

# print(*heightmap, sep='\n')

def is_low_point(heightmap, x_pos, y_pos):
    adjacent_heights = []
    x_max = len(heightmap[0])
    y_max = len(heightmap)
    x_min = 0
    y_min = 0
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

print(sum(heightmap[y_pos][x_pos]+1 for y_pos in range(len(heightmap)) for x_pos in range(len(heightmap[y_pos])) if is_low_point(heightmap, x_pos, y_pos)))

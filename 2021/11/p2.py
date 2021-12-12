with open('input.txt') as f:
    octopuses = [[int(char) for char in line.strip()] for line in f]
    x_max = len(octopuses[0])
    y_max = len(octopuses)
    x_min = 0
    y_min = 0

def run_step(octopuses):
    octopuses = [[level+1 for level in row] for row in octopuses]
    flashed = [[0 for _ in row] for row in octopuses]

    while any(level > 9 and flashed[y_pos][x_pos] == 0 for y_pos, row in enumerate(octopuses) for x_pos, level in enumerate(row)):
        for y_pos, row in enumerate(octopuses):
            for x_pos, level in enumerate(row):
                if level > 9 and flashed[y_pos][x_pos] == 0:
                    flashed[y_pos][x_pos] = 1
                    is_safe_left = x_pos-1 >= x_min
                    is_safe_right = x_pos+1 < x_max
                    is_safe_up = y_pos-1 >= y_min
                    is_safe_down = y_pos+1 < y_max
                    if is_safe_left:
                        octopuses[y_pos][x_pos-1] += 1
                    if is_safe_right:
                        octopuses[y_pos][x_pos+1] += 1
                    if is_safe_up:
                        octopuses[y_pos-1][x_pos] += 1
                    if is_safe_down:
                        octopuses[y_pos+1][x_pos] += 1
                    if is_safe_left and is_safe_up:
                        octopuses[y_pos-1][x_pos-1] += 1
                    if is_safe_left and is_safe_down:
                        octopuses[y_pos+1][x_pos-1] += 1
                    if is_safe_right and is_safe_up:
                        octopuses[y_pos-1][x_pos+1] += 1
                    if is_safe_right and is_safe_down:
                        octopuses[y_pos+1][x_pos+1] += 1
    
    for y_pos, row in enumerate(octopuses):
        for x_pos, level in enumerate(row):
            if level > 9:
                octopuses[y_pos][x_pos] = 0

    return octopuses, sum(value for row in flashed for value in row)
    
total_flashes = 0
step = 1
while any(level != 0 for row in octopuses for level in row):
    octopuses, flashes = run_step(octopuses)
    total_flashes += flashes
    print(f'After Step #{step}')
    print(*octopuses, sep='\n')
    step += 1

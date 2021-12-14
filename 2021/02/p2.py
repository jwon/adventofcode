horizontal_pos = 0
vertical_pos = 0
aim = 0

with open('input.txt') as f:
    for line in f:
        tokens = line.strip().split(' ')
        direction = tokens[0]
        amount = int(tokens[1])
        if direction == 'forward':
            horizontal_pos += amount
            vertical_pos += aim * amount
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
        else:
            print('unknown direction')

print(horizontal_pos * vertical_pos)

import sys

cycle_counter = 0
register = 1
pending_add = None
grid = [['.' for _ in range(40)] for _ in range(6)]


def tick_cycle():
    global cycle_counter, register, grid
    if cycle_counter % 40 in range(register-1, register+2):
        grid[int(cycle_counter / 40)][cycle_counter % 40] = '#'
    cycle_counter += 1
    print(f'Cycle #{cycle_counter}: instr: {tokens[0]} register: {register} pending_add: {pending_add}')
    for row in grid:
        print(''.join(row))


with open(sys.argv[1], 'r') as f:
    for line in f:
        tokens = line.strip().split(' ')
        if tokens[0] == 'addx':
            pending_add = int(tokens[1])
        tick_cycle()

        if pending_add is not None:
            tick_cycle()
            register += pending_add
            pending_add = None

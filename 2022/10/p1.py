import sys

cycle_counter = 0
register = 1
pending_add = None
result = 0


def tick_cycle():
    global cycle_counter, register, result
    cycle_counter += 1
    print(f'End of Cycle #{cycle_counter}: instr: {tokens[0]} register: {register} pending_add: {pending_add}')
    if cycle_counter in [20, 60, 100, 140, 180, 220]:
        signal_strength = register * cycle_counter
        print(f'INTERESTING: register: {register} signal_strength: {signal_strength}')
        result += signal_strength


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

print(result)
